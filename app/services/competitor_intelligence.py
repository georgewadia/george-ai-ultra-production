from app.ai.openai_client import client

def improve_content(post_text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "حلل المحتوى واكتب نسخة محسنة ومختلفة."
            },
            {
                "role": "user",
                "content": post_text
            }
        ]
    )

    return response.choices[0].message.content