import pytest
import pytest_asyncio
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_model import UserDb
from app.repositories import user_repository
from tests.factories.user_factory import UserDbFactory, UserSchemaFactory


@pytest_asyncio.fixture(loop_scope="session")
async def test_create(session_fixture):
    user_schema = UserSchemaFactory()
    password_hash = "password_hash"
    expected = UserDb(password_hash=password_hash, **user_schema.model_dump())

    db_user = await user_repository.create(user_schema, session_fixture, password_hash)

    assert db_user.password_hash == password_hash
    assert db_user.username == user_schema.username
    assert db_user.email == user_schema.email
    assert db_user.id != None


@pytest_asyncio.fixture(loop_scope="session")
async def test_create_catch_exception(mocker, session_fixture):
    user_schema = UserSchemaFactory()
    password_hash = "password_hash"
    session = AsyncSession()

    mocker.patch.object(session, "commit", side_effect=SQLAlchemyError)

    with pytest.raises(HTTPException):
        await user_repository.create(user_schema, session_fixture, password_hash)


@pytest_asyncio.fixture(loop_scope="session")
async def test_create_catch_integrity_error_duplicate_email(session_fixture):
    await UserDbFactory.create(email="email@test.com")
    user_schema = UserSchemaFactory.build(email="email@test.com")
    password_hash = "password_hash"

    with pytest.raises(HTTPException):
        await user_repository.create(user_schema, session_fixture, password_hash)


@pytest_asyncio.fixture(loop_scope="session")
async def test_create_catch_integrity_error_duplicate_username(session_fixture):
    await UserDbFactory.create(username="testusername")
    user_schema = UserSchemaFactory.build(username="testusername")
    password_hash = "password_hash"

    with pytest.raises(HTTPException):
        await user_repository.create(user_schema, session_fixture, password_hash)


@pytest_asyncio.fixture(loop_scope="session")
async def test_get(session_fixture):
    expected = await UserDbFactory.create(email="email2@test.com")

    result = await user_repository.get("email2@test.com", session_fixture)

    assert result.email == expected.email
    assert result.username == expected.username
    assert result.password_hash == expected.password_hash
    assert result.id == expected.id


@pytest_asyncio.fixture(loop_scope="session")
async def test_get_catch_exception(session_fixture):
    await UserDbFactory.create(email="email@test.com")

    with pytest.raises(HTTPException):
        await user_repository.get("email2@test.com", session_fixture)
