from datetime import datetime

from pydantic import BaseModel, EmailStr, SecretStr


class SignUpSchema(BaseModel):
    username: str
    email: EmailStr
    password: SecretStr
    class Config:
        json_schema_extra = {
            "example": {
                "username": "username",
                "email": "something@example.com",
                "password": "password",
            }
        }


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: SecretStr
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: datetime | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "username": "username",
                "email": "something@example.com",
                "password": "password",
                "first_name": "Name",
                "last_name": "Last",
                "date_of_birth": "2018-12-25 09:27:53",
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {"email": "something@example.com", "password": "password"}
        }


class UserOutputSchema(BaseModel):
    username: str
    email: EmailStr

