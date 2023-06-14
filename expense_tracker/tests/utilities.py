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
    data = {
        "title": "Expense tracker",
        "api_docs_enabled": True,
        "postgres_user": "postgre",
        "postgres_password": "postgres",
        "postgres_db": "expense_tracker",
        "postgres_port": "5432",
        "redis_uri": "redis://testconnection:6379",
        "jwt_algorithm": "HS256",
        "jwt_token_access_name": "expense_jwt_token",
        "jwt_token_refresh_name": "X-refresh-token",
        "jwt_expiration": 10080,
        "jwt_secret": "secret_key",
    }
    for key in override:
        data[key] = override[key]

    return data
