from app.internals.user.schema import UserSchema, UserLoginSchema
from sqlalchemy.ext.asyncio import AsyncSession
from app.internals.user.model import UserDb
from fastapi.exceptions import HTTPException
from sqlmodel import select
import logging


logger = logging.getLogger(__name__)  


async def create(user: UserSchema, session: AsyncSession, password_hash: str) -> UserDb:
    db_user = UserDb(password_hash=password_hash, **user.dict())
    try:
        session.add(db_user)
        await session.commit()
    except Exception as e:
        logger.error(e)
        raise HTTPException(500, detail="Something is wrong.")

    return db_user


async def get(credentials: UserLoginSchema, session: AsyncSession) -> UserDb:
    statement = select(UserDb).where(UserDb.email == credentials.email)
    result = await session.execute(statement)
    user = result.scalar()
    if not user:
        raise HTTPException(404, detail="User doesn't exits.")

    return user
