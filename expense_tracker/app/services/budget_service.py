from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import BudgetDb
from app.repositories import budget_repository, user_repository
from app.schemas.budget_schema import BudgetSchema


async def create(budget: BudgetSchema, token: str, session: AsyncSession) -> BudgetDb:
    user = await user_repository.get_by_id(id=token["sub"], session=session)
    created_budget = await budget_repository.create(
        budget=budget, user=user, session=session
    )

    return BudgetSchema(**created_budget.model_dump())
