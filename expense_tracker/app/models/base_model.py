from datetime import datetime, timezone

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel

current_datetime = datetime.now(timezone.utc).replace(tzinfo=None)


class BaseModelDb(SQLModel):
    date_created_at: datetime = Field(default_factory=lambda: current_datetime)
    date_updated_at: datetime = Field(default_factory=lambda: current_datetime)
    created_by: str = Field(nullable=False)
    updated_by: str = Field(nullable=True)
    soft_deleted: bool = Field(default=False)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )
