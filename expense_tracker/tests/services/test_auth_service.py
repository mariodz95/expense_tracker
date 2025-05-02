from unittest.mock import AsyncMock, Mock, call

import pytest
from fastapi.exceptions import HTTPException

from app.schemas.user_schema import UserLoginSchema, UserOutputSchema
from app.services import auth_service
from tests.factories.user_factory import UserDbFactory, UserSchemaFactory


async def test_create_user_returns_expected_response(mocker, session_fixture):
    user = UserSchemaFactory.build()

    create_mock = mocker.patch(
        "app.services.auth_service.user_service.create",
        AsyncMock(return_value=user),
    )

    response = await auth_service.create_user(user, session_fixture)

    create_mock.assert_called_once_with(user=user, session=session_fixture)
    assert response == user


async def test_create_user_calls_user_service_once(mocker, session_fixture):
    user = UserSchemaFactory.build()

    create_mock = mocker.patch(
        "app.services.auth_service.user_service.create",
        AsyncMock(return_value=user),
    )

    await auth_service.create_user(user, session_fixture)

    create_mock.assert_called_once_with(user=user, session=session_fixture)


async def test_login(mocker, session_fixture):
    credentials = UserLoginSchema(email="test@email.com", password="password")
    db_user = UserDbFactory.build()
    user_schema = UserOutputSchema(**db_user.model_dump())
    expected = {"access_token": "token", "refresh_token": "token", "user": user_schema}

    user_service_get_mock = mocker.patch(
        "app.services.auth_service.user_repository.get",
        AsyncMock(return_value=db_user),
    )
    generate_token_mock = mocker.patch(
        "app.services.auth_service.generate_token",
        Mock(return_value="token"),
    )
    verify_password_mock = mocker.patch(
        "app.services.auth_service.verify_password",
        Mock(return_value=True),
    )

    response = await auth_service.login(credentials, session_fixture)

    user_service_get_mock.assert_called_once_with(credentials.email, session_fixture)
    verify_password_mock.assert_called_once_with(
        credentials.password, db_user.password_hash
    )
    assert generate_token_mock.call_args_list == [
        call(db_user, "ACCESS_TOKEN"),
        call(db_user, "REFRESH_TOKEN"),
    ]
    assert response == expected


async def test_login_catch_exception(mocker, session_fixture):
    credentials = UserLoginSchema(email="test@email.com", password="password")
    db_user = UserDbFactory.build()
    mocker.patch(
        "app.services.auth_service.user_service.get",
        AsyncMock(return_value=db_user),
    )
    mocker.patch(
        "app.services.auth_service.verify_password",
        Mock(return_value=False),
    )

    with pytest.raises(HTTPException):
        await auth_service.login(credentials, session_fixture)


async def test_authenticate():
    response = await auth_service.authenticate()

    assert response == None


async def test_logout():
    response = await auth_service.logout()

    assert response == None
