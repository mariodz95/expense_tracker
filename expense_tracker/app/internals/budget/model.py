from app.internals.model import BaseModelDb
from sqlmodel import Field, Relationship
from app.internals.user.model import UserDb
import uuid as uuid_pkg
from typing import TYPE_CHECKING
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
    name: str
    description: str
    users: list["UserDb"] = Relationship(
        back_populates="budgets", link_model=UserBudgetLink
    )
