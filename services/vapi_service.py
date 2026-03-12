from typing import Any, Optional

from core.config import settings
from vapi import Vapi


class VapiService:
    def __init__(self, api_key: str):
        """
        Initialize the Vapi client.

        Args:
            api_key: Your Vapi API key (Bearer token).
        """
        self.client = Vapi(token=api_key)

    # -------------------------------------------------------------------------
    # Assistants
    # -------------------------------------------------------------------------

    def create_assistant(self, payload: dict) -> Any:
        """POST /assistant — Create an assistant."""
        return self.client.assistants.create(**payload)

    def list_assistants(
        self,
        limit: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /assistant — List all assistants."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.assistants.list(**params)

    def get_assistant(self, assistant_id: str) -> Any:
        """GET /assistant/{id} — Get a single assistant."""
        return self.client.assistants.get(assistant_id)

    def update_assistant(self, assistant_id: str, payload: dict) -> Any:
        """PATCH /assistant/{id} — Update an assistant."""
        return self.client.assistants.update(assistant_id, **payload)

    def delete_assistant(self, assistant_id: str) -> Any:
        """DELETE /assistant/{id} — Delete an assistant."""
        return self.client.assistants.delete(assistant_id)

    # -------------------------------------------------------------------------
    # Squads
    # -------------------------------------------------------------------------

    def create_squad(self, payload: dict) -> Any:
        """POST /squad — Create a squad."""
        return self.client.squads.create(**payload)

    def list_squads(
        self,
        limit: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /squad — List all squads."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.squads.list(**params)

    def get_squad(self, squad_id: str) -> Any:
        """GET /squad/{id} — Get a single squad."""
        return self.client.squads.get(squad_id)

    def update_squad(self, squad_id: str, payload: dict) -> Any:
        """PATCH /squad/{id} — Update a squad."""
        return self.client.squads.update(squad_id, **payload)

    def delete_squad(self, squad_id: str) -> Any:
        """DELETE /squad/{id} — Delete a squad."""
        return self.client.squads.delete(squad_id)

    # -------------------------------------------------------------------------
    # Calls
    # -------------------------------------------------------------------------

    def create_call(self, payload: dict) -> Any:
        """POST /call — Create / initiate a call."""
        return self.client.calls.create(**payload)

    def list_calls(
        self,
        limit: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /call — List all calls."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.calls.list(**params)

    def get_call(self, call_id: str) -> Any:
        """GET /call/{id} — Get a single call."""
        return self.client.calls.get(call_id)

    def update_call(self, call_id: str, payload: dict) -> Any:
        """PATCH /call/{id} — Update a call."""
        return self.client.calls.update(call_id, **payload)

    def delete_call(self, call_id: str) -> Any:
        """DELETE /call/{id} — Delete call data."""
        return self.client.calls.delete(call_id)

    # -------------------------------------------------------------------------
    # Chats
    # -------------------------------------------------------------------------

    def list_chats(
        self,
        limit: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /chat — List all chats."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.chats.list(**params)

    def create_chat(self, payload: dict) -> Any:
        """POST /chat — Create a chat."""
        return self.client.chats.create(**payload)

    def get_chat(self, chat_id: str) -> Any:
        """GET /chat/{id} — Get a single chat."""
        return self.client.chats.get(chat_id)

    def delete_chat(self, chat_id: str) -> Any:
        """DELETE /chat/{id} — Delete a chat."""
        return self.client.chats.delete(chat_id)

    def create_openai_chat(self, payload: dict) -> Any:
        """POST /chat/responses — Create a chat (OpenAI-compatible)."""
        return self.client.chats.create_openai(**payload)

    # -------------------------------------------------------------------------
    # Campaigns
    # -------------------------------------------------------------------------

    def create_campaign(self, payload: dict) -> Any:
        """POST /campaign — Create a campaign."""
        return self.client.campaigns.create(**payload)

    def list_campaigns(
        self,
        limit: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /campaign — List all campaigns."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.campaigns.list(**params)

    def get_campaign(self, campaign_id: str) -> Any:
        """GET /campaign/{id} — Get a single campaign."""
        return self.client.campaigns.get(campaign_id)

    def update_campaign(self, campaign_id: str, payload: dict) -> Any:
        """PATCH /campaign/{id} — Update a campaign."""
        return self.client.campaigns.update(campaign_id, **payload)

    def delete_campaign(self, campaign_id: str) -> Any:
        """DELETE /campaign/{id} — Delete a campaign."""
        return self.client.campaigns.delete(campaign_id)

    # -------------------------------------------------------------------------
    # Sessions
    # -------------------------------------------------------------------------

    def create_session(self, payload: dict) -> Any:
        """POST /session — Create a session."""
        return self.client.sessions.create(**payload)

    def list_sessions(
        self,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /session — List sessions (paginated)."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "page": page,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.sessions.list(**params)

    def get_session(self, session_id: str) -> Any:
        """GET /session/{id} — Get a single session."""
        return self.client.sessions.get(session_id)

    def update_session(self, session_id: str, payload: dict) -> Any:
        """PATCH /session/{id} — Update a session."""
        return self.client.sessions.update(session_id, **payload)

    def delete_session(self, session_id: str) -> Any:
        """DELETE /session/{id} — Delete a session."""
        return self.client.sessions.delete(session_id)

    # -------------------------------------------------------------------------
    # Phone Numbers
    # -------------------------------------------------------------------------

    def create_phone_number(self, payload: dict) -> Any:
        """POST /phone-number — Create / import a phone number."""
        return self.client.phone_numbers.create(**payload)

    def list_phone_numbers(
        self,
        limit: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /phone-number — List all phone numbers."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.phone_numbers.list(**params)

    def list_phone_numbers_paginated(
        self,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        sort_order: Optional[str] = None,
    ) -> Any:
        """GET /v2/phone-number — List phone numbers (paginated v2)."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "page": page,
                "sort_order": sort_order,
            }.items()
            if v is not None
        }
        return self.client.phone_numbers.list_paginated(**params)

    def get_phone_number(self, phone_number_id: str) -> Any:
        """GET /phone-number/{id} — Get a single phone number."""
        return self.client.phone_numbers.get(phone_number_id)

    def update_phone_number(self, phone_number_id: str, payload: dict) -> Any:
        """PATCH /phone-number/{id} — Update a phone number."""
        return self.client.phone_numbers.update(phone_number_id, **payload)

    def delete_phone_number(self, phone_number_id: str) -> Any:
        """DELETE /phone-number/{id} — Delete a phone number."""
        return self.client.phone_numbers.delete(phone_number_id)

    # -------------------------------------------------------------------------
    # Tools
    # -------------------------------------------------------------------------

    def create_tool(self, payload: dict) -> Any:
        """POST /tool — Create a tool."""
        return self.client.tools.create(**payload)

    def list_tools(
        self,
        limit: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /tool — List all tools."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.tools.list(**params)

    def get_tool(self, tool_id: str) -> Any:
        """GET /tool/{id} — Get a single tool."""
        return self.client.tools.get(tool_id)

    def update_tool(self, tool_id: str, payload: dict) -> Any:
        """PATCH /tool/{id} — Update a tool."""
        return self.client.tools.update(tool_id, **payload)

    def delete_tool(self, tool_id: str) -> Any:
        """DELETE /tool/{id} — Delete a tool."""
        return self.client.tools.delete(tool_id)

    def test_code_tool(self, payload: dict) -> Any:
        """POST /tool/code/test — Test code tool execution."""
        return self.client.tools.test_code_execution(**payload)

    def discover_mcp_children(self, tool_id: str, payload: dict) -> Any:
        """POST /tool/{id}/mcp-children — Discover MCP child tools."""
        return self.client.tools.discover_mcp_children(tool_id, **payload)

    # -------------------------------------------------------------------------
    # Files
    # -------------------------------------------------------------------------

    def upload_file(self, file, name: Optional[str] = None) -> Any:
        """POST /file — Upload a file."""
        return self.client.files.create(file=file, name=name)

    def list_files(
        self,
        limit: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /file — List all files."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.files.list(**params)

    def get_file(self, file_id: str) -> Any:
        """GET /file/{id} — Get a single file."""
        return self.client.files.get(file_id)

    def update_file(self, file_id: str, payload: dict) -> Any:
        """PATCH /file/{id} — Update a file."""
        return self.client.files.update(file_id, **payload)

    def delete_file(self, file_id: str) -> Any:
        """DELETE /file/{id} — Delete a file."""
        return self.client.files.delete(file_id)

    # -------------------------------------------------------------------------
    # Structured Outputs
    # -------------------------------------------------------------------------

    def list_structured_outputs(
        self,
        limit: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /structured-output — List all structured outputs."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.structured_outputs.list(**params)

    def create_structured_output(self, payload: dict) -> Any:
        """POST /structured-output — Create a structured output."""
        return self.client.structured_outputs.create(**payload)

    def get_structured_output(self, structured_output_id: str) -> Any:
        """GET /structured-output/{id} — Get a single structured output."""
        return self.client.structured_outputs.get(structured_output_id)

    def update_structured_output(self, structured_output_id: str, payload: dict) -> Any:
        """PATCH /structured-output/{id} — Update a structured output."""
        return self.client.structured_outputs.update(structured_output_id, **payload)

    def delete_structured_output(self, structured_output_id: str) -> Any:
        """DELETE /structured-output/{id} — Delete a structured output."""
        return self.client.structured_outputs.delete(structured_output_id)

    def run_structured_output(self, payload: dict) -> Any:
        """POST /structured-output/run — Run a structured output."""
        return self.client.structured_outputs.run(**payload)

    # -------------------------------------------------------------------------
    # Reporting / Insights
    # -------------------------------------------------------------------------

    def create_insight(self, payload: dict) -> Any:
        """POST /reporting/insight — Create an insight."""
        return self.client.insights.create(**payload)

    def list_insights(
        self,
        limit: Optional[int] = None,
        created_at_gt: Optional[str] = None,
        created_at_lt: Optional[str] = None,
        created_at_ge: Optional[str] = None,
        created_at_le: Optional[str] = None,
        updated_at_gt: Optional[str] = None,
        updated_at_lt: Optional[str] = None,
        updated_at_ge: Optional[str] = None,
        updated_at_le: Optional[str] = None,
    ) -> Any:
        """GET /reporting/insight — Get all insights."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "created_at_gt": created_at_gt,
                "created_at_lt": created_at_lt,
                "created_at_ge": created_at_ge,
                "created_at_le": created_at_le,
                "updated_at_gt": updated_at_gt,
                "updated_at_lt": updated_at_lt,
                "updated_at_ge": updated_at_ge,
                "updated_at_le": updated_at_le,
            }.items()
            if v is not None
        }
        return self.client.insights.list(**params)

    def get_insight(self, insight_id: str) -> Any:
        """GET /reporting/insight/{id} — Get a single insight."""
        return self.client.insights.get(insight_id)

    def update_insight(self, insight_id: str, payload: dict) -> Any:
        """PATCH /reporting/insight/{id} — Update an insight."""
        return self.client.insights.update(insight_id, **payload)

    def delete_insight(self, insight_id: str) -> Any:
        """DELETE /reporting/insight/{id} — Delete an insight."""
        return self.client.insights.delete(insight_id)

    def run_insight(self, insight_id: str) -> Any:
        """POST /reporting/insight/{id}/run — Run an insight."""
        return self.client.insights.run(insight_id)

    def preview_insight(self, payload: dict) -> Any:
        """POST /reporting/insight/preview — Preview an insight."""
        return self.client.insights.preview(**payload)

    # -------------------------------------------------------------------------
    # Evals
    # -------------------------------------------------------------------------

    def create_eval(self, payload: dict) -> Any:
        """POST /eval — Create an eval."""
        return self.client.evals.create(**payload)

    def list_evals(
        self,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        sort_order: Optional[str] = None,
    ) -> Any:
        """GET /eval — List evals (paginated)."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "page": page,
                "sort_order": sort_order,
            }.items()
            if v is not None
        }
        return self.client.evals.list(**params)

    def get_eval(self, eval_id: str) -> Any:
        """GET /eval/{id} — Get a single eval."""
        return self.client.evals.get(eval_id)

    def update_eval(self, eval_id: str, payload: dict) -> Any:
        """PATCH /eval/{id} — Update an eval."""
        return self.client.evals.update(eval_id, **payload)

    def delete_eval(self, eval_id: str) -> Any:
        """DELETE /eval/{id} — Delete an eval."""
        return self.client.evals.delete(eval_id)

    def run_eval(self, payload: dict) -> Any:
        """POST /eval/run — Create an eval run."""
        return self.client.evals.run(**payload)

    def list_eval_runs(
        self,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        sort_order: Optional[str] = None,
    ) -> Any:
        """GET /eval/run — List eval runs (paginated)."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "page": page,
                "sort_order": sort_order,
            }.items()
            if v is not None
        }
        return self.client.evals.list_runs(**params)

    def get_eval_run(self, eval_run_id: str) -> Any:
        """GET /eval/run/{id} — Get a single eval run."""
        return self.client.evals.get_run(eval_run_id)

    def delete_eval_run(self, eval_run_id: str) -> Any:
        """DELETE /eval/run/{id} — Delete an eval run."""
        return self.client.evals.delete_run(eval_run_id)

    # -------------------------------------------------------------------------
    # Observability / Scorecards
    # -------------------------------------------------------------------------

    def create_scorecard(self, payload: dict) -> Any:
        """POST /observability/scorecard — Create a scorecard."""
        return self.client.scorecards.create(**payload)

    def list_scorecards(
        self,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        sort_order: Optional[str] = None,
    ) -> Any:
        """GET /observability/scorecard — List scorecards (paginated)."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "page": page,
                "sort_order": sort_order,
            }.items()
            if v is not None
        }
        return self.client.scorecards.list(**params)

    def get_scorecard(self, scorecard_id: str) -> Any:
        """GET /observability/scorecard/{id} — Get a single scorecard."""
        return self.client.scorecards.get(scorecard_id)

    def update_scorecard(self, scorecard_id: str, payload: dict) -> Any:
        """PATCH /observability/scorecard/{id} — Update a scorecard."""
        return self.client.scorecards.update(scorecard_id, **payload)

    def delete_scorecard(self, scorecard_id: str) -> Any:
        """DELETE /observability/scorecard/{id} — Delete a scorecard."""
        return self.client.scorecards.delete(scorecard_id)

    # -------------------------------------------------------------------------
    # Provider Resources
    # -------------------------------------------------------------------------

    def create_provider_resource(
        self, provider: str, resource_name: str, payload: dict
    ) -> Any:
        """POST /provider/{provider}/{resourceName} — Create a provider resource."""
        return self.client.provider_resources.create(
            provider=provider, resource_name=resource_name, **payload
        )

    def list_provider_resources(
        self,
        provider: str,
        resource_name: str,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> Any:
        """GET /provider/{provider}/{resourceName} — List provider resources (paginated)."""
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "page": page,
            }.items()
            if v is not None
        }
        return self.client.provider_resources.list(
            provider=provider, resource_name=resource_name, **params
        )

    def get_provider_resource(
        self, provider: str, resource_name: str, resource_id: str
    ) -> Any:
        """GET /provider/{provider}/{resourceName}/{id} — Get a provider resource."""
        return self.client.provider_resources.get(
            provider=provider, resource_name=resource_name, resource_id=resource_id
        )

    def update_provider_resource(
        self, provider: str, resource_name: str, resource_id: str, payload: dict
    ) -> Any:
        """PATCH /provider/{provider}/{resourceName}/{id} — Update a provider resource."""
        return self.client.provider_resources.update(
            provider=provider,
            resource_name=resource_name,
            resource_id=resource_id,
            **payload,
        )

    def delete_provider_resource(
        self, provider: str, resource_name: str, resource_id: str
    ) -> Any:
        """DELETE /provider/{provider}/{resourceName}/{id} — Delete a provider resource."""
        return self.client.provider_resources.delete(
            provider=provider, resource_name=resource_name, resource_id=resource_id
        )

    # -------------------------------------------------------------------------
    # Analytics
    # -------------------------------------------------------------------------

    def query_analytics(self, payload: dict) -> Any:
        """POST /analytics — Create analytics queries."""
        return self.client.analytics.query(**payload)


vapi_service = VapiService(api_key=settings.VAPI_API_KEY)
