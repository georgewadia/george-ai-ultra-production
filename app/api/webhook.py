from fastapi import APIRouter, Request

from app.agents.manager_agent import route_message

from app.services.facebook_service import send_message
from app.services.memory_service import save_memory

from app.database.database import SessionLocal
from app.database.models import Message

router = APIRouter()


@router.post("/")
async def webhook(request: Request):

    try:

        data = await request.json()

        if data.get("object") == "page":

            for entry in data.get("entry", []):

                if "messaging" in entry:

                    for event in entry["messaging"]:

                        # تجاهل رسائل الـ Echo
                        if event.get("message", {}).get("is_echo"):
                            continue

                        if "message" in event:

                            sender_id = event["sender"]["id"]

                            message_text = event["message"].get(
                                "text",
                                ""
                            ).strip()

                            # تجاهل الرسائل الفارغة
                            if not message_text:
                                continue

                            print(
                                f"New Message From {sender_id}: {message_text}"
                            )

                            # حفظ رسالة العميل
                            save_memory(
                                sender_id,
                                message_text
                            )

                            # إنشاء رد AI
                            ai_response = route_message(
                             sender_id,
                            message_text
                            )

                            # إرسال الرد
                            send_message(
                                sender_id,
                                ai_response
                            )

                            # حفظ رد الـ AI
                            db = SessionLocal()

                            ai_message = Message(
                                facebook_id=sender_id,
                                role="assistant",
                                content=ai_response
                            )

                            db.add(ai_message)

                            db.commit()

                            db.close()

        return {
            "status": "ok"
        }

    except Exception as e:

        print(f"Webhook Error: {e}")

        return {
            "status": "error",
            "message": str(e)
        }