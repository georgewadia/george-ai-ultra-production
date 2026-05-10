from fastapi import APIRouter, Request
from app.agents.manager_agent import route_message
from app.services.facebook_service import send_message
from app.services.memory_service import save_memory

router = APIRouter()

@router.post("/")
async def webhook(request: Request):
    data = await request.json()

    if data.get("object") == "page":
        for entry in data.get("entry", []):
            if "messaging" in entry:
                for event in entry["messaging"]:
                    if "message" in event:
                        sender = event["sender"]["id"]
                        text = event["message"].get("text", "")

                        save_memory(sender, text)

                        response = route_message(text)

                        send_message(sender, response)

    return {"status": "ok"}