from fastapi import APIRouter
from app.internals.user.schema import UserSchema, UserOutputSchema, UserLoginSchema
from app.internals.auth.services.auth_service import create_user
from app.internals.auth.services.auth_service import login as login_service

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.setup import get_session


router = APIRouter()


@router.post("/signup")
async def signup(
    user: UserSchema, session: AsyncSession = Depends(get_session)
) -> UserOutputSchema:
    return await create_user(user, session)


@router.post("/login", response_model=dict)
async def login(
    user_credentials: UserLoginSchema, session: AsyncSession = Depends(get_session)
):
    return await login_service(user_credentials, session)
