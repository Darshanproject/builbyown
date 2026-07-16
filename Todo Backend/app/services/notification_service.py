from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.websocket.connection_manager import manager
from app.models.notifaction import Notification


class NotificationService:

    @staticmethod
    async def create_notification(
            db: AsyncSession,
            user_id,
            title: str,
            message: str
    ):

        notification = Notification(
            user_id=user_id,
            title=title,    
            message=message
        )

        db.add(notification)

        await db.commit()
        await db.refresh(notification)
        await manager.send_personal_message(
            str(user_id),
            {
                "title": title,
                "message": message
            }
        )

        return notification

    @staticmethod
    async def get_notifications(
            db: AsyncSession,
            user_id
    ):

        result = await db.execute(
            select(Notification)
            .where(Notification.user_id == user_id)
            .order_by(Notification.created_at.desc())
        )

        return result.scalars().all()

    @staticmethod
    async def get_notification(
            db: AsyncSession,
            notification_id
    ):

        result = await db.execute(
            select(Notification)
            .where(Notification.id == notification_id)
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def mark_as_read(
            db: AsyncSession,
            notification
    ):

        notification.is_read = True

        await db.commit()
        await db.refresh(notification)

        return notification

    @staticmethod
    async def mark_all_read(
            db: AsyncSession,
            user_id
    ):

        result = await db.execute(
            select(Notification)
            .where(Notification.user_id == user_id)
        )

        notifications = result.scalars().all()

        for item in notifications:
            item.is_read = True

        await db.commit()

        return {
            "message": "All notifications marked as read"
        }

    @staticmethod
    async def delete_notification(
            db: AsyncSession,
            notification
    ):

        await db.delete(notification)
        await db.commit()

    @staticmethod
    async def unread_count(
            db: AsyncSession,
            user_id
    ):

        count = await db.scalar(
            select(func.count())
            .select_from(Notification)
            .where(
                Notification.user_id == user_id,
                Notification.is_read == False
            )
        )

        return {
            "unread_notifications": count
        }