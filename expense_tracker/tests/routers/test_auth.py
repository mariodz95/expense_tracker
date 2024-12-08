from unittest.mock import AsyncMock

import orjson
from pydantic import SecretStr

from app.schemas.user_schema import UserOutputSchema
from tests.factories.user_factory import UserSchemaFactory


def test_signup(client, mocker):
    user = UserSchemaFactory()
    user.password = "password"
    user_json = orjson.dumps(user.model_dump()).decode()
    user_json_dict = orjson.loads(user_json)

    mocker.patch(
        "app.routers.auth.auth_service.create_user", AsyncMock(return_value=user)
    )

    actual = client.post("/auth/signup", json=user_json_dict)
    user_json_dict.pop("password", None)
    user.password = SecretStr("password")

    assert actual.status_code == 200
    assert actual.json() == UserOutputSchema(**user_json_dict).model_dump()


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
