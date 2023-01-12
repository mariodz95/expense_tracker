import pytest
from pydantic import BaseModel, SecretStr

from app import util
from tests.utilities import restore_env_vars, update_env_vars


@pytest.fixture
def some_class_dict():

    return {
        "bool_attr": "true",
        "int_attr": "456",
        "float_attr": "3.14",
        "str_attr": "asdf",
        "secret_attr": "secret",
    }


@pytest.fixture
def _some_class_env_setup(some_class_dict):
    original_env, new_env = update_env_vars(some_class_dict)

    yield new_env

    restore_env_vars(original_env)


class SomeClass(BaseModel):
    optional_attr: str = None
    bool_attr: bool
    int_attr: int
    float_attr: float
    str_attr: str
    secret_attr: SecretStr


def test_populate_env_vars(_some_class_env_setup, some_class_dict):
    expected = SomeClass(**some_class_dict).dict(exclude_defaults=True)
    expected["secret_attr"] = "secret"

    actual = util.populate_env_vars(SomeClass)

    assert actual == expected
