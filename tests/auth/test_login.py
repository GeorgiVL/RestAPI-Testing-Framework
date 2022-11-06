from lib.auth import Auth
from config import APP_URL, LOG


def test_login_as_admin():
    response = Auth().login(APP_URL, "admin", "admin")
    LOG.debug(response.json())
    assert response.ok


