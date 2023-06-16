from sqlalchemy.ext.asyncio import AsyncSession

from app.internals.budget.model import BudgetDb
from app.internals.budget.schema import BudgetSchema
from app.internals.user.model import UserDb


async def create(budget: BudgetSchema, user: UserDb, session: AsyncSession) -> BudgetDb:
    budget_db = BudgetDb(**budget.dict(), users=[user])
    session.add(budget_db)
    await session.commit()
    session.refresh(budget_db)

    return budget_db
