from pydantic import BaseModel


class BudgetSchema(BaseModel):
    name: str
    description: str

    class Config:
        schema_extra = {
            "example": {
                "name": "home budget",
                "description": "home budget",
            }
        }
