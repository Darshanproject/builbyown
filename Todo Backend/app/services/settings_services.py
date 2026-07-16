from sqlalchemy import select

from app.models.setting import Settings


class SettingsService:

    @staticmethod
    async def get_settings(
            db,
            user_id
    ):

        result = await db.execute(
            select(Settings)
            .where(Settings.user_id == user_id)
        )

        settings = result.scalar_one_or_none()

        return settings