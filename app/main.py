from fastapi import FastAPI

from app.api.webhook import router as webhook_router

from app.database.database import engine
from app.database.models import Base

from app.scheduler.scheduler import start_scheduler

from app.api.dashboard import router as dashboard_router

from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router

from fastapi.responses import HTMLResponse


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

app.include_router(auth_router)


@app.get("/delete-data", response_class=HTMLResponse)
async def delete_data():

    return """
    <h1>Delete User Data</h1>

    <p>
    If you want to delete your data from
    George AI System,
    please send a request to:
    georgeai@gmail.com
    </p>
    """