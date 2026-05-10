from apscheduler.schedulers.background import BackgroundScheduler
from app.services.content_factory import generate_daily_post

scheduler = BackgroundScheduler()

def generate_content():
    post = generate_daily_post()
    print("AI Generated Post:", post)

def start_scheduler():
    scheduler.add_job(generate_content, 'interval', hours=24)
    scheduler.start()