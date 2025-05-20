from uuid import uuid4

import factory

from app.database.models import BudgetDb
from app.schemas.budget_schema import BudgetSchema

from .initial_model_factory import InitialBaseFactory


class BudgetDbFactory(InitialBaseFactory):
    class Meta:
        model = BudgetDb

    id = uuid4()
    name = factory.Faker("pystr")
    description = factory.Faker("pystr")


class BudgetSchemaFactory(factory.Factory):
    class Meta:
        model = BudgetSchema

    name = factory.Faker("pystr")
    description = factory.Faker("pystr")
