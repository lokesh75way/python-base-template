from uuid import UUID

from models.assistant import (
    Assistant,
    AssistantClientMessage,
    AssistantEndCallPhrase,
    AssistantModelConfig,
    AssistantModelMessage,
    AssistantModelTool,
    AssistantServerMessage,
    AssistantStartSpeakingPlan,
    AssistantTranscriber,
    AssistantVoice,
)
from schema.assistant import AssistantCreate, AssistantUpdate
from services.vapi_service import vapi_service
from sqlalchemy.orm import Session


class AssistantService:
    # ------------------------------------------------------------------ #
    # Read                                                                 #
    # ------------------------------------------------------------------ #

    def get_all(self, db: Session) -> list[Assistant]:
        return db.query(Assistant).all()

    def get_by_id(self, db: Session, assistant_id: UUID) -> Assistant | None:
        return db.query(Assistant).filter(Assistant.id == str(assistant_id)).first()

    def get_by_external_id(self, db: Session, external_id: str) -> Assistant | None:
        return db.query(Assistant).filter(Assistant.external_id == external_id).first()

    # ------------------------------------------------------------------ #
    # Create                                                               #
    # ------------------------------------------------------------------ #

    def create(self, db: Session, payload: AssistantCreate) -> Assistant:
        assistant = Assistant(
            user=payload.user,
            external_id=payload.external_id,
            name=payload.name,
            first_message=payload.first_message,
            voicemail_message=payload.voicemail_message,
            end_call_message=payload.end_call_message,
            hipaa_enabled=payload.hipaa_enabled,
            background_denoising_enabled=payload.background_denoising_enabled,
            is_server_url_secret_set=payload.is_server_url_secret_set,
        )
        db.add(assistant)
        db.flush()  # populate assistant.id before inserting children

        self._sync_children(db, assistant, payload)

        db.commit()
        db.refresh(assistant)
        return assistant

    # ------------------------------------------------------------------ #
    # Update                                                               #
    # ------------------------------------------------------------------ #

    def update(
        self, db: Session, assistant_id: UUID, payload: AssistantUpdate
    ) -> Assistant | None:
        assistant = self.get_by_id(db, assistant_id)
        if not assistant:
            return None

        scalar_fields = (
            "name",
            "first_message",
            "voicemail_message",
            "end_call_message",
            "hipaa_enabled",
            "background_denoising_enabled",
            "is_server_url_secret_set",
        )
        for field in scalar_fields:
            value = getattr(payload, field, None)
            if value is not None:
                setattr(assistant, field, value)

        self._sync_children(db, assistant, payload)

        db.commit()
        db.refresh(assistant)
        return assistant

    # ------------------------------------------------------------------ #
    # Delete                                                               #
    # ------------------------------------------------------------------ #

    def delete(self, db: Session, assistant_id: UUID) -> bool:
        assistant = self.get_by_id(db, assistant_id)
        if not assistant:
            return False
        db.delete(assistant)
        db.commit()
        return True

    # ------------------------------------------------------------------ #
    # Sync from VAPI                                                       #
    # ------------------------------------------------------------------ #

    def sync_from_vapi(self, db: Session) -> list[Assistant]:
        vapi_assistants = vapi_service.list_assistants()
        results = []

        for item in vapi_assistants:
            # --- transcriber ---
            transcriber = None
            if t := item.get("transcriber"):
                transcriber = {
                    "provider": t.get("provider", ""),
                    "language": t.get("language"),
                    "model": t.get("model"),
                    "endpointing": t.get("endpointing"),
                }

            # --- model config ---
            model_config = None
            if m := item.get("model"):
                model_config = {
                    "provider": m.get("provider", ""),
                    "model": m.get("model", ""),
                    "temperature": m.get("temperature"),
                    "messages": [
                        {"role": msg["role"], "content": msg["content"]}
                        for msg in m.get("messages", [])
                    ],
                    "tool_ids": [{"tool_id": tid} for tid in m.get("toolIds", [])],
                }

            # --- voice ---
            voice = None
            if v := item.get("voice"):
                voice = {
                    "provider": v.get("provider", ""),
                    "voice_id": v.get("voiceId", ""),
                }

            # --- start speaking plan ---
            start_speaking_plan = None
            if sp := item.get("startSpeakingPlan"):
                sme = sp.get("smartEndpointingEnabled")
                start_speaking_plan = {
                    "wait_seconds": sp.get("waitSeconds"),
                    "smart_endpointing_enabled": str(sme) if sme is not None else None,
                }

            payload_data = dict(
                external_id=item["id"],
                name=item.get("name", ""),
                user=item.get("orgId", ""),
                first_message=item.get("firstMessage"),
                voicemail_message=item.get("voicemailMessage"),
                end_call_message=item.get("endCallMessage"),
                end_call_phrases=item.get("endCallPhrases") or [],
                client_messages=item.get("clientMessages") or [],
                server_messages=item.get("serverMessages") or [],
                hipaa_enabled=item.get("hipaaEnabled", False),
                background_denoising_enabled=item.get(
                    "backgroundDenoisingEnabled", False
                ),
                is_server_url_secret_set=item.get("isServerUrlSecretSet", False),
                transcriber=transcriber,
                model_config=model_config,
                voice=voice,
                start_speaking_plan=start_speaking_plan,
            )

            existing = self.get_by_external_id(db, item["id"])
            if existing:
                result = self.update(db, existing.id, AssistantUpdate(**payload_data))
            else:
                result = self.create(db, AssistantCreate(**payload_data))

            results.append(result)

        return results

    # ------------------------------------------------------------------ #
    # Private: sync all child rows                                         #
    # ------------------------------------------------------------------ #

    def _sync_children(self, db: Session, assistant: Assistant, payload) -> None:
        self._sync_transcriber(db, assistant, payload)
        self._sync_model_config(db, assistant, payload)
        self._sync_voice(db, assistant, payload)
        self._sync_start_speaking_plan(db, assistant, payload)
        self._sync_list_children(db, assistant, payload)

    def _sync_transcriber(self, db: Session, assistant: Assistant, payload) -> None:
        if payload.transcriber is None:
            return
        data = (
            payload.transcriber
            if isinstance(payload.transcriber, dict)
            else payload.transcriber.model_dump()
        )
        if assistant.transcriber:
            for k, v in data.items():
                setattr(assistant.transcriber, k, v)
        else:
            db.add(AssistantTranscriber(assistant_id=assistant.id, **data))

    def _sync_model_config(self, db: Session, assistant: Assistant, payload) -> None:
        if payload.model_config is None:
            return
        data = (
            payload.model_config
            if isinstance(payload.model_config, dict)
            else payload.model_config.model_dump()
        )
        messages = data.pop("messages") or []
        tool_ids = data.pop("tool_ids") or []

        if assistant.model_config:
            cfg = assistant.model_config
            for k, v in data.items():
                setattr(cfg, k, v)
            # replace messages and tools
            db.query(AssistantModelMessage).filter_by(model_config_id=cfg.id).delete()
            db.query(AssistantModelTool).filter_by(model_config_id=cfg.id).delete()
        else:
            cfg = AssistantModelConfig(assistant_id=assistant.id, **data)
            db.add(cfg)
            db.flush()

        for msg in messages:
            db.add(AssistantModelMessage(model_config_id=cfg.id, **msg))
        for tool in tool_ids:
            db.add(AssistantModelTool(model_config_id=cfg.id, **tool))

    def _sync_voice(self, db: Session, assistant: Assistant, payload) -> None:
        if payload.voice is None:
            return
        data = (
            payload.voice
            if isinstance(payload.voice, dict)
            else payload.voice.model_dump()
        )
        if assistant.voice:
            for k, v in data.items():
                setattr(assistant.voice, k, v)
        else:
            db.add(AssistantVoice(assistant_id=assistant.id, **data))

    def _sync_start_speaking_plan(
        self, db: Session, assistant: Assistant, payload
    ) -> None:
        if payload.start_speaking_plan is None:
            return
        data = (
            payload.start_speaking_plan
            if isinstance(payload.start_speaking_plan, dict)
            else payload.start_speaking_plan.model_dump()
        )
        if assistant.start_speaking_plan:
            for k, v in data.items():
                setattr(assistant.start_speaking_plan, k, v)
        else:
            db.add(AssistantStartSpeakingPlan(assistant_id=assistant.id, **data))

    def _sync_list_children(self, db: Session, assistant: Assistant, payload) -> None:
        if payload.end_call_phrases is not None:
            db.query(AssistantEndCallPhrase).filter_by(
                assistant_id=assistant.id
            ).delete()
            for phrase in payload.end_call_phrases:
                db.add(AssistantEndCallPhrase(assistant_id=assistant.id, phrase=phrase))

        if payload.client_messages is not None:
            db.query(AssistantClientMessage).filter_by(
                assistant_id=assistant.id
            ).delete()
            for msg in payload.client_messages:
                db.add(AssistantClientMessage(assistant_id=assistant.id, message=msg))

        if payload.server_messages is not None:
            db.query(AssistantServerMessage).filter_by(
                assistant_id=assistant.id
            ).delete()
            for msg in payload.server_messages:
                db.add(AssistantServerMessage(assistant_id=assistant.id, message=msg))

    # ------------------------------------------------------------------ #
    # Clone helpers                                                        #
    # ------------------------------------------------------------------ #

    def clone(
        self, db: Session, assistant_id: UUID, target_user: str
    ) -> Assistant | None:
        """
        Clone an existing assistant and assign it to a different (or same) user.
        Steps:
          1. Load source from DB.
          2. POST to VAPI to create a brand-new assistant (gets a new external_id).
          3. Persist locally with target_user as the owner.
        """
        source = self.get_by_id(db, assistant_id)
        if not source:
            return None

        # Push clone to VAPI
        vapi_payload = self._build_vapi_payload(source)
        vapi_response = vapi_service.create_assistant(vapi_payload)
        new_external_id = (
            vapi_response.id if hasattr(vapi_response, "id") else vapi_response["id"]
        )

        # Build local create payload from source
        clone_payload = AssistantCreate(
            user=target_user,
            external_id=new_external_id,
            name=source.name,
            first_message=source.first_message,
            voicemail_message=source.voicemail_message,
            end_call_message=source.end_call_message,
            end_call_phrases=[p.phrase for p in (source.end_call_phrases or [])],
            client_messages=[m.message for m in (source.client_messages or [])],
            server_messages=[m.message for m in (source.server_messages or [])],
            hipaa_enabled=source.hipaa_enabled,
            background_denoising_enabled=source.background_denoising_enabled,
            is_server_url_secret_set=source.is_server_url_secret_set,
            transcriber=self._clone_transcriber(source),
            model_config=self._clone_model_config(source),
            voice=self._clone_voice(source),
            start_speaking_plan=self._clone_start_speaking_plan(source),
        )

        return self.create(db, clone_payload)

    def _build_vapi_payload(self, source: Assistant) -> dict:
        """
        Converts a local Assistant ORM object into a VAPI-compatible dict.
        None values are stripped so VAPI does not reject the payload.
        """

        def strip_none(d: dict) -> dict:
            return {k: v for k, v in d.items() if v is not None}

        payload: dict = {"name": source.name}

        if source.first_message:
            payload["firstMessage"] = source.first_message
        if source.voicemail_message:
            payload["voicemailMessage"] = source.voicemail_message
        if source.end_call_message:
            payload["endCallMessage"] = source.end_call_message
        if source.end_call_phrases:
            payload["endCallPhrases"] = [p.phrase for p in source.end_call_phrases]
        if source.client_messages:
            payload["clientMessages"] = [m.message for m in source.client_messages]
        if source.server_messages:
            payload["serverMessages"] = [m.message for m in source.server_messages]

        payload["hipaaEnabled"] = source.hipaa_enabled
        payload["backgroundDenoisingEnabled"] = source.background_denoising_enabled

        if t := source.transcriber:
            payload["transcriber"] = strip_none(
                {
                    "provider": t.provider,
                    "language": t.language,
                    "model": t.model,
                    "endpointing": t.endpointing,
                }
            )

        if m := source.model_config:
            model_dict: dict = strip_none(
                {
                    "provider": m.provider,
                    "model": m.model,
                    "temperature": m.temperature,
                }
            )
            model_dict["messages"] = [
                {"role": msg.role, "content": msg.content} for msg in (m.messages or [])
            ]
            tool_ids = [tool.tool_id for tool in (m.tool_ids or [])]
            if tool_ids:
                model_dict["toolIds"] = tool_ids
            payload["model"] = model_dict

        if v := source.voice:
            payload["voice"] = {"provider": v.provider, "voiceId": v.voice_id}

        if sp := source.start_speaking_plan:
            payload["startSpeakingPlan"] = strip_none(
                {
                    "waitSeconds": sp.wait_seconds,
                    "smartEndpointingEnabled": sp.smart_endpointing_enabled,
                }
            )

        return payload

    def _clone_transcriber(self, source: Assistant):
        if not source.transcriber:
            return None
        from schema.assistant import TranscriberCreate

        return TranscriberCreate(
            provider=source.transcriber.provider,
            language=source.transcriber.language,
            model=source.transcriber.model,
            endpointing=source.transcriber.endpointing,
        )

    def _clone_model_config(self, source: Assistant):
        if not source.model_config:
            return None
        from schema.assistant import (
            AssistantModelConfigCreate,
            ModelMessageCreate,
            ModelToolCreate,
        )

        return AssistantModelConfigCreate(
            provider=source.model_config.provider,
            model=source.model_config.model,
            temperature=source.model_config.temperature,
            messages=[
                ModelMessageCreate(role=m.role, content=m.content)
                for m in (source.model_config.messages or [])
            ],
            tool_ids=[
                ModelToolCreate(tool_id=t.tool_id)
                for t in (source.model_config.tool_ids or [])
            ],
        )

    def _clone_voice(self, source: Assistant):
        if not source.voice:
            return None
        from schema.assistant import VoiceCreate

        return VoiceCreate(
            provider=source.voice.provider, voice_id=source.voice.voice_id
        )

    def _clone_start_speaking_plan(self, source: Assistant):
        if not source.start_speaking_plan:
            return None
        from schema.assistant import StartSpeakingPlanCreate

        return StartSpeakingPlanCreate(
            wait_seconds=source.start_speaking_plan.wait_seconds,
            smart_endpointing_enabled=source.start_speaking_plan.smart_endpointing_enabled,
        )


assistant_service = AssistantService()
