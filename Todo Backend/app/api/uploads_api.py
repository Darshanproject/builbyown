from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.file_handler import save_file
from app.dependencies.authy_dependencies import get_current_user

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)
@router.post("/profile")
async def upload_profile(
        file: UploadFile = File(...),
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    path = await save_file(
        file,
        "profile"
    )

    current_user.profile_image = path

    await db.commit()

    return {
        "message": "Uploaded",
        "file": path
    }
