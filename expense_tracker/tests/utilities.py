import os


def update_env_vars(env: dict) -> tuple[dict, dict]:
    new_env = convert_to_env_vars(env)
    original_env = dict(os.environ)
    os.environ.update(new_env)

    return original_env, new_env


def restore_env_vars(original_env: dict):
    os.environ.clear()
    os.environ.update(original_env)


def convert_to_env_vars(data: dict) -> dict:
    return {key.upper(): str(data[key]) for key in data}


def create_config_dict(override: dict = {}) -> dict:
    data = {"title": "Expense tracker", "api_docs_enabled": "True"}
    for key in override:
        data[key] = override[key]

    return data
