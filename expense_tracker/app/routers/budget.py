from fastapi import APIRouter, Response, Cookie
from app.internals.user.schema import UserSchema, UserOutputSchema, UserLoginSchema
from app.internals.auth.services.auth_service import create_user
from app.internals.auth.services.auth_service import login as login_service

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.setup import get_session
from app.config import get_config
from app.internals.budget.schema import BudgetSchema
from app.internals.budget.services import budget_service
from app.internals.budget.model import BudgetDb

config = get_config()

router = APIRouter()


@router.post("/create")
async def create(
    budget: BudgetSchema,
    expense_jwt_token: str | None = Cookie(default=None),
    session: AsyncSession = Depends(get_session),
) -> BudgetDb:
    return await budget_service.create(budget, expense_jwt_token, session)
