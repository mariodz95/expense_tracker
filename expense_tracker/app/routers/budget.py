from fastapi import APIRouter, Cookie, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_config
from app.database.setup import get_session
from app.models.budget_model import BudgetDb
from app.schemas.budget_schema import BudgetSchema
from app.services import budget_service

config = get_config()

router = APIRouter()


@router.post("/create")
async def create(
    budget: BudgetSchema,
    expense_jwt_token: str | None = Cookie(default=None),
    session: AsyncSession = Depends(get_session),
) -> BudgetDb:
    return await budget_service.create(budget, expense_jwt_token, session)
