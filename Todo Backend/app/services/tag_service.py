from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tag import Tag


class TagService:

    @staticmethod
    async def create_tag(
            db: AsyncSession,
            payload
    ):

        tag = Tag(
            name=payload.name,
            color=payload.color
        )

        db.add(tag)

        await db.commit()

        await db.refresh(tag)

        return tag