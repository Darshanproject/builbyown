from sqlalchemy.ext.asyncio import AsyncSession

from app.models.activity import Activity


class ActivityService:

    @staticmethod
    async def log(
            db: AsyncSession,
            user_id,
            action: str
    ):

        activity = Activity(
            user_id=user_id,
            action=action
        )

        db.add(activity)

        await db.commit()

        return activity