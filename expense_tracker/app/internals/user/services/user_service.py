from app.internals.user.schema import UserOutputSchema, UserSchema, UserLoginSchema
from app.internals.user.model import UserDb
from app.internals.user.repositories import user_repository
from app.internals.auth import utils
from sqlalchemy.ext.asyncio import AsyncSession


async def create(user: UserSchema, session: AsyncSession) -> UserOutputSchema:
    password_hash = utils.get_password_hash(user.password.get_secret_value())
    db_user = await user_repository.create(user, session, password_hash)

    return UserOutputSchema(**db_user.dict())


async def get(credentials: UserLoginSchema, session: AsyncSession) -> UserDb:
    user = await user_repository.get(credentials, session)

    return user
