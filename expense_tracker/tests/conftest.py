import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.pool import StaticPool

from app.main import app
from tests.utilities import create_config_dict


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def config_dict():
    return create_config_dict()


engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@db:5432/test_expense_tracker",
    poolclass=StaticPool,
    echo=True,
)


@pytest.fixture(scope="session")
def event_loop():
    """Overrides pytest default function scoped event loop"""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)


@pytest.fixture(scope="function")
async def session_fixture() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(engine, class_=AsyncSession, autoflush=True)
    async with async_session() as session:
        yield session
        for table in reversed(SQLModel.metadata.sorted_tables):
            await session.execute("DELETE FROM " + table.name)
        await session.commit()
