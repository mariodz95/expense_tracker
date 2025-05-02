from pydantic import BaseModel

from app.util import populate_env_vars


class Config(BaseModel):
    allowed_origins: str
    api_docs_enabled: bool
    jwt_algorithm: str
    jwt_token_access_name: str
    jwt_token_refresh_name: str
    jwt_access_expiration: int
    jwt_refresh_expiration: int
    jwt_secret: str
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_port: str
    redis_uri: str
    title: str


def get_config() -> Config:
    env_vars = populate_env_vars(Config)

    return Config(**env_vars)
