from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import user_repository
from app.schemas.user_schema import (SignUpSchema, UserLoginSchema,
                                     UserOutputSchema)
from app.utils import auth_utils


async def create(user: SignUpSchema, session: AsyncSession) -> UserOutputSchema:
    password_hash = auth_utils.get_password_hash(user.password.get_secret_value())
    db_user = await user_repository.create(user, session, password_hash)

    return UserOutputSchema(**db_user.model_dump())


async def get(credentials: UserLoginSchema, session: AsyncSession) -> UserOutputSchema:
    db_user = await user_repository.get(credentials.email, session)
    return UserOutputSchema(**db_user.model_dump())
