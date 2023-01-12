import re
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app import main
from tests.utilities import create_config_dict, restore_env_vars, update_env_vars


@pytest.fixture
def _api_docs_disabled_env_setup():
    config = create_config_dict({"api_docs_enabled": False})
    original_env, new_env = update_env_vars(config)

    yield new_env
    
    restore_env_vars(original_env)


def test_app_settings_api_docs_enabled():
    actual = main.app_settings()

    assert actual == {"title": "Expense Tracker"}


def test_app_settings_api_docs_disabled(_api_docs_disabled_env_setup):
    actual = main.app_settings()

    assert actual == {"docs_url": None, "redoc_url": None, "title": "Expense tracker"}


def test_main_swagger_enabled(client):
    response = client.get("/docs")
    title = re.search(r"<\W*title\W*(.*)</title", response.text, re.IGNORECASE).group(1)

    assert response.status_code == 200
    assert title == "Expense Tracker - Swagger UI"


def test_main_redoc_enabled(client):
    reponse = client.get("/redoc")
    title = re.search(r"<\W*title\W*(.*)</title", reponse.text, re.IGNORECASE).group(1)

    assert reponse.status_code == 200
    assert title == "Expense Tracker - ReDoc"
  