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

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    expose_headers=[config.jwt_token_refresh_name],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def app_init():
    # async with engine.begin() as conn:
    #     await conn.run_sync(SQLModel.metadata.create_all)
    print("App startup complete")
