from config import SESSION, LOG
from lib.utils import build_request_headers


class Comments:
    def __init__(self):
        self.comment_url = "/comments"

    def get_all_comments(self, app_url, access_token):
        LOG.info("get_all_comments")
        request_header = build_request_headers(access_token)
        response = SESSION.get(f"{app_url}{self.comment_url}", headers=request_header)

        return response

    def get_comment_id(self, app_url, access_token):
        LOG.info("get_comment_id")
        request_header = build_request_headers(access_token)
        response = SESSION.get(f"{app_url}{self.comment_url}", headers=request_header)

        return response.json()[0]["id"]

    def create_comment(self, app_url, access_token, message):
        LOG.info("create_comment")
        request_headers = build_request_headers(access_token)
        payload_params = {"text": message}
        LOG.debug(f"Request parameters: {payload_params}")
        response = SESSION.post(f"{app_url}{self.comment_url}/", headers=request_headers, params=payload_params)

        return response

    def update_the_comment(self, app_url, access_token, comment_id, **kwargs):
        LOG.info("update_the_comment")
        request_headers = build_request_headers(access_token, content_type="application/json")
        payload = {}

        if "message" in kwargs:
            payload["comment_text"] = kwargs["message"]
        if "likes" in kwargs:
            payload["likes"] = kwargs["likes"]

        response = SESSION.put(f"{app_url}{self.comment_url}/{comment_id}", headers=request_headers, json=payload)

        return response

    def delete_comment(self, app_url, access_token, comment_id):
        LOG.info("delete_comment")
        request_headers = build_request_headers(access_token)
        response = SESSION.delete(f"{app_url}{self.comment_url}/{comment_id}", headers=request_headers)

        return response
