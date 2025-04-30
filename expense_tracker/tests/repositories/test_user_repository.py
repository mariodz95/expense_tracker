import pytest
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import user_repository
from tests.factories.user_factory import UserDbFactory, UserSchemaFactory


async def test_create_returns_created_model(session_fixture):
    user_schema = UserSchemaFactory()
    password_hash = "password_hash"

    db_user = await user_repository.create(user_schema, session_fixture, password_hash)

    for field in ["username", "email", "first_name", "last_name", "dob"]:
        assert getattr(db_user, field) == getattr(user_schema, field)

    assert db_user.password_hash == password_hash
    assert db_user.id is not None


async def test_create_catch_exception(mocker):
    user_schema = UserSchemaFactory()
    password_hash = "password_hash"
    session = AsyncSession()

    mocker.patch.object(session, "commit", side_effect=SQLAlchemyError)

    with pytest.raises(HTTPException) as exc_info:
        await user_repository.create(user_schema, session, password_hash)

    exception = exc_info.value
    assert exception.status_code == 409
    assert exception.detail == "User signup failed."


async def test_create_catch_integrity_error_duplicate_email(session_fixture):
    await UserDbFactory.create(email="email@test.com")
    user_schema = UserSchemaFactory.build(email="email@test.com")
    password_hash = "password_hash"

    with pytest.raises(HTTPException) as exc_info:
        await user_repository.create(user_schema, session_fixture, password_hash)

    exception = exc_info.value
    assert exception.status_code == 409
    assert exception.detail == "Email or username is already used."


async def test_create_catch_integrity_error_duplicate_username(session_fixture):
    await UserDbFactory.create(username="testusername")
    user_schema = UserSchemaFactory.build(username="testusername")
    password_hash = "password_hash"

    with pytest.raises(HTTPException):
        await user_repository.create(user_schema, session_fixture, password_hash)


async def test_get(session_fixture):
    expected = await UserDbFactory.create(email="email2@test.com")

    result = await user_repository.get("email2@test.com", session_fixture)

    assert result.email == expected.email
    assert result.username == expected.username
    assert result.password_hash == expected.password_hash
    assert result.id == expected.id


async def test_get_catch_exception(session_fixture):
    await UserDbFactory.create(email="email@test.com")

    with pytest.raises(HTTPException) as exc_info:
        await user_repository.get("email2@test.com", session_fixture)

    exception = exc_info.value
    assert exception.status_code == 404
    assert exception.detail == "Invalid email or password."
