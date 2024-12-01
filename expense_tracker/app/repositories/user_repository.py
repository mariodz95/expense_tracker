import logging

from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.models.user_model import UserDb
from app.schemas.user_schema import UserSchema

logger = logging.getLogger(__name__)


async def create(user: UserSchema, session: AsyncSession, password_hash: str) -> UserDb:
    db_user = UserDb(password_hash=password_hash, **user.dict())
    try:
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)

        return db_user
    except IntegrityError as e:
        await session.rollback()
        logger.error(e)
        raise HTTPException(500, detail="Email is already used.")
    except Exception as e:
        logger.error(e)
        raise HTTPException(500, detail="Something is wrong.")


async def get(email: str, session: AsyncSession) -> UserDb:
    statement = select(UserDb).where(UserDb.email == email)
    result = await session.execute(statement)
    user = result.scalar()
    if not user:
        raise HTTPException(404, detail="Invalid email or password")

    return user
