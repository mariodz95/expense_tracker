from unittest.mock import AsyncMock

import orjson
from pydantic import SecretStr

from tests.factories.user_factory import UserSchemaFactory


def test_signup_returns_200(client, mocker, sign_up_payload):
    mocker.patch(
        "app.routers.auth.auth_service.create_user",
        AsyncMock(return_value=sign_up_payload),
    )

    actual = client.post("/auth/signup", json=sign_up_payload)

    assert actual.status_code == 200


def test_signup_returns_expected_json(client, mocker, sign_up_payload):
    expected: dict = sign_up_payload

    mocker.patch(
        "app.routers.auth.auth_service.create_user",
        AsyncMock(return_value=sign_up_payload),
    )

    actual = client.post("/auth/signup", json=sign_up_payload)
    expected.pop("password", None)

    assert actual.json() == expected


def test_login(client, mocker):
    user = UserSchemaFactory()
    user.password = SecretStr("password")

    user_dict = user.model_dump()
    user_dict["password"] = user.password.get_secret_value()
    user_json = orjson.dumps(user_dict).decode()
    user_json_dict = orjson.loads(user_json)

    user_credentials = {
        "email": user_dict["email"],
        "password": user.password.get_secret_value(),
    }
    auth_service_response = {
        "access_token": "access_token",
        "refresh_token": "refresh_token",
        "user": user_dict,
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
