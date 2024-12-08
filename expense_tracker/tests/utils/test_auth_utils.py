from unittest.mock import Mock

import pytest
from fastapi.exceptions import HTTPException

from app.utils import auth_utils
from tests.factories.user_factory import UserSchemaFactory


def test_verify_password():
    password = "password"
    password_hash = "$2b$12$qSRM/dGGXgLVF11f//KDBejTHlRTkbj1v/GfHjJhKRErEWU2OBIBm"

    result = auth_utils.verify_password(password, password_hash)

    assert result == True


def test_get_password_hash(mocker):
    password = "password"
    password_hash = "$2b$12$qSRM/dGGXgLVF11f//KDBejTHlRTkbj1v/GfHjJhKRErEWU2OBIBm"
    mocker.patch(
        "app.utils.auth_utils.pwd_context.hash",
        Mock(return_value=password_hash),
    )

    result = auth_utils.get_password_hash(password)

    assert result == password_hash


def test_generate_token(mocker):
    user = UserSchemaFactory()
    token = "token"
    mocker.patch(
        "app.utils.auth_utils.jwt.encode",
        Mock(return_value=token),
    )

    result = auth_utils.generate_token(user, "ACCESS_TOKEN")

    assert result == token


def test_decode_token(mocker):
    token = "token"
    mocker.patch(
        "app.utils.auth_utils.jwt.decode",
        Mock(return_value=token),
    )

    result = auth_utils.decode_token(token)

    assert result == token


def test_decode_token_catch_exception():
    token = "token"

    with pytest.raises(HTTPException):
        auth_utils.decode_token(token)
