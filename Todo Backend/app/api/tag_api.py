from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.tag_schema import CreateTagSchema
from app.services.tag_service import TagService

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)


@router.post("/")
async def create_tag(
        payload: CreateTagSchema,
        db: AsyncSession = Depends(get_db)
):

    return await TagService.create_tag(
        db,
        payload
    )   