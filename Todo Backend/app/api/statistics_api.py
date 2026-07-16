from fastapi import APIRouter, Depends
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.dependencies.authy_dependencies import get_current_user

from app.models.task import Task

router = APIRouter(
    prefix="/statistics",
    tags=["Statistics"]
)


@router.get("/")
async def statistics(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    total = await db.scalar(
        select(func.count())
        .select_from(Task)
        .where(Task.user_id == current_user.id)
    )

    completed = await db.scalar(
        select(func.count())
        .select_from(Task)
        .where(
            Task.user_id == current_user.id,
            Task.completed == True
        )
    )

    important = await db.scalar(
        select(func.count())
        .select_from(Task)
        .where(
            Task.user_id == current_user.id,
            Task.is_important == True
        )
    )

    pending = total - completed

    completion_rate = (
        completed / total * 100
        if total > 0
        else 0
    )

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "important_tasks": important,
        "completion_rate": round(
            completion_rate,
            2
        )
    }