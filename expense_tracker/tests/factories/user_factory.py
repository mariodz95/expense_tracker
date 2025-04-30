from datetime import datetime, timezone
from uuid import uuid4

import factory

from app.models.user_model import UserDb
from app.schemas.user_schema import UserSchema
from tests.factories.initial_model_factory import InitialBaseFactory


class UserSchemaFactory(factory.Factory):
    class Meta:
        model = UserSchema

    username = factory.Faker("pystr")
    email = factory.Faker("email")
    password = factory.Faker("pystr")
    first_name = factory.Faker("pystr")
    last_name = factory.Faker("pystr")
    dob = datetime.now(timezone.utc).replace(tzinfo=None)


class UserDbFactory(InitialBaseFactory):
    class Meta:
        model = UserDb

    id = uuid4()
    username = factory.Faker("pystr")
    email = factory.Faker("email")
    password_hash = factory.Faker("pystr")
    first_name = factory.Faker("pystr")
    last_name = factory.Faker("pystr")
    dob = datetime.now(timezone.utc).replace(tzinfo=None)
