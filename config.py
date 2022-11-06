import logging

import requests
import os

SESSION = requests.Session()

APP_URL = os.getenv("APP_URL", "")
ADMIN_USER = os.getenv("ADMIN_USER", "")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")

new_username = os.getenv("new_username", "")
new_password = os.getenv("new_password", "")
new_user_role_user = os.getenv("new_user_role_user", "")

second_new_username = os.getenv("second_new_username", "")
second_new_password = os.getenv("second_new_password", "")

new_username_admin = os.getenv("new_username_admin", "")
new_password_admin = os.getenv("new_password_admin", "")
new_user_role_admin = os.getenv("new_user_role_admin", "")

LOG = logging.getLogger()


class HideSensitiveData(logging.Filter):
    def filter(self, record) -> bool:
        record.msg = str(record).replace(ADMIN_PASSWORD, "*******")
        return True


LOG.addFilter(HideSensitiveData())
