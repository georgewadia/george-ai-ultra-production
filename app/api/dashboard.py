from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.models import Customer, Message

router = APIRouter()


@router.get("/dashboard/stats")
async def dashboard_stats():

    db = SessionLocal()

    total_customers = db.query(Customer).count()

    hot_leads = db.query(Customer).filter(
        Customer.lead_status == "HOT"
    ).count()

    total_messages = db.query(Message).count()

    db.close()

    return {
        "total_customers": total_customers,
        "hot_leads": hot_leads,
        "total_messages": total_messages
    }


@router.get("/dashboard/customers")
async def get_customers():

    db = SessionLocal()

    customers = db.query(Customer).all()

    data = []

    for customer in customers:

        data.append({
            "facebook_id": customer.facebook_id,
            "lead_status": customer.lead_status,
            "lead_score": customer.lead_score
        })

    db.close()

    return data