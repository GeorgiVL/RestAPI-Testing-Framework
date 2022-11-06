def build_request_headers(access_token, access_type="application/json", **kwargs):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": f"{access_type}",
    }

    if "Content-Type" in kwargs:
        headers["Content-Type"] = kwargs["Content-Type"]

    return headers


