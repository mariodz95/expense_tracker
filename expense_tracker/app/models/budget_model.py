import uuid as uuid_pkg
from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship

from app.models.base_model import BaseModelDb
from app.models.user_model import UserBudgetLink, UserDb

if TYPE_CHECKING:
    from app.models.user_model import UserDb


class BudgetDb(BaseModelDb, table=True):
    __tablename__ = "budget"
    __table_args__ = (UniqueConstraint("owner", "name", name="uq_owner_budget_name"),)

    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str
    owner: uuid_pkg.UUID = Field(foreign_key="users.id", nullable=False, index=True)
    description: str
    users: list["UserDb"] = Relationship(
        back_populates="budgets", link_model=UserBudgetLink
    )
