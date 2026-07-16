from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.models.activity import Activity
from app.dependencies.authy_dependencies import get_current_user

router = APIRouter(
    prefix="/activities",
    tags=["Activities"]
)