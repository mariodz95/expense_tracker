from unittest.mock import AsyncMock


async def test_create(auth_client, mocker):
    json_data = {"name": "home budget", "description": "home budget"}
    expected = {"name": "home budget", "description": "home budget"}

    mocker.patch(
        "app.routers.budget.budget_service.create", AsyncMock(return_value=expected)
    )

    actual = auth_client.post("/budget/create", json=json_data)

    assert actual.status_code == 200
    assert actual.json() == expected


async def test_create_without_token_unauthorized(client, mocker):
    json_data = {"name": "home budget", "description": "home budget"}
    expected = {"detail": "Unauthorized request."}

    mocker.patch(
        "app.routers.budget.budget_service.create", AsyncMock(return_value=expected)
    )

    actual = client.post("/budget/create", json=json_data)

    assert actual.status_code == 401
    assert actual.json() == expected
