from datetime import datetime, timedelta
from uuid import uuid4

from pydantic import (BaseModel, ConfigDict, EmailStr, SecretStr,
                      field_validator)


class SignUpSchema(BaseModel):
    username: str
    email: EmailStr
    password: SecretStr
    first_name: str
    last_name: str
    dob: datetime

    @field_validator("password")
    def check_password_length(cls, value):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long.")
        return value

    @field_validator("dob")
    def check_age(cls, value):
        min_age_date = datetime.now() - timedelta(days=365 * 14)

        if value > min_age_date:
            raise ValueError("You must be at least 14 years old.")
        return value

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "username",
                "email": "something@example.com",
                "password": "password",
                "first_name": "john",
                "last_name": "doe",
                "dob": "2025-04-30T20:15:43",
            }
        }
    )


class UserSchema(BaseModel):
    id: uuid4
    username: str
    email: EmailStr
    password: SecretStr
    first_name: str | None = None
    last_name: str | None = None
    dob: datetime | None = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "username",
                "email": "something@example.com",
                "password": "password",
                "first_name": "Name",
                "last_name": "Last",
                "date_of_birth": "2018-12-25 09:27:53",
            }
        }
    )


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {"email": "something@example.com", "password": "password"}
        }
    )


class UserOutputSchema(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    dob: datetime
