from redis.asyncio.client import Redis
from redis.asyncio.connection import ConnectionPool

from app.config import get_config

config = get_config()

pool = ConnectionPool.from_url(config.redis_uri, decode_responses=True)


def connection() -> Redis:
    return Redis(connection_pool=pool)
