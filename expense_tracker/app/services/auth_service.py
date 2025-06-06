from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.enums import JwtTokenClaim
from app.repositories import user_repository
from app.schemas.user_schema import (SignUpSchema, UserLoginSchema,
                                     UserOutputSchema)
from app.services import user_service
from app.utils.auth_utils import generate_token, verify_password


async def create_user(user: SignUpSchema, session: AsyncSession) -> UserOutputSchema:
    return await user_service.create(user=user, session=session)


async def login(user_credentials: UserLoginSchema, session: AsyncSession) -> dict:
    user = await user_repository.get(user_credentials.email, session)

    if not verify_password(user_credentials.password, user.password_hash):
        raise HTTPException(401, detail="Invalid email or password.")

    access_token = generate_token(user, JwtTokenClaim.ACCESS_TOKEN)
    refresh_token = generate_token(user, JwtTokenClaim.REFRESH_TOKEN)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": user,
    }


async def authenticate():
    return


async def logout():
    return
