from app.database.database import SessionLocal
from app.database.models import Customer, Message


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

    new_message = Message(
        facebook_id=user_id,
        role="user",
        content=text
    )

    db.add(new_message)

    db.commit()

    db.close()