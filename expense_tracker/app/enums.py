from enum import Enum


class JwtTokenClaim(str, Enum):
    ACCESS_TOKEN = "ACCESS_TOKEN"
    REFRESH_TOKEN = "REFRESH_TOKEN"
