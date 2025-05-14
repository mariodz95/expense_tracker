from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_config
from app.database.setup import get_session
from app.dependencies import authorize_request
from app.schemas.budget_schema import BudgetSchema
from app.services import budget_service

config = get_config()

router = APIRouter()


@router.post("/create")
async def create(
    budget: BudgetSchema,
    session: AsyncSession = Depends(get_session),
    token=Depends(authorize_request),
) -> BudgetSchema:
    return await budget_service.create(budget, token, session)
