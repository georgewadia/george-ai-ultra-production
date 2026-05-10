from fastapi import FastAPI
from app.api.webhook import router as webhook_router
from app.scheduler.scheduler import start_scheduler

app = FastAPI(title="George AI Ultra Production")

app.include_router(webhook_router)

@app.on_event("startup")
async def startup():
    start_scheduler()

@app.get("/")
async def health():
    return {"status": "ultra-production-running"}