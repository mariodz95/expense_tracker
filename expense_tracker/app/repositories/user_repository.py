import logging

from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.database.models import UserDb
from app.logger_config import setup_logger
from app.schemas.user_schema import SignUpSchema

logger = setup_logger(level=logging.INFO)


async def create(
    user: SignUpSchema, session: AsyncSession, password_hash: str
) -> UserDb:
    db_user = UserDb(
        password_hash=password_hash, **user.model_dump(), created_by="SYSTEM"
    )
    try:
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)

        return db_user
    except IntegrityError as e:
        await session.rollback()
        logger.error(f"Create user failed {e}.")
        raise HTTPException(409, detail="Email or username is already used.")
    except Exception as e:
        await session.rollback()
        logger.error(f"Create user failed {e}.")
        raise HTTPException(409, detail="User signup failed.")


async def get(email: str, session: AsyncSession) -> UserDb:
    statement = select(UserDb).where(UserDb.email == email)
    result = await session.execute(statement)
    user = result.scalar()
    if not user:
        raise HTTPException(404, detail="Invalid email or password.")

    return user


async def get_by_id(id: str, session: AsyncSession) -> UserDb:
    user = await session.get(UserDb, id)
    if not user:
        raise HTTPException(404, detail="Invalid user id.")

    return user
