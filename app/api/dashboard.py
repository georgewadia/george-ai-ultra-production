from fastapi import APIRouter, Depends

from app.database.database import SessionLocal

from app.database.models import Customer, Message

from app.api.auth import verify_token

router = APIRouter()


@router.get("/dashboard/stats")
async def dashboard_stats(
    user=Depends(verify_token)
):

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
async def get_customers(
    user=Depends(verify_token)
):

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