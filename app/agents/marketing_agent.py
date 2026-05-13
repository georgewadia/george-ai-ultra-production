from openai import OpenAI

from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


SYSTEM_PROMPT = """
أنت خبير تسويق احترافي متخصص في:
- الجبس بورد
- الديكورات
- التشطيبات
- التصميم الداخلي

مهمتك:
إنشاء منشورات تسويقية قوية جدًا باللهجة المصرية.

يجب أن تكون المنشورات:
- جذابة
- احترافية
- قصيرة نسبيًا
- تحتوي Hook قوي
- تحتوي CTA
- تدفع العميل للتفاعل
- متنوعة
- غير مكررة

وأحيانًا:
- أفكار ريلز
- نصوص فيديوهات قصيرة
- أفكار قبل/بعد
- أفكار مودرن
- نصائح تشطيب
- أخطاء شائعة
- أفكار سقف جبس بورد
- إضاءة مخفية
- ديكورات غرف نوم وريسبشن

الأسلوب:
كأن مهندس محترف وخبير يتحدث بثقة.
"""


def marketing_agent(topic="منشور تسويقي عن الجبس بورد"):

    prompt = f"""
    أنشئ منشور Facebook احترافي عن:
    {topic}

    المطلوب:
    - Hook قوي
    - محتوى جذاب
    - CTA
    - Hashtags
    """

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        temperature=0.9,
        max_tokens=500
    )

    return response.choices[0].message.content