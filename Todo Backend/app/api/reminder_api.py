from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.schemas.reminder_schema import CreateReminderSchema, UpdateReminderSchema
from app.dependencies.authy_dependencies import get_current_user

from app.services.reminder_services import ReminderService

router = APIRouter(
    prefix="/reminders",
    tags=["Reminders"]
)


@router.post("/")
async def create_reminder(
        payload: CreateReminderSchema,
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await ReminderService.create_reminder(
        db,
        current_user.id,
        payload
    )


@router.get("/")
async def get_reminders(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await ReminderService.get_reminders(
        db,
        current_user.id
    )

@router.get("/today")
async def today_reminders(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await ReminderService.today_reminders(
        db,
        current_user.id
    )

@router.get("/upcoming")
async def upcoming_reminders(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await ReminderService.upcoming_reminders(
        db,
        current_user.id
    )

@router.get("/dashboard")
async def dashboard(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await ReminderService.dashboard(
        db,
        current_user.id
    )

@router.get("/{reminder_id}")
async def get_reminder(
        reminder_id: str,
        db: AsyncSession = Depends(get_db)
):

    reminder = await ReminderService.get_reminder(
        db,
        reminder_id
    )

    if not reminder:
        raise HTTPException(
            status_code=404,
            detail="Reminder not found"
        )

    return reminder

@router.put("/{reminder_id}")
async def update_reminder(
        reminder_id: str,
        payload: UpdateReminderSchema,
        db: AsyncSession = Depends(get_db)
):

    reminder = await ReminderService.get_reminder(
        db,
        reminder_id
    )

    return await ReminderService.update_reminder(
        db,
        reminder,
        payload
    )

@router.delete("/{reminder_id}")
async def delete_reminder(
        reminder_id: str,
        db: AsyncSession = Depends(get_db)
):

    reminder = await ReminderService.get_reminder(
        db,
        reminder
    )

    await ReminderService.delete_reminder(
        db,
        reminder
    )

    return {
        "message": "Reminder deleted successfully"
    }


@router.patch("/id/{reminder_id}/complete")
async def complete_reminder(
        reminder_id: str,
        db: AsyncSession = Depends(get_db)
):

    reminder = await ReminderService.get_reminder(
        db,
        reminder_id
    )

    return await ReminderService.complete_reminder(
        db,
        reminder
    )