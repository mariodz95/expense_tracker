from fastapi import FastAPI

from app.routers.router import router
from app.config import get_config


def app_settings() -> dict:
    config = get_config()
    settings = {"title": config.title}
    if not config.api_docs_enabled:
        settings["docs_url"] = None
        settings["redoc_url"] = None
    
    return settings


app = FastAPI(**app_settings())
app.include_router(router)


@app.on_event("startup")
async def app_init():
    print("App startup complete")
