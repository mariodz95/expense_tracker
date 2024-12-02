import factory

from app.models.budget_model import BudgetDb
from app.schemas.budget_schema import BudgetSchema
from tests.internals.initial_model_factory import InitialBaseFactory


class BudgetDbFactory(InitialBaseFactory):
    class Meta:
        model = BudgetDb

    id = factory.Faker("uuid4")
    name = factory.Faker("pystr")
    description = factory.Faker("pystr")


class BudgetSchemaFactory(factory.Factory):
    class Meta:
        model = BudgetSchema

    name = factory.Faker("pystr")
    description = factory.Faker("pystr")
