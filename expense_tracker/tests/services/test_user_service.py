from unittest.mock import AsyncMock, Mock

from app.schemas.user_schema import UserLoginSchema, UserOutputSchema
from app.services import user_service
from tests.factories.user_factory import UserDbFactory, UserSchemaFactory


async def test_create(mocker, session_fixture):
    user = UserSchemaFactory()
    db_user = UserDbFactory.build()
    expected = UserOutputSchema(**db_user.model_dump())

    utils_get_password_hash_mock = mocker.patch(
        "app.services.user_service.utils.get_password_hash",
        Mock(return_value="password_hash"),
    )
    user_repository_create_mock = mocker.patch(
        "app.services.user_service.user_repository.create",
        AsyncMock(return_value=db_user),
    )
    response = await user_service.create(user, session_fixture)

    assert response == expected
    utils_get_password_hash_mock.assert_called_once_with(
        user.password.get_secret_value()
    )
    user_repository_create_mock.assert_called_once_with(
        user, session_fixture, "password_hash"
    )


async def test_get(mocker, session_fixture):
    credentials = UserLoginSchema(email="test@email.com", password="password")
    user = UserDbFactory.build()
    expected = user
    user_repository_get_mock = mocker.patch(
        "app.services.user_service.user_repository.get",
        AsyncMock(return_value=user),
    )

    response = await user_service.get(credentials, session_fixture)

    assert response == expected
    user_repository_get_mock.assert_called_once_with(credentials.email, session_fixture)
