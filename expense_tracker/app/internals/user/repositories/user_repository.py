from app.internals.user.schema import UserSchema, UserLoginSchema
from sqlalchemy.ext.asyncio import AsyncSession
from app.internals.user.model import UserDb
from fastapi.exceptions import HTTPException
from sqlmodel import select
import logging
from sqlalchemy.exc import IntegrityError


logger = logging.getLogger(__name__)


async def create(user: UserSchema, session: AsyncSession, password_hash: str) -> UserDb:
    db_user = UserDb(password_hash=password_hash, **user.dict())
    try:
        session.add(db_user)
        await session.commit()
    except IntegrityError as e:
        session.rollback()
        logger.error(e)
        raise HTTPException(500, detail="Email is already used.")
    except Exception as e:
        logger.error(e)
        raise HTTPException(500, detail="Something is wrong.")
    finally:
        session.close()

    return db_user


async def get(email: str, session: AsyncSession) -> UserDb:
    statement = select(UserDb).where(UserDb.email == email)
    result = await session.execute(statement)
    user = result.scalar()
    if not user:
        raise HTTPException(404, detail="Invalid email or password")

    return user
