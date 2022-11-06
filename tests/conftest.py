import logging
import pytest
from config import APP_URL, ADMIN_USER, ADMIN_PASSWORD, new_username, new_password
from lib.users import *


@pytest.fixture(scope="session")
def login_as_admin():
    # Authorization
    LOG.info("login_as_admin()")
    payload = {
        "username": ADMIN_USER,
        "password": ADMIN_PASSWORD,
    }
    logging.debug("Login payload: {}".format(payload))
    response = SESSION.post(f"{APP_URL}/auth/login", data=payload)
    assert response.status_code == 200

    # Retrieving the access token
    access_token = response.json()["access_token"]
    yield access_token


@pytest.fixture(scope="session")
def login_as_user():
    # Authorization
    LOG.info("login_as_user()")
    payload = {
        "username": new_username,
        "password": new_password,
    }
    logging.debug("Login payload: {}".format(payload))
    response = SESSION.post(f"{APP_URL}/auth/login", data=payload)
    assert response.status_code == 200

    # Retrieving the access token from a normal user login
    access_token = response.json()["access_token"]
    yield access_token
