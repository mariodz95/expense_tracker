from pydantic import EmailStr
from datetime import datetime
from app.internals.model import BaseModelDb
from sqlmodel import Field
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
    username: str
    email: EmailStr
    password_hash: str
    first_name: str
    last_name: str
    date_of_birth: datetime = Field(default_factory=lambda: datetime.utcnow())
