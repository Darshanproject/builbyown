from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func
from app.models.note import Note
from app.schemas.note_schema import (
    CreateNoteSchema,
    UpdateNoteSchema
)


class NoteService:

    @staticmethod
    async def create_note(
            db: AsyncSession,
            user_id,
            payload: CreateNoteSchema
    ):

        note = Note(
            user_id=user_id,
            title=payload.title,
            content=payload.content
        )

        db.add(note)
        await db.commit()
        await db.refresh(note)

        return note

    @staticmethod
    async def get_notes(
            db: AsyncSession,
            user_id
    ):

        result = await db.execute(
            select(Note)
            .where(Note.user_id == user_id)
        )

        return result.scalars().all()

    @staticmethod
    async def get_note(
            db: AsyncSession,
            note_id
    ):

        result = await db.execute(
            select(Note)
            .where(Note.id == note_id)
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def update_note(
            db: AsyncSession,
            note: Note,
            payload: UpdateNoteSchema
    ):

        if payload.title is not None:
            note.title = payload.title

        if payload.content is not None:
            note.content = payload.content

        await db.commit()
        await db.refresh(note)

        return note

    @staticmethod
    async def delete_note(
            db: AsyncSession,
            note: Note
    ):

        await db.delete(note)
        await db.commit()

    @staticmethod
    async def pin_note(
        db: AsyncSession,
        note: Note
):

        note.is_pinned = not note.is_pinned

        await db.commit()
        await db.refresh(note)

        return note
    
    @staticmethod
    async def archive_note(
        db: AsyncSession,
        note: Note
):

        note.is_archived = not note.is_archived

        await db.commit()
        await db.refresh(note)

        return note
    
    @staticmethod
    async def favorite_note(
        db: AsyncSession,
        note: Note
):

        note.is_favorite = not note.is_favorite

        await db.commit()
        await db.refresh(note)

        return note
    
    @staticmethod
    async def search_notes(
        db: AsyncSession,
        user_id,
        keyword: str
):

        result = await db.execute(
        select(Note).where(
            Note.user_id == user_id,
            Note.title.ilike(f"%{keyword}%")
        )
    )

        return result.scalars().all()
    
    @staticmethod
    async def paginated_notes(
        db: AsyncSession,
        user_id,
        page: int,
        limit: int
):

        offset = (page - 1) * limit

        result = await db.execute(
        select(Note)
        .where(Note.user_id == user_id)
        .offset(offset)
        .limit(limit)
    )

        return result.scalars().all()
    
    @staticmethod
    async def dashboard(
        db: AsyncSession,
        user_id
):

        total = await db.scalar(
        select(func.count())
        .select_from(Note)
        .where(Note.user_id == user_id)
    )

        pinned = await db.scalar(
        select(func.count())
        .select_from(Note)
        .where(
            Note.user_id == user_id,
            Note.is_pinned == True
        )
    )

        archived = await db.scalar(
        select(func.count())
        .select_from(Note)
        .where(
            Note.user_id == user_id,
            Note.is_archived == True
        )
    )

        favorite = await db.scalar(
        select(func.count())
        .select_from(Note)
        .where(
            Note.user_id == user_id,
            Note.is_favorite == True
        )
    )

        return {
        "total_notes": total,
        "pinned_notes": pinned,
        "archived_notes": archived,
        "favorite_notes": favorite
    }