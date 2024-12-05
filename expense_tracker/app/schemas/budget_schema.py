from pydantic import BaseModel, ConfigDict


class BudgetSchema(BaseModel):
    name: str
    description: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "home budget",
                "description": "home budget",
            }
        }
    )
