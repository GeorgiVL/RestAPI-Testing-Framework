import pytest
from config import APP_URL, SESSION


def test_health():
    response = SESSION.get(f"{APP_URL}/health")
    assert response.status_code == 200
