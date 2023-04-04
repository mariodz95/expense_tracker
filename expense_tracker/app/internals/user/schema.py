from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
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
                "date_of_birth": "date_of_birth"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "something@example.com",
                "password": "password"
            }
        }


class UserOutput(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    date_of_birth: datetime
