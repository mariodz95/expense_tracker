import factory
from factory import Faker
from app.internals.user.schema import UserSchema


class UserSchemaFactory(factory.Factory):
    class Meta:
        model = UserSchema

    username = Faker("pystr")
    email = Faker("email")
    password = Faker("pystr")
    first_name = Faker("pystr")
    last_name = Faker("pystr")
    date_of_birth = Faker("date_time")
