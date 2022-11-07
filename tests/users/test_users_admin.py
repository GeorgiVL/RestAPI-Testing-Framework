from lib.users import *
from config import new_username_admin, new_user_role_admin, new_password_admin, APP_URL


def test_admin_delete_an_user(login_as_admin):
    user_id = get_user_id(APP_URL, login_as_admin)
    user_deletion = delete_an_user(APP_URL, login_as_admin, user_id)
    assert user_deletion.ok


def test_admin_creation(login_as_admin):
    admin_creation = create_an_user(APP_URL, login_as_admin, new_username_admin, new_password_admin,
                                    new_user_role_admin)
    assert admin_creation.ok


def test_admin_delete_admin(login_as_admin):
    user_id = get_user_id(APP_URL, login_as_admin)
    admin_deletion = delete_an_user(APP_URL, login_as_admin, user_id)
    assert admin_deletion.ok
