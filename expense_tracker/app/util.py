import os
from typing import Type, get_type_hints

from pydantic import SecretStr

from app.model import PydanticModel


def populate_env_vars(doc_model: Type[PydanticModel]) -> dict:
    """
    Returns dictionary populated with present keys and type casted values from
    environment variables matched in provided Pydantic model.
    """
    env_vars = {}
    type_hints = get_type_hints(doc_model)
    for key in type_hints:
        value = os.getenv(key.upper(), None)
        value_type = type_hints[key]

        if value is None:
            continue
        elif value_type is bool:
            env_vars[key] = value.lower() == "true"
        elif value_type is SecretStr:
            env_vars[key] = value
        else:
            env_vars[key] = value_type(value)

    return env_vars
