from app.internals.user.schema import UserOutputSchema, UserSchema, UserLoginSchema
from app.internals.user.services import user_service
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(user: UserSchema, session: AsyncSession) -> UserOutputSchema:
    return await user_service.create(user, session)


async def login(user_credentials: UserLoginSchema, session: AsyncSession):
    user = await user_service.get(user_credentials, session)

    return user
