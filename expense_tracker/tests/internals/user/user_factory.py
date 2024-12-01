import factory
from factory import Faker

from app.models.user_model import UserDb
from app.schemas.user_schema import UserSchema
from tests.internals.initial_model_factory import InitialBaseFactory


class UserSchemaFactory(factory.Factory):
    class Meta:
        model = UserSchema

    username = Faker("pystr")
    email = Faker("email")
    password = Faker("pystr")
    first_name = Faker("pystr")
    last_name = Faker("pystr")
    date_of_birth = Faker("date_time")


class UserDbFactory(InitialBaseFactory):
    class Meta:
        model = UserDb

    id = Faker("uuid4")
    username = Faker("pystr")
    email = Faker("email")
    password_hash = Faker("pystr")
    first_name = Faker("pystr")
    last_name = Faker("pystr")
    date_of_birth = Faker("date_time")
