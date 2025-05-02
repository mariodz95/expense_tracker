from datetime import datetime, timedelta, timezone

import jwt
from fastapi.exceptions import HTTPException
from jwt import InvalidTokenError
from passlib.context import CryptContext

from app.config import get_config
from app.enums import JwtTokenClaim
from app.schemas.user_schema import UserSchema

config = get_config()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    return pwd_context.hash(password)


def generate_token(user: UserSchema, claim: str):
    payload = {
        "sub": str(user.id),
        "claim": claim,
        "exp": token_expire_at(claim=claim),
    }

    return jwt.encode(payload, config.jwt_secret, algorithm=config.jwt_algorithm)


def token_expire_at(claim: str) -> datetime:
    jwt_expiration = config.jwt_access_expiration

    if claim == JwtTokenClaim.REFRESH_TOKEN:
        jwt_expiration = config.jwt_refresh_expiration

    return datetime.now(timezone.utc) + timedelta(minutes=jwt_expiration)


def decode_token(token: str):
    try:
        return jwt.decode(
            jwt=token, key=config.jwt_secret, algorithms=config.jwt_algorithm
        )
    except InvalidTokenError as e:
        raise HTTPException(401, detail=f"Invalid token. {e}.")
