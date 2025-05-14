from fastapi import Cookie

from app.utils.auth_utils import decode_token


async def authorize_request(
    expense_jwt_token: str | None = Cookie(default=None),
):
    return decode_token(token=expense_jwt_token)
