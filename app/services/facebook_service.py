import requests

from app.config.settings import settings


def send_message(recipient_id, text):

    url = (
        "https://graph.facebook.com/"
        "v21.0/me/messages"
        f"?access_token="
        f"{settings.FACEBOOK_PAGE_ACCESS_TOKEN}"
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

    return response.json()


def reply_to_comment(comment_id, message):

    url = (
        f"https://graph.facebook.com/"
        f"v21.0/{comment_id}/comments"
    )

    payload = {
        "message": message,
        "access_token":
        settings.FACEBOOK_PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        url,
        data=payload
    )

    return response.json()