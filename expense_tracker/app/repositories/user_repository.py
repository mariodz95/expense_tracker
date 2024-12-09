import logging
from logging.config import dictConfig

from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.logger_config import LogConfig
from app.models.user_model import UserDb
from app.schemas.user_schema import SignUpSchema

dictConfig(LogConfig().model_dump())
logger = logging.getLogger("expense_tracker")


async def create(
    user: SignUpSchema, session: AsyncSession, password_hash: str
) -> UserDb:
    db_user = UserDb(password_hash=password_hash, **user.model_dump())
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
        raise HTTPException(409, detail="Create user failed.")


async def get(email: str, session: AsyncSession) -> UserDb:
    statement = select(UserDb).where(UserDb.email == email)
    result = await session.execute(statement)
    user = result.scalar()
    if not user:
        raise HTTPException(404, detail="Invalid email or password.")

    return user
