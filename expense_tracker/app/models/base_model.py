from datetime import datetime, timezone

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel

# now = datetime.utcnow()


class BaseModelDb(SQLModel):
    date_created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )
    date_updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )
