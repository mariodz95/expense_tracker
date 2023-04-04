from app.internals.user.schema import UserOutput, UserSchema
from app.internals.user.services import user_service
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(user: UserSchema, session: AsyncSession) -> UserOutput:
    return await user_service.create_user(user, session)


async def hash_password(password: str):
    return
