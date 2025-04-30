import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
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
    future=True,
)


@pytest.fixture(scope="session")
def event_loop():
    event_loop = asyncio.get_event_loop()
    yield event_loop
    event_loop.close()


@pytest.fixture(scope="session", autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


@pytest.fixture(scope="function")
async def session_fixture() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(engine, class_=AsyncSession, autoflush=True)
    async with async_session() as session:
        yield session
        for table in reversed(SQLModel.metadata.sorted_tables):
            # Use `text()` to wrap the SQL string
            await session.execute(text(f"DELETE FROM {table.name}"))
        await session.commit()


@pytest.fixture
def sign_up_payload():
    return {
        "dob": "2025-04-30T20:15:43",
        "email": "something@example.com",
        "first_name": "john",
        "last_name": "doe",
        "password": "password",
        "username": "username",
    }
