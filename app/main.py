from fastapi import FastAPI

from app.api.webhook import router as webhook_router

from app.database.database import engine
from app.database.models import Base

from app.scheduler.scheduler import start_scheduler


Base.metadata.create_all(bind=engine)

app = FastAPI(title="George AI Ultra Production")

app.include_router(webhook_router)


@app.on_event("startup")
async def startup():
    start_scheduler()


@app.get("/")
async def health():
    return {"status": "ultra-production-running"}