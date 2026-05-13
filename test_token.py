import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv(
    "FACEBOOK_PAGE_ACCESS_TOKEN"
)

url = (
    "https://graph.facebook.com/"
    "102774725157552"
)

params = {
    "fields": "name",
    "access_token": TOKEN
}

response = requests.get(
    url,
    params=params
)

print(response.json())