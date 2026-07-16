from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.dependencies.authy_dependencies import get_current_user
from app.schemas.category_schema import CreateCategorySchema, UpdateCategorySchema
from app.services.category_service import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post("/")
async def create_category(
        payload: CreateCategorySchema,
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await CategoryService.create_category(
        db,
        current_user.id,
        payload
    )


@router.get("/")
async def get_categories(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    from sqlalchemy import select
    from app.models.category import Category

    result = await db.execute(
        select(Category)
        .where(Category.user_id == current_user.id)
    )

    return result.scalars().all()

@router.get("/search")
async def search_category(
        keyword: str,
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await CategoryService.search_categories(
        db,
        current_user.id,
        keyword
    )

@router.put("/{category_id}")
async def update_category(
        category_id: str,
        payload: UpdateCategorySchema,
        db: AsyncSession = Depends(get_db)
):

    category = await CategoryService.get_category(
        db,
        category_id
    )

    return await CategoryService.update_category(
        db,
        category,
        payload
    )
@router.delete("/{category_id}")
async def delete_category(
        category_id: str,
        db: AsyncSession = Depends(get_db)
):

    category = await CategoryService.get_category(
        db,
        category_id
    )

    await CategoryService.delete_category(
        db,
        category
    )

    return {
        "message": "Category deleted successfully"
    }
@router.get("/page")
async def paginated_categories(
        page: int = 1,
        limit: int = 10,
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await CategoryService.paginated_categories(
        db,
        current_user.id,
        page,
        limit
    )
@router.get("/dashboard")
async def dashboard(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await CategoryService.dashboard(
        db,
        current_user.id
    )
@router.get("/task-count")
async def task_count(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await CategoryService.category_task_count(
        db,
        current_user.id
    )
@router.get("/most-used")
async def most_used(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return await CategoryService.most_used_category(
        db,
        current_user.id
    )