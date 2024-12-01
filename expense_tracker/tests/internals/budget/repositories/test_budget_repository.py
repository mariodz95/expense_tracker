from app.repositories import budget_repository
from tests.internals.budget.budget_factory import BudgetSchemaFactory
from tests.internals.user.user_factory import UserDbFactory


async def test_create(session_fixture):
    user_db = UserDbFactory.build()
    budget_schema = BudgetSchemaFactory()

    budget_db = await budget_repository.create(budget_schema, user_db, session_fixture)

    assert budget_db.name == budget_schema.name
    assert budget_db.description == budget_schema.description
    assert budget_db.id != None
