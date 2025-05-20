from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_config
from app.database.setup import get_session
from app.dependencies import authorize_request
from app.schemas.expense_schema import ExpenseSchema
from app.services import expense_service

config = get_config()

router = APIRouter()


@router.post("/create")
async def create(
    expense: ExpenseSchema,
    session: AsyncSession = Depends(get_session),
    token=Depends(authorize_request),
) -> ExpenseSchema:
    return await expense_service.create(expense, token, session)
