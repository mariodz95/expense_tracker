from app.internals.user.schema import UserOutputSchema, UserSchema, UserLoginSchema
from app.internals.user.services import user_service
from sqlalchemy.ext.asyncio import AsyncSession
from app.internals.auth.utils import verify_password, generate_token
from fastapi.exceptions import HTTPException


async def create_user(user: UserSchema, session: AsyncSession) -> UserOutputSchema:
    return await user_service.create(user, session)


async def login(user_credentials: UserLoginSchema, session: AsyncSession):
    user = await user_service.get(user_credentials, session)

    if not verify_password(user_credentials.password, user.password_hash):
        raise HTTPException(401, detail="Invalid email or password.")

    access_token = generate_token(user, "ACCESS_TOKEN")
    refresh_token = generate_token(user, "REFRESH_TOKEN")

    return {"access_token": access_token, "refresh_token": refresh_token}


async def authenticate():
    return


async def logout():
    return
