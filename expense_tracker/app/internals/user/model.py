from pydantic import EmailStr
from datetime import datetime
from app.internals.model import BaseModelDb
from sqlmodel import Field, Column, VARCHAR, Relationship, SQLModel
from datetime import datetime
import uuid as uuid_pkg
from typing import Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from app.internals.budget.model import BudgetDb


class UserBudgetLink(SQLModel, table=True):
    user_id: Optional[uuid_pkg.UUID] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    budget_id: Optional[uuid_pkg.UUID] = Field(
        default=None, foreign_key="budget.id", primary_key=True
    )


class UserDb(BaseModelDb, table=True):
    __tablename__ = "user"

    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    username: str = Field(sa_column=Column("username", VARCHAR, unique=True))
    email: EmailStr = Field(sa_column=Column("email", VARCHAR, unique=True))
    password_hash: str = Field(nullable=False)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    date_of_birth: datetime = Field(nullable=False, default_factory=datetime.utcnow)
    budgets: list["BudgetDb"] = Relationship(
        back_populates="users", link_model=UserBudgetLink
    )


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
