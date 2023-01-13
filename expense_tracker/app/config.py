from pydantic import BaseModel

from app.util import populate_env_vars


class Config(BaseModel):
    title: str
    api_docs_enabled: bool
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_port: str


def get_config() -> Config:
    env_vars = populate_env_vars(Config)

    return Config(**env_vars)
