import json
import time

import requests

API_URL = "https://api.dax.cloud/walker/generatePath"

errorMessageMapping = {
    "UNMAPPED_REGION": "Unmapped region",
    "BLOCKED": "Tile is blocked",
    "EXCEEDED_SEARCH_LIMIT": "Exceeded search limit",
    "UNREACHABLE": "Unreachable tile",
    "NO_WEB_PATH": "No web path",
    "INVALID_CREDENTIALS": "Invalid credentials",
    "RATE_LIMIT_EXCEEDED": "Rate limit exceeded",
    "NO_RESPONSE_FROM_SERVER": "No response from server",
    "UNKNOWN": "Unknown"
}


def post_http_path(start, end, api_key, api_secret):
    headers = {
        "key": api_key,
        "secret": api_secret
    }
    pathArray = {"start": {
        "x": start[0],
        "y": start[1],
        "z": start[2]
    },
        "end": {
            "x": end[0],
            "y": end[1],
            "z": end[2]
        }
    }
    data = pathArray
    # data = json.dumps(pathArray, separators=(',', ':'))
    print(data)
    response = requests.post(API_URL, json=data, headers=headers)
    print(response.text)
    result = response.text
    #stats = json.loads(response.text)
    #print(stats)
    return result

API_KEY = "sub_DPjXXzL5DeSiPf"
#API_KEY = "sub_DPjcfqN4YkIxm8"
API_SECRET = "PUBLIC-KEY"
start = (3223,3218,0)
#print(start[0])
end = (3164,3480,0)

#post_http_path(start, end, API_KEY, API_SECRET)
