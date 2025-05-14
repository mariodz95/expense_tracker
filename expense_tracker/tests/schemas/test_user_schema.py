from datetime import datetime

import pytest
from pydantic import SecretStr, ValidationError

from app.schemas.user_schema import SignUpSchema
from tests.factories.user_factory import UserSchemaFactory


def test_signup_schema_underage():
    expected = "You must be at least 14 years old."

    invalid_data = UserSchemaFactory.build(
        dob=datetime(2012, 4, 15, 12, 0, 0), password=SecretStr("valid_password")
    )

    with pytest.raises(ValidationError) as exc:
        SignUpSchema(**invalid_data.model_dump())

    assert expected in str(exc.value)


def test_signup_schema_invalid_password():
    expected = "Password must be at least 6 characters long."
    invalid_data = UserSchemaFactory.build(password=SecretStr("short"))

    with pytest.raises(ValidationError) as exc:
        SignUpSchema(**invalid_data.model_dump())

    assert expected in str(exc.value)
