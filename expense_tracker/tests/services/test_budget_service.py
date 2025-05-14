from unittest.mock import AsyncMock

from app.schemas.budget_schema import BudgetSchema
from app.services import budget_service
from tests.factories.budget_factory import BudgetDbFactory
from tests.factories.user_factory import UserDbFactory


async def test_create(mocker, session_fixture):
    budget = BudgetSchema(name="test budget", description="test budget")
    budget_db = BudgetDbFactory.build()
    user = UserDbFactory.build()
    expected = BudgetSchema(**budget_db.model_dump())
    token = {"sub": "user@email.com"}

    user_repository_get_mock = mocker.patch(
        "app.services.budget_service.user_repository.get_by_id",
        AsyncMock(return_value=user),
    )
    budget_repository_create_mock = mocker.patch(
        "app.services.budget_service.budget_repository.create",
        AsyncMock(return_value=budget_db),
    )

    response = await budget_service.create(budget, token, session_fixture)

    assert response == expected
    user_repository_get_mock.assert_called_once_with(
        id=token["sub"], session=session_fixture
    )
    budget_repository_create_mock.assert_called_once_with(
        budget=budget, user=user, session=session_fixture
    )
