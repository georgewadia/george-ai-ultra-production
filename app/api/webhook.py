from fastapi import APIRouter, Request

from app.agents.manager_agent import route_message

from app.services.facebook_service import (
    send_message,
    reply_to_comment
)

from app.services.memory_service import save_memory

from app.database.database import SessionLocal
from app.database.models import Message

from app.config.settings import settings

router = APIRouter()


# =====================================
# Facebook Verification
# =====================================

@router.get("/")
async def verify_webhook(
    hub_mode: str = None,
    hub_verify_token: str = None,
    hub_challenge: str = None
):

    if (
        hub_mode == "subscribe"
        and hub_verify_token == settings.VERIFY_TOKEN
    ):

        return int(hub_challenge)

    return {
        "error": "Verification failed"
    }


# =====================================
# Facebook Events
# =====================================

@router.post("/")
async def webhook(request: Request):

    try:

        data = await request.json()

        print("WEBHOOK DATA:")
        print(data)

        if data.get("object") == "page":

            for entry in data.get("entry", []):

                # =========================
                # Messenger Messages
                # =========================

                if "messaging" in entry:

                    for event in entry["messaging"]:

                        if event.get(
                            "message",
                            {}
                        ).get("is_echo"):
                            continue

                        if "message" in event:

                            sender_id = (
                                event["sender"]["id"]
                            )

                            message_text = (
                                event["message"]
                                .get("text", "")
                                .strip()
                            )

                            if not message_text:
                                continue

                            print(
                                f"New Message From "
                                f"{sender_id}: "
                                f"{message_text}"
                            )

                            save_memory(
                                sender_id,
                                message_text
                            )

                            ai_response = route_message(
                                sender_id,
                                message_text
                            )

                            print(
                                f"AI Response: "
                                f"{ai_response}"
                            )

                            send_message(
                                sender_id,
                                ai_response
                            )

                            db = SessionLocal()

                            ai_message = Message(
                                facebook_id=sender_id,
                                role="assistant",
                                content=ai_response
                            )

                            db.add(ai_message)

                            db.commit()

                            db.close()

                # =========================
                # Facebook Comments
                # =========================

                if "changes" in entry:

                    for change in entry["changes"]:

                        if (
                            change.get("field")
                            == "feed"
                        ):

                            value = change.get(
                                "value",
                                {}
                            )

                            if (
                                value.get("item")
                                == "comment"
                            ):

                                comment_text = value.get(
                                    "message",
                                    ""
                                )

                                comment_id = value.get(
                                    "comment_id"
                                )

                                sender_name = (
                                    value.get(
                                        "from",
                                        {}
                                    ).get(
                                        "name",
                                        "User"
                                    )
                                )

                                print(
                                    f"New Comment "
                                    f"From {sender_name}: "
                                    f"{comment_text}"
                                )

                                ai_reply = route_message(
                                    sender_name,
                                    comment_text
                                )

                                print(
                                    f"AI Comment Reply: "
                                    f"{ai_reply}"
                                )

                                reply_to_comment(
                                    comment_id,
                                    ai_reply
                                )

        return {
            "status": "ok"
        }

    except Exception as e:

        print(
            f"Webhook Error: {e}"
        )

        return {
            "status": "error",
            "message": str(e)
        }