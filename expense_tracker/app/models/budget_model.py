import uuid as uuid_pkg
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.models.base_model import BaseModelDb
from app.models.user_model import UserBudgetLink, UserDb

if TYPE_CHECKING:
    from app.models.user_model import UserDb


class BudgetDb(BaseModelDb, table=True):
    __tablename__ = "budget"

    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str
    description: str
    users: list["UserDb"] = Relationship(
        back_populates="budgets", link_model=UserBudgetLink
    )
