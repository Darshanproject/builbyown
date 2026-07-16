from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.services.auth_services import AuthService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
async def get_all_users(
        db: AsyncSession = Depends(get_db)
):

    return await AuthService.get_all_users(db)


@router.get("/count")
async def get_user_count(
        db: AsyncSession = Depends(get_db)
):

    total = await AuthService.get_total_users(db)

    return {
        "total_users": total
    }