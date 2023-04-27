from passlib.context import CryptContext
from app.internals.user.schema import UserSchema
from jwt import encode as jwt_encode
from app.config import get_config

config = get_config()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def generate_token(user: UserSchema, claim: str):
    payload = {
        "sub": user.email,
        "claim": claim,
        "exp": config.jwt_expiration,
    }
    return jwt_encode(payload, config.jwt_secret, algorithm=config.jwt_algorithm)


def decode_token():
    return
