from datetime import datetime

from pydantic import BaseModel, EmailStr, SecretStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: SecretStr
    first_name: str
    last_name: str
    date_of_birth: datetime

    class Config:
        schema_extra = {
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
        schema_extra = {
            "example": {"email": "something@example.com", "password": "password"}
        }


class UserOutputSchema(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    date_of_birth: datetime
