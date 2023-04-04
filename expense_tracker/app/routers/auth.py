from fastapi import APIRouter
from app.internals.user.schema import UserSchema, UserOutput
from app.internals.auth.services.auth_service import create_user
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.setup import get_session


router = APIRouter()


@router.post("/signup")
async def signup(user: UserSchema, session: AsyncSession = Depends(get_session)) -> UserOutput:
    return await create_user(user, session)


@router.get("/login", response_model=dict)
async def login():

    return {}
