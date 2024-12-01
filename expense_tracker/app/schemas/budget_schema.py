from pydantic import BaseModel


class BudgetSchema(BaseModel):
    name: str
    description: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "home budget",
                "description": "home budget",
            }
        }
