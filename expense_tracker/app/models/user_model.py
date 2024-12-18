import uuid as uuid_pkg
from typing import TYPE_CHECKING, Optional

from pydantic import EmailStr
from sqlmodel import VARCHAR, Column, Field, Relationship, SQLModel

from app.models.base_model import BaseModelDb

if TYPE_CHECKING:
    from app.models.budget_model import BudgetDb


class UserBudgetLink(SQLModel, table=True):
    user_id: Optional[uuid_pkg.UUID] = Field(
        default=None, foreign_key="users.id", primary_key=True
    )
    budget_id: Optional[uuid_pkg.UUID] = Field(
        default=None, foreign_key="budget.id", primary_key=True
    )


class UserDb(BaseModelDb, table=True):
    __tablename__ = "users"

    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    username: str = Field(sa_column=Column("username", VARCHAR, unique=True))
    email: EmailStr = Field(sa_column=Column("email", VARCHAR, unique=True))
    password_hash: str = Field(nullable=False)
    budgets: list["BudgetDb"] = Relationship(
        back_populates="users", link_model=UserBudgetLink
    )
