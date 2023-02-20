from app.internals.user.schema import UserSchema
from app.internals.user.repositories import user_repository
from sqlalchemy.ext.asyncio import AsyncSession


async def create_and_login(user: UserSchema, session: AsyncSession):
    await user_repository.create_and_login(user, session)


async def hash_password(password: str):
    return
