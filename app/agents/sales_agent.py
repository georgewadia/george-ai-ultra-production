from app.ai.openai_client import client
from app.ai.system_prompt import GEORGE_SYSTEM_PROMPT

from app.database.database import SessionLocal
from app.database.models import Message


def get_conversation_history(user_id: str):

    db = SessionLocal()

    messages = db.query(Message).filter(
        Message.facebook_id == user_id
    ).order_by(
        Message.created_at.asc()
    ).limit(20).all()

    db.close()

    history = []

    for msg in messages:

        history.append({
            "role": msg.role,
            "content": msg.content
        })

    return history


def sales_agent(user_id: str, message: str):

    history = get_conversation_history(user_id)

    response = client.chat.completions.create(
        model="gpt-4o",

        messages=[
            {
                "role": "system",
                "content": GEORGE_SYSTEM_PROMPT
            }
        ] + history + [
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content