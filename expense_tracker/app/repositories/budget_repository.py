import logging

from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import BudgetDb, UserDb
from app.logger_config import setup_logger
from app.schemas.budget_schema import BudgetSchema

logger = setup_logger(level=logging.INFO)


async def create(budget: BudgetSchema, user: UserDb, session: AsyncSession) -> BudgetDb:
    try:
        budget_db = BudgetDb(
            **budget.model_dump(), users=[user], owner=user.id, created_by=str(user.id)
        )
        session.add(budget_db)
        await session.commit()
        await session.refresh(budget_db)

        return budget_db
    except Exception as e:
        logger.error(f"Error while inserting budget into db: {e}")
        raise HTTPException(409, detail="There is already budget with given name.")
