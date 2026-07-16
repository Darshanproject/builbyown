import os
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "uploads"


async def save_file(
        file: UploadFile,
        folder: str
):

    ext = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{ext}"

    folder_path = os.path.join(
        UPLOAD_DIR,
        folder
    )

    os.makedirs(
        folder_path,
        exist_ok=True
    )

    file_path = os.path.join(
        folder_path,
        filename
    )

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    return file_path