from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_config
from app.routers.router import router


def app_settings() -> dict:
    config = get_config()
    settings = {"title": config.title}
    if not config.api_docs_enabled:
        settings["docs_url"] = None
        settings["redoc_url"] = None

    return settings


app = FastAPI(**app_settings())
app.include_router(router)
config = get_config()

origins = [config.allowed_origins]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    expose_headers=[config.jwt_token_refresh_name],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App startup complete")
