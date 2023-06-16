import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.database.setup import get_session
from app.main import app
from tests.utilities import create_config_dict

# @pytest.fixture
# def client():
#     return TestClient(app)


@pytest.fixture
def config_dict():
    return create_config_dict()


engine = create_engine(
    "postgresql+asyncpg://postgres:postgres@postgres:5432/test_expense_tracker",
    poolclass=StaticPool,
    echo=True,
)


@pytest.fixture(name="session")
async def session_fixture():
    SQLModel.metadata.create_all(engine)
    async with AsyncSession(engine) as session:
        yield session


# @pytest.fixture()
# async def test_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)
#     yield
#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.drop_all)


# @pytest.fixture(scope="function")
# async def session_fixture() -> AsyncGenerator[AsyncSession, None]:


# @pytest.fixture(name="session")
# def session_fixture():
#     engine = create_engine(
#         "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
#     )
#     SQLModel.metadata.create_all(engine)
#     with Session(engine) as session:
#         yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
