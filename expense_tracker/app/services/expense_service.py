from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import BudgetDb
from app.repositories import (budget_repository, expense_repository,
                              user_repository)
from app.schemas.expense_schema import ExpenseSchema


async def create(expense: ExpenseSchema, token: str, session: AsyncSession) -> BudgetDb:
    user = await user_repository.get_by_id(id=token["sub"], session=session)
    budget = await budget_repository.get(
        user_id=token["sub"], budget_id=expense.budget_id, session=session
    )
    if not budget:
        raise HTTPException(409, detail="Check your request and try again.")
    created_expense = await expense_repository.create(
        expense=expense, user=user, session=session
    )

    return ExpenseSchema(**created_expense.model_dump())
