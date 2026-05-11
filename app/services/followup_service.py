from datetime import datetime

from app.database.database import SessionLocal
from app.database.models import Customer

from app.services.facebook_service import send_message


def process_followups():

    db = SessionLocal()

    customers = db.query(Customer).all()

    now = datetime.utcnow()

    for customer in customers:

        # تجاهل العملاء الساخنين
        if customer.lead_status == "HOT":
            continue

        # أول Follow-up
        if customer.last_followup is None:

            message = (
                "يا فنان لو حابب ابعتلي مساحة المكان "
                "أقدر أرشحلك أفضل تصميم مناسب ✨"
            )

            send_message(
                customer.facebook_id,
                message
            )

            customer.last_followup = now

        else:

            hours_passed = (
                now - customer.last_followup
            ).total_seconds() / 3600

            # Follow-up كل 24 ساعة
            if hours_passed >= 24:

                message = (
                    "لسه معاك يا فنان 😊 "
                    "لو حابب أساعدك في التصميم أو التسعير "
                    "ابعتلي أي تفاصيل."
                )

                send_message(
                    customer.facebook_id,
                    message
                )

                customer.last_followup = now

    db.commit()

    db.close()