from unittest.mock import AsyncMock, Mock, call

import pytest
from fastapi.exceptions import HTTPException

from app.internals.auth.services import auth_service
from app.internals.user.schema import UserLoginSchema
from tests.internals.user.user_factory import UserDbFactory, UserSchemaFactory


@pytest.mark.asyncio
async def test_create_user(mocker, session):
    user = UserSchemaFactory()
    create_mock = mocker.patch(
        "app.internals.auth.services.auth_service.user_service.create",
        AsyncMock(return_value=user),
    )

    response = await auth_service.create_user(user, session)

    assert response == user
    create_mock.assert_called_once_with(user, session)


@pytest.mark.asyncio
async def test_login(mocker, session):
    credentials = UserLoginSchema(email="test@email.com", password="password")
    db_user = UserDbFactory()
    expected = {"access_token": "token", "refresh_token": "token", "user": db_user}
    user_service_get_mock = mocker.patch(
        "app.internals.auth.services.auth_service.user_service.get",
        AsyncMock(return_value=db_user),
    )
    generate_token_mock = mocker.patch(
        "app.internals.auth.services.auth_service.generate_token",
        Mock(return_value="token"),
    )
    verify_password_mock = mocker.patch(
        "app.internals.auth.services.auth_service.verify_password",
        Mock(return_value=True),
    )
    response = await auth_service.login(credentials, session)

    user_service_get_mock.assert_called_once_with(credentials, session)
    verify_password_mock.assert_called_once_with(
        credentials.password, db_user.password_hash
    )
    assert generate_token_mock.call_args_list == [
        call(db_user, "ACCESS_TOKEN"),
        call(db_user, "REFRESH_TOKEN"),
    ]
    assert response == expected


@pytest.mark.asyncio
async def test_login_catch_exception(mocker, session):
    credentials = UserLoginSchema(email="test@email.com", password="password")
    db_user = UserDbFactory()
    mocker.patch(
        "app.internals.auth.services.auth_service.user_service.get",
        AsyncMock(return_value=db_user),
    )
    mocker.patch(
        "app.internals.auth.services.auth_service.verify_password",
        Mock(return_value=False),
    )

    with pytest.raises(HTTPException):
        await auth_service.login(credentials, session)


@pytest.mark.asyncio
async def test_authenticate():
    response = await auth_service.authenticate()

    assert response == None


@pytest.mark.asyncio
async def test_logout():
    response = await auth_service.logout()

    assert response == None
