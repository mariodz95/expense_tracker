from datetime import datetime, timezone
from uuid import uuid4

from factory import Factory, Faker, LazyFunction
from pydantic import SecretStr

from app.database.models import UserDb
from app.schemas.user_schema import UserSchema
from tests.factories.initial_model_factory import InitialBaseFactory


class UserSchemaFactory(Factory):
    class Meta:
        model = UserSchema

    id = LazyFunction(uuid4)
    username = Faker("pystr")
    email = Faker("email")
    password = SecretStr(Faker("password"))
    first_name = Faker("pystr")
    last_name = Faker("pystr")
    dob = datetime.now(timezone.utc).replace(tzinfo=None)

    @classmethod
    def _build(cls, model_class, *args, **kwargs):
        return model_class.model_construct(**kwargs)


class UserDbFactory(InitialBaseFactory):
    class Meta:
        model = UserDb

    id = LazyFunction(uuid4)
    created_by = "SYSTEM"
    username = Faker("pystr")
    email = Faker("email")
    password_hash = Faker("pystr")
    first_name = Faker("pystr")
    last_name = Faker("pystr")
    dob = datetime.now(timezone.utc).replace(tzinfo=None)
