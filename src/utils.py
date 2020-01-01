import requests
import json

import constants


def comment(url, text):
    payload = {
        "event": "COMMENT",
        "body": text,
    }

    headers = {
        "Authorization": constants.DBOTTER_GITHUB_BASIC_TOKEN
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    # Should assert the status number is 200
    assert response is not None
