from datetime import datetime

from sqlmodel import Field, SQLModel

now = datetime.utcnow()


class BaseModelDb(SQLModel):
    date_created_at: datetime = Field(default_factory=lambda: datetime.utcnow())
    date_updated_at: datetime = Field(default_factory=lambda: datetime.utcnow())

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
