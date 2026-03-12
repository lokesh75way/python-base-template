from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from routes.users import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("✅ Application starting up")
    yield
    print("🛑 Application shutting down")


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)


@app.get("/health")
def health():
    return {"status": "success", "message": "API is healthy"}
