from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ExpenseSchema(BaseModel):
    amount: float
    description: str
    budget_id: UUID
    expense_category_id: UUID

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "amount": "100",
                "description": "Fuel expenses",
                "budget_id": "2b96f851-fbfb-4e30-becc-64b0c5b22742",
                "expense_category_id": "2b96f851-fbfb-4e30-becc-64b0c5b22742",
            }
        }
    )
