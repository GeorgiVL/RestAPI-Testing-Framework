from lib.users import Users
from config import *


# Positive scenarios
def test_user_creation(login_as_admin):
    response = Users().create_an_user(APP_URL, login_as_admin, new_username, new_password, new_user_role_user)
    assert response.ok


def test_user_info(login_as_user):
    user_info = Users().get_current_authenticated_user(APP_URL, login_as_user)
    assert user_info.ok


# Negative testing
def test_user_cannot_create_user(login_as_user):
    create_an_user = Users().create_an_user(APP_URL, login_as_user, second_new_username, second_new_password,
                                            new_user_role_user)
    assert not create_an_user.ok


def test_user_cannot_delete_user(login_as_user, login_as_admin):
    user_id = Users().get_user_id(APP_URL, login_as_admin)
    delete_an_user = Users().delete_an_user(APP_URL, login_as_user, user_id)
    assert not delete_an_user
