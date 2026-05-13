import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv(
    "FACEBOOK_PAGE_ACCESS_TOKEN"
)

url = (
    f"https://graph.facebook.com/me/accounts"
    f"?access_token={TOKEN}"
)

response = requests.get(url)

print(response.json())