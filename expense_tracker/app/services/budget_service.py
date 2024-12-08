from sqlalchemy.ext.asyncio import AsyncSession

from app.models.budget_model import BudgetDb
from app.repositories import budget_repository, user_repository
from app.schemas.budget_schema import BudgetSchema
from app.utils.auth_utils import decode_token


async def create(budget: BudgetSchema, token: str, session: AsyncSession) -> BudgetDb:
    decoded_token = decode_token(token=token)
    user = await user_repository.get(email=decoded_token["sub"], session=session)
    created_budget = await budget_repository.create(
        budget=budget, user=user, session=session
    )

    return BudgetSchema(**created_budget.model_dump())
