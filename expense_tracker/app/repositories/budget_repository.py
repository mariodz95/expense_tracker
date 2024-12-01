from sqlalchemy.ext.asyncio import AsyncSession

from app.models.budget_model import BudgetDb
from app.models.user_model import UserDb
from app.schemas.budget_schema import BudgetSchema


async def create(budget: BudgetSchema, user: UserDb, session: AsyncSession) -> BudgetDb:
    budget_db = BudgetDb(**budget.dict(), users=[user])
    session.add(budget_db)
    await session.commit()
    await session.refresh(budget_db)

    return budget_db
