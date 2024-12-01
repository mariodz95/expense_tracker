from sqlalchemy.ext.asyncio import AsyncSession

from app.utils import utils
from app.models.user_model import UserDb
from app.repositories import user_repository
from app.schemas.user_schema import (UserLoginSchema, UserOutputSchema,
                                       UserSchema)


async def create(user: UserSchema, session: AsyncSession) -> UserOutputSchema:
    password_hash = utils.get_password_hash(user.password.get_secret_value())
    db_user = await user_repository.create(user, session, password_hash)

    return UserOutputSchema(**db_user.dict())


async def get(credentials: UserLoginSchema, session: AsyncSession) -> UserDb:
    return await user_repository.get(credentials.email, session)
