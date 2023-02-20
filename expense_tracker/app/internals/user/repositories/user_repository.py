from app.internals.user.schema import UserSchema
from sqlalchemy.ext.asyncio import AsyncSession
from app.internals.user.model import UserDb


async def create_and_login(user: UserSchema, session: AsyncSession):
    db_user = UserDb(password_hash="hash", **user.dict())
    try:
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
    except Exception as e:
        print("Error", e)

    return user
