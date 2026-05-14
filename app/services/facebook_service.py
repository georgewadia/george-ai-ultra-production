import requests

from app.config.settings import settings


def clean_text(text: str):

    if not text:
        return ""

    # إزالة Markdown
    text = (
        text
        .replace("**", "")
        .replace("*", "")
        .replace("#", "")
        .replace("```", "")
    )

    # تقليل طول الرسالة
    text = text[:900]

    return text


def send_message(recipient_id, text):

    text = clean_text(text)

    url = (
        "https://graph.facebook.com/v21.0/me/messages"
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

    print("FACEBOOK MESSAGE RESPONSE:")
    print(response.status_code)
    print(response.text)


def reply_to_comment(comment_id, text):

    text = clean_text(text)

    url = (
        f"https://graph.facebook.com/v21.0/"
        f"{comment_id}/comments"
        f"?access_token="
        f"{settings.FACEBOOK_PAGE_ACCESS_TOKEN}"
    )

    payload = {
        "message": text
    }

    response = requests.post(
        url,
        json=payload
    )

    print("FACEBOOK COMMENT RESPONSE:")
    print(response.status_code)
    print(response.text)