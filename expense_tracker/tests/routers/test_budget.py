from unittest.mock import AsyncMock

import orjson

from tests.internals.budget.budget_factory import BudgetDbFactory


def test_create(client, mocker):
    json_data = {"name": "home budget", "description": "home budget"}
    budget = BudgetDbFactory()
    budget_json = orjson.dumps(budget.dict()).decode()
    budget_json_dict = orjson.loads(budget_json)
    expected = budget_json_dict

    mocker.patch(
        "app.routers.budget.budget_service.create", AsyncMock(return_value=budget)
    )

    actual = client.post("/budget/create", json=json_data)

    assert actual.status_code == 200
    assert actual.json() == expected
