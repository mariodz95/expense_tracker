import factory
from factory import Faker

from app.internals.budget.model import BudgetDb
from app.internals.budget.schema import BudgetSchema
from tests.internals.initial_model_factory import InitialBaseFactory


class BudgetDbFactory(InitialBaseFactory):
    class Meta:
        model = BudgetDb

    id = Faker("uuid4")
    name = Faker("pystr")
    description = Faker("pystr")


class BudgetSchemaFactory(factory.Factory):
    class Meta:
        model = BudgetSchema

    name = Faker("pystr")
    description = Faker("pystr")
