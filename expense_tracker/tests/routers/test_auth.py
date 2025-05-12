from unittest.mock import AsyncMock

import orjson
from pydantic import SecretStr

from app.schemas.user_schema import UserOutputSchema
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
    user = UserSchemaFactory.build()
    user.password = SecretStr("password")
    output_schema = UserOutputSchema(**user.model_dump())
    expected_json = orjson.dumps(output_schema.model_dump()).decode()
    expected_normalized = orjson.loads(expected_json)

    user_credentials = {
        "email": user.email,
        "password": user.password.get_secret_value(),
    }
    auth_service_response = {
        "access_token": "access_token",
        "refresh_token": "refresh_token",
        "user": user,
    }

    mocker.patch(
        "app.routers.auth.auth_service.login",
        AsyncMock(return_value=auth_service_response),
    )

    actual = client.post("/auth/login", json=user_credentials)

    assert actual.status_code == 200
    assert actual.headers["x-refresh-token"] == "refresh_token"
    assert actual.cookies["expense_jwt_token"] == "access_token"
    assert actual.json() == expected_normalized
