from apscheduler.schedulers.background import BackgroundScheduler
from app.services.content_factory import generate_daily_post
from app.services.followup_service import process_followups

scheduler = BackgroundScheduler()

def generate_content():
    post = generate_daily_post()
    print("AI Generated Post:", post)

def start_scheduler():
    scheduler.add_job(generate_content, 'interval', hours=24)
    scheduler.add_job(
    process_followups,
    'interval',
    hours=1
    )
    scheduler.start()