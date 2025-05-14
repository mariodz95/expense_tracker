import pytest
from fastapi.exceptions import HTTPException

from app.repositories import budget_repository
from tests.factories.budget_factory import BudgetDbFactory, BudgetSchemaFactory
from tests.factories.user_factory import UserDbFactory


async def test_create(session_fixture):
    user_db = await UserDbFactory.create(session=session_fixture)
    budget_schema = BudgetSchemaFactory()

    budget_db = await budget_repository.create(budget_schema, user_db, session_fixture)

    assert budget_db.name == budget_schema.name
    assert budget_db.description == budget_schema.description
    assert budget_db.id != None


async def test_create_duplicate_name_raises_exception(session_fixture):
    user_db = await UserDbFactory.create(session=session_fixture)
    await BudgetDbFactory.create(session=session_fixture, name="test", owner=user_db.id)
    budget_schema = BudgetSchemaFactory(name="test")

    with pytest.raises(HTTPException, match="There is already budget with given name."):
        await budget_repository.create(budget_schema, user_db, session_fixture)
