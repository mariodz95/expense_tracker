from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from fastapi.exceptions import HTTPException
from jwt import InvalidTokenError

from app.config import get_config
from app.enums import JwtTokenClaim
from app.schemas.user_schema import UserSchema

config = get_config()


def get_password_hash(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


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
    except InvalidTokenError:
        raise HTTPException(401, detail="Unauthorized request.")
