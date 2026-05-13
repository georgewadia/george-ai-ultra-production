import os
import requests


PAGE_ACCESS_TOKEN = os.getenv(
    "FACEBOOK_PAGE_ACCESS_TOKEN"
)

PAGE_ID = "102774725157552"


def post_to_facebook(message):

    url = f"https://graph.facebook.com/{PAGE_ID}/feed"

    data = {
        "message": message,
        "access_token": PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        url,
        data=data
    )

    return response.json()