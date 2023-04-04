from fastapi import APIRouter
from app.internals.user.schema import UserSchema
from app.internals.auth.services.auth_service import create_and_login
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.setup import get_session


router = APIRouter()


@router.post("/signup")
async def signup(user: UserSchema, session: AsyncSession = Depends(get_session)):
    await create_and_login(user, session)

    return {}


@router.get("/login", response_model=dict)
async def login():

    return {}
