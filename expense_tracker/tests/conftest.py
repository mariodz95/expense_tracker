import pytest
from fastapi.testclient import TestClient
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, SQLModel
from typing import Optional
from app.database.setup import engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from app.database.setup import get_session

from app.main import app


@pytest.fixture
def client():

    return TestClient(app)



@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session): 
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override 

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear() 
