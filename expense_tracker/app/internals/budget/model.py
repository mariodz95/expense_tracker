from pydantic import EmailStr
from datetime import datetime
from app.internals.model import BaseModelDb
from sqlmodel import Field, Column, VARCHAR, SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional
from app.internals.user.model import UserDb
import uuid as uuid_pkg
from typing import TYPE_CHECKING, List, Optional
from app.internals.user.model import UserBudgetLink


if TYPE_CHECKING:
    from app.internals.user.model import UserDb


class BudgetDb(BaseModelDb, table=True):
    __tablename__ = "budget"

    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    users: list["UserDb"] = Relationship(
        back_populates="budgets", link_model=UserBudgetLink
    )
