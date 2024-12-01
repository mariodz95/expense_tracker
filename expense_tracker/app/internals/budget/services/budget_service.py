from sqlalchemy.ext.asyncio import AsyncSession

from app.internals.auth.utils import decode_token
from app.models.budget_model import BudgetDb
from app.internals.budget.repositories import budget_repository
from app.schemas.budget_schema import BudgetSchema
from app.internals.user.repositories import user_repository


async def create(budget: BudgetSchema, token: str, session: AsyncSession) -> BudgetDb:
    decoded_token = decode_token(token)
    user = await user_repository.get(decoded_token["sub"], session)

    return await budget_repository.create(budget, user, session)
