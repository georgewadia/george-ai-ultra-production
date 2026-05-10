from app.ai.openai_client import client
from app.ai.system_prompt import GEORGE_SYSTEM_PROMPT

def sales_agent(message: str):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": GEORGE_SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content