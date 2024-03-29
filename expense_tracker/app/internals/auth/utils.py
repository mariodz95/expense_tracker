from datetime import datetime, timedelta

from fastapi.exceptions import HTTPException
from jwt import InvalidTokenError, decode as jwt_decode, encode as jwt_encode
from passlib.context import CryptContext

from app.config import get_config
from app.internals.user.schema import UserSchema

config = get_config()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def generate_token(user: UserSchema, claim: str):
    expire_at = datetime.utcnow() + timedelta(minutes=config.jwt_expiration)
    payload = {
        "sub": user.email,
        "claim": claim,
        "exp": expire_at,
    }

    return jwt_encode(payload, config.jwt_secret, algorithm=config.jwt_algorithm)


def decode_token(token: str):
    try:
        return jwt_decode(
            jwt=token, key=config.jwt_secret, algorithms=config.jwt_algorithm
        )
    except InvalidTokenError as e:
        raise HTTPException(401, detail=f"Invalid token. {e}.")
