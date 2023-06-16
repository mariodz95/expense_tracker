from unittest.mock import AsyncMock, Mock

import pytest

from app.internals.user.schema import UserLoginSchema, UserOutputSchema
from app.internals.user.services import user_service
from tests.internals.user.user_factory import UserDbFactory, UserSchemaFactory


@pytest.mark.asyncio
async def test_create(mocker, session):
    user = UserSchemaFactory()
    db_user = UserDbFactory()
    expected = UserOutputSchema(**db_user.dict())

    utils_get_password_hash_mock = mocker.patch(
        "app.internals.user.services.user_service.utils.get_password_hash",
        Mock(return_value="password_hash"),
    )
    user_repository_create_mock = mocker.patch(
        "app.internals.user.services.user_service.user_repository.create",
        AsyncMock(return_value=db_user),
    )
    response = await user_service.create(user, session)

    assert response == expected
    utils_get_password_hash_mock.assert_called_once_with(
        user.password.get_secret_value()
    )
    user_repository_create_mock.assert_called_once_with(user, session, "password_hash")


@pytest.mark.asyncio
async def test_get(mocker, session):
    credentials = UserLoginSchema(email="test@email.com", password="password")
    user = UserDbFactory()
    expected = user
    user_repository_get_mock = mocker.patch(
        "app.internals.user.services.user_service.user_repository.get",
        AsyncMock(return_value=user),
    )

    response = await user_service.get(credentials, session)

    assert response == expected
    user_repository_get_mock.assert_called_once_with(credentials.email, session)
