from genericpath import samefile

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.dependencies.authy_dependencies import get_current_user
from app.schemas.note_schema import (
    CreateNoteSchema,
    UpdateNoteSchema
)
from app.services.note_service import NoteService

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.post("/")
async def create_note(
        payload: CreateNoteSchema,
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await NoteService.create_note(
        db,
        current_user.id,
        payload
    )

@router.get("/")
async def get_notes(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await NoteService.get_notes(
        db,
        current_user.id
    )

@router.get("/search")
async def search_notes(
        keyword: str,
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await NoteService.search_notes(
        db,
        current_user.id,
        keyword
    )

@router.get("/page")
async def paginated_notes(
        page: int = 1,
        limit: int = 10,
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await NoteService.paginated_notes(
        db,
        current_user.id,
        page,
        limit
    )
@router.get("/{note_id}")
async def get_note(
        note_id: str,
        db: AsyncSession = Depends(get_db)
):

    note = await NoteService.get_note(
        db,
        note_id
    )

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note
@router.put("/{note_id}")
async def update_note(
        note_id: str,
        payload: UpdateNoteSchema,
        db: AsyncSession = Depends(get_db)
):

    note = await NoteService.get_note(
        db,
        note_id
    )

    return await NoteService.update_note(
        db,
        note,
        payload
    )
@router.delete("/{note_id}")
async def delete_note(
        note_id: str,
        db: AsyncSession = Depends(get_db)
):

    note = await NoteService.get_note(
        db,
        note_id
    )

    await NoteService.delete_note(
        db,
        note
    )

    return {
        "message": "Note deleted successfully"
    }
@router.patch("/{note_id}/pin")
async def pin_note(
        note_id: str,
        db: AsyncSession = Depends(get_db)
):

    note = await NoteService.get_note(db, note_id)

    return await NoteService.pin_note(
        db,
        note
    )

@router.patch("/{note_id}/archive")
async def archive_note(
        note_id: str,
        db: AsyncSession = Depends(get_db)
):

    note = await NoteService.get_note(db, note_id)

    return await NoteService.archive_note(
        db,
        note
    )
@router.patch("/{note_id}/favorite")
async def favorite_note(
        note_id: str,
        db: AsyncSession = Depends(get_db)
):

    note = await NoteService.get_note(db, note_id)

    return await NoteService.favorite_note(
        db,
        note
    )
@router.get("/dashboard")
async def dashboard(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await NoteService.dashboard(
        db,
        current_user.id
    )
@router.post("/note/{note_id}")
async def upload_note_attachment(
        note_id: str,
        file: UploadFile = File(...),
        db: AsyncSession = Depends(get_db)
):

    note = await NoteService.get_note(
        db,
        note_id
    )

    path = await samefile(
        file,
        "notes"
    )

    note.attachment_url = path

    await db.commit()

    return note