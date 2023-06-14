from redis import asyncio as aioredis
from redis.asyncio.client import Redis
from app.config import get_config

config = get_config()


def connection() -> Redis:
    return aioredis.from_url(config.redis_uri, decoded_responses=True)
