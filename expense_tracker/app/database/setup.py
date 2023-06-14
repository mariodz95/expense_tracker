from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import get_config


config = get_config()
DATABASE_URL = f"postgresql+asyncpg://{config.postgres_user}:{config.postgres_password}@db:{config.postgres_port}/{config.postgres_db}"
engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
