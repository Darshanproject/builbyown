from pydantic import BaseModel


class CreateNoteSchema(BaseModel):
    title: str
    content: str


class UpdateNoteSchema(BaseModel):
    title: str | None = None
    content: str | None = None


class NoteResponse(BaseModel):
    id: str
    title: str
    content: str
    is_pinned: bool
    is_archived: bool
    is_favorite: bool