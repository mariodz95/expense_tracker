from datetime import datetime

from sqlmodel import Field, SQLModel

now = datetime.utcnow()


class BaseModelDb(SQLModel):
    date_created_at: datetime = Field(default_factory=lambda: datetime.utcnow())
    date_updated_at: datetime = Field(default_factory=lambda: datetime.utcnow())

    class Config:
        from_attributes = True
        populate_by_name = True
