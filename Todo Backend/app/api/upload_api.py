import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_file(
        file: UploadFile = File(...)
):

    path = f"app/uploads/{file.filename}"

    with open(path, "wb") as buffer:
        buffer.write(
            await file.read()
        )

    return {
        "filename": file.filename
    }
@router.post("/profile_image")
async def upload_file(
        file: UploadFile = File(...)
):

    path = f"app/uploads/profile/{file.filename}"

    with open(path, "wb") as buffer:
        buffer.write(
            await file.read()
        )

    return {
        "filename": file.filename
    }
@router.post("/task_attachment")
async def upload_file(
        file: UploadFile = File(...)
):

    path = f"app/uploads/task/{file.filename}"

    with open(path, "wb") as buffer:
        buffer.write(
            await file.read()
        )

    return {
        "filename": file.filename
    }
@router.post("/notes_attachment")
async def upload_file(
        file: UploadFile = File(...)
):

    path = f"app/uploads/notes/{file.filename}"

    with open(path, "wb") as buffer:
        buffer.write(
            await file.read()
        )

    return {
        "filename": file.filename
    }