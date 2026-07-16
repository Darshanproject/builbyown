from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.dependencies.authy_dependencies import get_current_user

from app.services.settings_services import SettingsService

router = APIRouter(
    prefix="/settings",
    tags=["Settings"]
)


@router.get("/")
async def get_settings(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await SettingsService.get_settings(
        db,
        current_user.id
    )