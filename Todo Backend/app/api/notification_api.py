from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.dependencies.authy_dependencies import get_current_user

from app.services.notification_service import NotificationService

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

@router.get("/")
async def get_notifications(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await NotificationService.get_notifications(
        db,
        current_user.id
    )
@router.patch("/{notification_id}/read")
async def mark_read(
        notification_id: str,
        db: AsyncSession = Depends(get_db)
):

    notification = await NotificationService.get_notification(
        db,
        notification_id
    )

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return await NotificationService.mark_as_read(
        db,
        notification
    )
@router.patch("/read-all")
async def read_all(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await NotificationService.mark_all_read(
        db,
        current_user.id
    )
@router.delete("/{notification_id}")
async def delete_notification(
        notification_id: str,
        db: AsyncSession = Depends(get_db)
):

    notification = await NotificationService.get_notification(
        db,
        notification_id
    )

    await NotificationService.delete_notification(
        db,
        notification
    )

    return {
        "message": "Notification deleted"
    }
@router.get("/unread-count")
async def unread_count(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await NotificationService.unread_count(
        db,
        current_user.id
    )