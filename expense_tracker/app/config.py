from pydantic import BaseModel

from app.util import populate_env_vars


class Config(BaseModel):
    title: str
    api_docs_enabled: bool
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_port: str
    redis_uri: str
    jwt_algorithm: str
    jwt_token_access_name: str
    jwt_token_refresh_name: str
    jwt_expiration: int
    jwt_secret: str


def get_config() -> Config:
    env_vars = populate_env_vars(Config)

    return Config(**env_vars)
