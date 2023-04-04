from app.internals.user.schema import UserOutput, UserSchema
from app.internals.user.repositories import user_repository
from app.internals.auth import utils
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(user: UserSchema, session: AsyncSession) -> UserOutput:
    password_hash = utils.get_password_hash(user.password.get_secret_value())
    
    db_user = await user_repository.create(user, session, password_hash)
    return UserOutput(**db_user.dict())
