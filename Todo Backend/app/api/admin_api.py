from logging import Manager

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.dependencies.authy_dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.models.task import Task
from app.models.note import Note

from app.dependencies.admin_dependency import (
    admin_required
)
router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)
@router.get("/dashboard")
async def dashboard(
        db: AsyncSession = Depends(get_db),
        admin=Depends(admin_required)
):

    users = await db.scalar(
        select(func.count())
        .select_from(User)
    )

    tasks = await db.scalar(
        select(func.count())
        .select_from(Task)
    )

    notes = await db.scalar(
        select(func.count())
        .select_from(Note)
    )

    return {
        "total_users": users,
        "total_tasks": tasks,
        "total_notes": notes
    }
@router.get("/users")
async def get_users(
        db: AsyncSession = Depends(get_db),
        admin=Depends(admin_required)
):

    result = await db.execute(
        select(User)
    )

    return result.scalars().all()
@router.patch("/users/{user_id}/ban")
async def ban_user(
        user_id: str,
        db: AsyncSession = Depends(get_db),
        admin=Depends(admin_required)
):

    result = await db.execute(
        select(User)
        .where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    user.is_banned = True

    await db.commit()

    return {
        "message": "User banned"
    }
@router.patch("/users/{user_id}/unban")
async def unban_user(
        user_id: str,
        db: AsyncSession = Depends(get_db),
        admin=Depends(admin_required)
):

    result = await db.execute(
        select(User)
        .where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    user.is_banned = False

    await db.commit()

    return {
        "message": "User unbanned"
    }
@router.patch("/users/{user_id}/disable")
async def disable_user(
        user_id: str,
        db: AsyncSession = Depends(get_db),
        admin=Depends(admin_required)
):

    result = await db.execute(
        select(User)
        .where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    user.is_active = False

    await db.commit()

    return {
        "message": "User disabled"
    }
# @router.post("/broadcast")
# async def broadcast_message(
#         payload: BroadcastSchema,
#         current_user=Depends(get_current_user)
# ):

#     if current_user.role != "admin":
#         raise HTTPException(
#             status_code=403,
#             detail="Forbidden"
#         )

#     await Manager.broadcast(
#         {
#             "type": "broadcast",
#             "message": payload.message
#         }
#     )

#     return {
#         "message": "Broadcast sent"
#     }