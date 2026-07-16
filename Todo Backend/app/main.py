from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.auth_api import router as auth_router
from app.core.database import engine
from app.models.base import Base
from app.models import *
from fastapi.middleware.cors import CORSMiddleware
from app.api.task_api import router as task_router
from app.api.category_api import router as category_router
from app.api.settings_api import router as settings_router
from app.api.reminder_api import router as reminder_router
from app.api.upload_api import router as upload_router
from app.api.statistics_api import router as statistics_router
from app.api.user_api import router as user_router
from app.api.note_api import router as note_router
from app.api.admin_api import router as admin_router
from fastapi import WebSocket
from fastapi.staticfiles import StaticFiles
from app.api.notification_api import router as notification_router
from app.api.activity_api import router as activity_router
from app.api.otp_api import router as otp_router
from app.api.websocket_api import router as websocket_router
from app.scheduler.task_scheduler import scheduler
from app.scheduler.jobs import recurring_task_job
from app.scheduler.task_scheduler import scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()

    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)

    yield
    scheduler.shutdown()
    scheduler.add_job(
    recurring_task_job,
    "interval",
    minutes=1
)

    scheduler.start()

    yield

    scheduler.shutdown()

app = FastAPI(
    title="Todo Backend API",
    version="1.0.0",
    lifespan=lifespan
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []

app.mount(
    "/uploads",
    StaticFiles(directory="app/uploads"),
    name="uploads"
)

@app.get("/")
async def root():
    return {
        "message": "Todo Backend Running"
    }


app.include_router(auth_router)
app.include_router(task_router)
app.include_router(category_router)
app.include_router(settings_router)
app.include_router(reminder_router)
app.include_router(upload_router)
app.include_router(statistics_router)
app.include_router(user_router)
app.include_router(note_router)
app.include_router(notification_router)
app.include_router(admin_router)
app.include_router(activity_router)
app.include_router(otp_router)
app.include_router(websocket_router)