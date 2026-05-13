import requests

from app.config.settings import settings


def send_message(recipient_id, text):

    url = (
        "https://graph.facebook.com/v21.0/me/messages"
        f"?access_token={settings.FACEBOOK_PAGE_ACCESS_TOKEN}"
    )

    payload = {
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": text
        }
    }

    response = requests.post(
        url,
        json=payload
    )

    print("FACEBOOK RESPONSE:")
    print(response.status_code)
    print(response.text)