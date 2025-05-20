import uuid as uuid_pkg
from datetime import datetime, timezone
from typing import Optional

from pydantic import ConfigDict, EmailStr
from sqlalchemy import UniqueConstraint
from sqlmodel import VARCHAR, Column, Field, Relationship, SQLModel

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
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    dob: datetime = Field(nullable=False)
    budgets: list["BudgetDb"] = Relationship(
        back_populates="users", link_model=UserBudgetLink
    )
    expenses: list["ExpenseDb"] = Relationship(back_populates="user")


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
    expenses: list["ExpenseDb"] = Relationship(back_populates="budget")


class ExpenseCategoryDb(BaseModelDb, table=True):
    __tablename__ = "expense_category"

    id: uuid_pkg.UUID = Field(default=None, primary_key=True)
    name: str

    expenses: list["ExpenseDb"] = Relationship(back_populates="category")


class ExpenseDb(BaseModelDb, table=True):
    __tablename__ = "expense"

    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    amount: float
    description: str
    user_id: uuid_pkg.UUID = Field(foreign_key="users.id")
    budget_id: uuid_pkg.UUID = Field(foreign_key="budget.id")
    expense_category_id: uuid_pkg.UUID = Field(foreign_key="expense_category.id")

    user: "UserDb" = Relationship(back_populates="expenses")
    budget: "BudgetDb" = Relationship(back_populates="expenses")
    category: "ExpenseCategoryDb" = Relationship(back_populates="expenses")
