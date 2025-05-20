import logging

from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import ExpenseDb, UserDb
from app.logger_config import setup_logger
from app.schemas.expense_schema import ExpenseSchema

logger = setup_logger(level=logging.INFO)


async def create(
    expense: ExpenseSchema, user: UserDb, session: AsyncSession
) -> ExpenseDb:
    try:
        expense_db = ExpenseDb(
            **expense.model_dump(),
            user_id=user.id,
            owner=user.id,
            created_by=str(user.id),
        )
        session.add(expense_db)
        await session.commit()
        await session.refresh(expense_db)

        return expense_db
    except Exception as e:
        logger.error(f"Error while inserting expense into db: {e}")
        raise HTTPException(500, detail="Check your request and try again.")
