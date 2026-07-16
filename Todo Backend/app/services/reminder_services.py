# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.models.reminder import Reminder


# class ReminderService:

#     @staticmethod
#     async def create_reminder(
#             db: AsyncSession,
#             payload
#     ):

#         reminder = Reminder(
#             task_id=payload.task_id,
#             remind_at=payload.remind_at
#         )

#         db.add(reminder)

#         await db.commit()

#         await db.refresh(reminder)

#         return reminder

#     @staticmethod
#     async def get_reminders(
#             db: AsyncSession
#     ):

#         result = await db.execute(
#             select(Reminder)
#         )

#         return result.scalars().all()

from datetime import datetime, date

from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.reminder import Reminder
from app.services.email_service import EmailService

from app.schemas.reminder_schema import (
    CreateReminderSchema,
    UpdateReminderSchema
)


class ReminderService:

    @staticmethod
    async def create_reminder(
            db: AsyncSession,
            user_id,
            payload: CreateReminderSchema
    ):

        reminder = Reminder(
            user_id=user_id,
            title=payload.title,
            reminder_time=payload.remind_at,
            recurring_type=payload.recurring_type
        )

        db.add(reminder)
        await EmailService.send_email(
        reminder.email,
    "Task Reminder",
    {
        "task": reminder.title
    },
    "reminder.html"
)
        await db.commit()
        await db.refresh(reminder)

        return reminder


    @staticmethod
    async def get_reminders(
            db: AsyncSession,
            user_id
    ):

        result = await db.execute(
            select(Reminder)
            .where(Reminder.user_id == user_id)
        )

        return result.scalars().all()


    @staticmethod
    async def get_reminder(
            db: AsyncSession,
            reminder_id
    ):

        result = await db.execute(
            select(Reminder)
            .where(Reminder.id == reminder_id)
        )

        return result.scalar_one_or_none()


    @staticmethod
    async def update_reminder(
            db: AsyncSession,
            reminder: Reminder,
            payload: UpdateReminderSchema
    ):

        if payload.title is not None:
            reminder.title = payload.title

        if payload.remind_at is not None:
            reminder.reminder_time = payload.remind_at

        if payload.recurring_type is not None:
            reminder.recurring_type = payload.recurring_type

        await db.commit()
        await db.refresh(reminder)

        return reminder


    @staticmethod
    async def delete_reminder(
            db: AsyncSession,
            reminder: Reminder
    ):

        await db.delete(reminder)
        await db.commit()


    # @staticmethod
    # async def complete_reminder(
    #         db: AsyncSession,
    #         reminder: Reminder
    # ):

    #     reminder.is_completed = True

    #     await db.commit()
    #     await db.refresh(reminder)

    #     return reminder

    @staticmethod
    async def complete_reminder(
    db: AsyncSession,
    reminder_id
):
        reminder = await ReminderService.get_reminder(
        db,
        reminder_id
    )

        if reminder is None:
            raise HTTPException(
            status_code=404,
            detail="Reminder not found"
        )


        reminder.is_completed = True

        await db.commit()
        await db.refresh(reminder)
        print(reminder_id)
        print(reminder)
        return reminder

    @staticmethod
    async def today_reminders(
            db: AsyncSession,
            user_id
    ):

        result = await db.execute(
            select(Reminder)
            .where(
                Reminder.user_id == user_id,
                func.date(Reminder.reminder_time) == date.today()
            )
        )

        return result.scalars().all()


    @staticmethod
    async def upcoming_reminders(
            db: AsyncSession,
            user_id
    ):

        result = await db.execute(
            select(Reminder)
            .where(
                Reminder.user_id == user_id,
                Reminder.reminder_time >= datetime.now()
            )
        )

        return result.scalars().all()


    @staticmethod
    async def dashboard(
            db: AsyncSession,
            user_id
    ):

        total = await db.scalar(
            select(func.count())
            .select_from(Reminder)
            .where(Reminder.user_id == user_id)
        )

        completed = await db.scalar(
            select(func.count())
            .select_from(Reminder)
            .where(
                Reminder.user_id == user_id,
                Reminder.is_completed == True
            )
        )

        pending = total - completed

        return {
            "total_reminders": total,
            "completed_reminders": completed,
            "pending_reminders": pending
        }