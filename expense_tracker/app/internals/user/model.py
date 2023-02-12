from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from uuid import UUID, uuid4



class UserDb(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str
    email: EmailStr
    password_hash: str
    first_name: str
    last_name: str
    date_of_birth: datetime
