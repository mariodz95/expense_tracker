import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from app.database.setup import get_session

from app.main import app
from tests.utilities import create_config_dict


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def config_dict():
    return create_config_dict()


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
