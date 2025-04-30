from unittest.mock import AsyncMock, Mock

from app.schemas.user_schema import UserLoginSchema, UserOutputSchema
from app.services import user_service
from tests.factories.user_factory import UserDbFactory, UserSchemaFactory


async def test_create_returns_expected_response(mocker, session_fixture):
    user = UserSchemaFactory()
    db_user = UserDbFactory.build()
    expected = UserOutputSchema(**db_user.model_dump())

    utils_get_password_hash_mock = mocker.patch(
        "app.services.user_service.auth_utils.get_password_hash",
        Mock(return_value="password_hash"),
    )
    user_repository_create_mock = mocker.patch(
        "app.services.user_service.user_repository.create",
        AsyncMock(return_value=db_user),
    )
    response = await user_service.create(user, session_fixture)

    assert response == expected


async def test_create_calls_auth_utils_once(mocker, session_fixture):
    user = UserSchemaFactory()
    db_user = UserDbFactory.build()

    utils_get_password_hash_mock = mocker.patch(
        "app.services.user_service.auth_utils.get_password_hash",
        Mock(return_value="password_hash"),
    )
    mocker.patch(
        "app.services.user_service.user_repository.create",
        AsyncMock(return_value=db_user),
    )
    await user_service.create(user, session_fixture)

    utils_get_password_hash_mock.assert_called_once_with(
        user.password.get_secret_value()
    )


async def test_create_calls_user_repository_once(mocker, session_fixture):
    user = UserSchemaFactory()
    db_user = UserDbFactory.build()

    mocker.patch(
        "app.services.user_service.auth_utils.get_password_hash",
        Mock(return_value="password_hash"),
    )
    user_repository_create_mock = mocker.patch(
        "app.services.user_service.user_repository.create",
        AsyncMock(return_value=db_user),
    )
    await user_service.create(user, session_fixture)

    user_repository_create_mock.assert_called_once_with(
        user, session_fixture, "password_hash"
    )


async def test_get(mocker, session_fixture):
    credentials = UserLoginSchema(email="test@email.com", password="password")
    user = UserDbFactory.build()
    expected = UserOutputSchema(**user.model_dump())
    user_repository_get_mock = mocker.patch(
        "app.services.user_service.user_repository.get",
        AsyncMock(return_value=user),
    )

    response = await user_service.get(credentials, session_fixture)

    assert response == expected
    user_repository_get_mock.assert_called_once_with(credentials.email, session_fixture)
