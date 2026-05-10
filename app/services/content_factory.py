from app.ai.openai_client import client

def generate_daily_post():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "أنت خبير تسويق وتشطيبات."
            },
            {
                "role": "user",
                "content": "اكتب بوست تسويقي احترافي باللهجة المصرية."
            }
        ]
    )

    return response.choices[0].message.content