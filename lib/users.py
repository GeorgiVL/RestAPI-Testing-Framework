import json
from config import SESSION, LOG
from lib.utils import build_request_headers

USER_URL = "/users"


def get_current_users(app_url, access_token):
    LOG.info("get_current_users")
    request_headers = build_request_headers(access_token)
    response = SESSION.get(f"{app_url}{USER_URL}/", headers=request_headers)
    LOG.debug(response.json())

    return response


def get_user_id(app_url, access_token):
    LOG.info("get_user_id")
    request_headers = build_request_headers(access_token)
    response = SESSION.get(f"{app_url}{USER_URL}/", headers=request_headers)
    LOG.debug(response.json()[1]["id"])

    return response.json()[1]["id"]


def create_an_user(app_url, access_token, username, password, role):
    LOG.info("create_an_user")
    request_headers = build_request_headers(access_token, content_type="application/json")
    payload = {
        "username": username,
        "password_hash": password,
        "roles": role,
    }

    LOG.debug(f"Request payload: {payload}")
    response = SESSION.post(f"{app_url}{USER_URL}/", headers=request_headers, json=payload)
    LOG.info(response.json())

    return response


def get_current_authenticated_user(app_url, access_token):
    LOG.info("get_current_authenticated_user")
    request_headers = build_request_headers(access_token)
    response = SESSION.get(f"{app_url}{USER_URL}/me", headers=request_headers)
    LOG.debug(response.json())

    return response


def delete_an_user(app_url, access_token, user_id):
    LOG.info("delete_an_user")
    request_headers = build_request_headers(access_token)
    response = SESSION.delete(f"{app_url}{USER_URL}/{user_id}", headers=request_headers)
    LOG.debug(response.json())

    return response
