import factory
from factory import Faker
from app.internals.budget.model import BudgetDb


class BudgetDbFactory(factory.Factory):
    class Meta:
        model = BudgetDb

    id = Faker("uuid4")
    name = Faker("pystr")
    description = Faker("pystr")
