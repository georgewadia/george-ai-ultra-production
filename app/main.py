from fastapi import FastAPI

from app.api.webhook import router as webhook_router

from app.database.database import engine
from app.database.models import Base

from app.scheduler.scheduler import start_scheduler

from app.api.dashboard import router as dashboard_router

from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI(title="George AI Ultra Production")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(webhook_router)


@app.on_event("startup")
async def startup():
    start_scheduler()


@app.get("/")
async def health():
    return {"status": "ultra-production-running"}

app.include_router(webhook_router)

app.include_router(dashboard_router)