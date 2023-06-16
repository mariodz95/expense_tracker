from unittest.mock import Mock

import pytest
from fastapi.exceptions import HTTPException

from app.internals.auth import utils
from tests.internals.user.user_factory import UserSchemaFactory


def test_verify_password():
    password = "password"
    password_hash = "$2b$12$qSRM/dGGXgLVF11f//KDBejTHlRTkbj1v/GfHjJhKRErEWU2OBIBm"

    result = utils.verify_password(password, password_hash)

    assert result == True


def test_get_password_hash(mocker):
    password = "password"
    password_hash = "$2b$12$qSRM/dGGXgLVF11f//KDBejTHlRTkbj1v/GfHjJhKRErEWU2OBIBm"
    mocker.patch(
        "app.internals.auth.utils.pwd_context.hash",
        Mock(return_value=password_hash),
    )

    result = utils.get_password_hash(password)

    assert result == password_hash


def test_generate_token(mocker):
    user = UserSchemaFactory()
    token = "token"
    mocker.patch(
        "app.internals.auth.utils.jwt_encode",
        Mock(return_value=token),
    )

    result = utils.generate_token(user, "ACCESS_TOKEN")

    assert result == token


def test_generate_token(mocker):
    user = UserSchemaFactory()
    token = "token"
    mocker.patch(
        "app.internals.auth.utils.jwt_encode",
        Mock(return_value=token),
    )

    result = utils.generate_token(user, "ACCESS_TOKEN")

    assert result == token



def test_decode_token(mocker):
    token = "token"
    mocker.patch(
        "app.internals.auth.utils.jwt_decode",
        Mock(return_value=token),
    )

    result = utils.decode_token(token)

    assert result == token


def test_decode_token_catch_exception(mocker):
    token = "token"

    with pytest.raises(HTTPException):
        utils.decode_token(token)

