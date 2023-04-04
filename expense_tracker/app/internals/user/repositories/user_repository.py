from app.internals.user.schema import UserSchema, UserOutput
from sqlalchemy.ext.asyncio import AsyncSession
from app.internals.user.model import UserDb
from fastapi.exceptions import HTTPException
import logging


logger = logging.getLogger(__name__)  


async def create(user: UserSchema, session: AsyncSession, password_hash: str) -> UserOutput:
    db_user = UserDb(password_hash=password_hash, **user.dict())
    try:
        session.add(db_user)
        await session.commit()
    except Exception as e:
        logger.error(e)
        raise HTTPException(500, detail="Something is wrong.")

    return db_user
