from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.internals.auth.utils import generate_token, verify_password
from app.internals.user.schema import (UserLoginSchema, UserOutputSchema,
                                       UserSchema)
from app.internals.user.services import user_service


async def create_user(user: UserSchema, session: AsyncSession) -> UserOutputSchema:
    return await user_service.create(user, session)


async def login(user_credentials: UserLoginSchema, session: AsyncSession):
    user = await user_service.get(user_credentials, session)

    if not verify_password(user_credentials.password, user.password_hash):
        raise HTTPException(401, detail="Invalid email or password.")

    access_token = generate_token(user, "ACCESS_TOKEN")
    refresh_token = generate_token(user, "REFRESH_TOKEN")

    return {"access_token": access_token, "refresh_token": refresh_token, "user": user}


async def authenticate():
    return


async def logout():
    return
