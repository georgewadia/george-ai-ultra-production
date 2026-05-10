from app.database.database import SessionLocal
from app.database.models import Customer, Message
from app.services.lead_engine import calculate_lead_score, detect_lead_status


def save_memory(user_id: str, text: str):

    db = SessionLocal()

    customer = db.query(Customer).filter(
        Customer.facebook_id == user_id
    ).first()

    if not customer:
        customer = Customer(
            facebook_id=user_id
        )

        db.add(customer)

     score = calculate_lead_score(text)

    customer.lead_score += score

    customer.lead_status = detect_lead_status(
    customer.lead_score
)
     

    new_message = Message(
        facebook_id=user_id,
        role="user",
        content=text
    )

    db.add(new_message)

    db.commit()

    db.close()