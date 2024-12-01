from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_config
from app.database.setup import get_session
from app.schemas.user_schema import (UserLoginSchema, SignUpSchema,
                                     UserOutputSchema)
from app.services import auth_service

config = get_config()
router = APIRouter()


@router.post("/signup")
async def signup(
    user: SignUpSchema, session: AsyncSession = Depends(get_session)
) -> UserOutputSchema:
    return await auth_service.create_user(user=user, session=session)


@router.post("/login", response_model=dict)
async def login(
    user_credentials: UserLoginSchema,
    response: Response,
    session: AsyncSession = Depends(get_session),
):
    auth_response = await auth_service.login(user_credentials, session)
    response.set_cookie(
        key=config.jwt_token_access_name,
        value=auth_response["access_token"],
    )
    response.headers[config.jwt_token_refresh_name] = auth_response["refresh_token"]

    return {"user": auth_response["user"]}
