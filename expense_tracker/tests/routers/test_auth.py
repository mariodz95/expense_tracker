from unittest.mock import AsyncMock

import orjson

from tests.internals.user.user_factory import UserSchemaFactory
from pydantic import SecretStr


def test_signup(client, mocker, session_fixture):
    user = UserSchemaFactory()
    user.password = "password"
    user_json = orjson.dumps(user.dict()).decode()
    user_json_dict = orjson.loads(user_json)
    expected = user_json_dict

    auth_service_mock = mocker.patch(
        "app.routers.auth.auth_service.create_user", AsyncMock(return_value=user)
    )

    actual = client.post("/auth/signup", json=user_json_dict)
    user_json_dict.pop("password", None)
    user.password = SecretStr("password")

    assert actual.status_code == 200
    assert actual.json() == expected


def test_login(client, mocker):
    user = UserSchemaFactory()
    user.password = "password"
    user_json = orjson.dumps(user.dict()).decode()
    user_json_dict = orjson.loads(user_json)
    user_credentials = {"email": "test@email.com", "password": "testpassword"}
    auth_service_response = {
        "access_token": "access_token",
        "refresh_token": "refresh_token",
        "user": user,
    }
    expected = {"user": user_json_dict}

    mocker.patch(
        "app.routers.auth.auth_service.login",
        AsyncMock(return_value=auth_service_response),
    )

    actual = client.post("/auth/login", json=user_credentials)

    assert actual.status_code == 200
    assert actual.headers["x-refresh-token"] == "refresh_token"
    assert actual.cookies["expense_jwt_token"] == "access_token"
    assert actual.json() == expected
