from pydantic import EmailStr
from datetime import datetime
from app.internals.model import BaseModelDb
from sqlmodel import Field, Column, VARCHAR
from datetime import datetime

import uuid as uuid_pkg


class UserDb(BaseModelDb, table=True):
    __tablename__ = "user"

    uuid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    username: str = Field(sa_column=Column("username", VARCHAR, unique=True))
    email: EmailStr = Field(sa_column=Column("email", VARCHAR, unique=True))
    password_hash: str = Field(nullable=False)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    date_of_birth: datetime = Field(nullable=False, default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
