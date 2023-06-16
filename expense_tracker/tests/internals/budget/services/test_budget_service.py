from unittest.mock import AsyncMock, Mock

import pytest

from app.internals.budget.schema import BudgetSchema
from app.internals.budget.services import budget_service
from tests.internals.budget.budget_factory import BudgetDbFactory
from tests.internals.user.user_factory import UserDbFactory


@pytest.mark.asyncio
async def test_create(mocker, session):
    budget = BudgetSchema(name="test budget", description="test budget")
    budget_db = BudgetDbFactory()
    user = UserDbFactory()
    expected = budget_db
    token = {"sub": "user@email.com"}
    decode_token_mock = mocker.patch(
        "app.internals.budget.services.budget_service.decode_token",
        Mock(return_value=token),
    )
    user_repository_get_mock = mocker.patch(
        "app.internals.budget.services.budget_service.user_repository.get",
        AsyncMock(return_value=user),
    )
    budget_repository_create_mock = mocker.patch(
        "app.internals.budget.services.budget_service.budget_repository.create",
        AsyncMock(return_value=budget_db),
    )

    response = await budget_service.create(budget, "token", session)

    assert response == expected
    decode_token_mock.assert_called_once_with("token")
    user_repository_get_mock.assert_called_once_with(token["sub"], session)
    budget_repository_create_mock.assert_called_once_with(budget, user, session)
