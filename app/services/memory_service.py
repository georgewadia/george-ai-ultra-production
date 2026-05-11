from app.database.database import SessionLocal
from app.database.models import Customer, Message

from app.services.lead_engine import (
    calculate_lead_score,
    detect_lead_status
)


def save_memory(user_id: str, text: str):

    db = SessionLocal()

    customer = db.query(Customer).filter(
        Customer.facebook_id == user_id
    ).first()

    # إنشاء عميل جديد إذا غير موجود
    if not customer:

        customer = Customer(
            facebook_id=user_id,
            lead_score=0,
            lead_status="COLD"
        )

        db.add(customer)

    # حساب النقاط
    score = calculate_lead_score(text)

    # معالجة مشكلة None
    if customer.lead_score is None:
        customer.lead_score = 0

    # تحديث النقاط
    customer.lead_score += score

    # تحديث الحالة
    customer.lead_status = detect_lead_status(
        customer.lead_score
    )

    # حفظ الرسالة
    new_message = Message(
        facebook_id=user_id,
        role="user",
        content=text
    )

    db.add(new_message)

    db.commit()

    db.close()