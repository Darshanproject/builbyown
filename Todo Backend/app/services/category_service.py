# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select, func
# from app.models import Category, Task
# from app.schemas.category_schema import UpdateCategorySchema


# class CategoryService:

#     @staticmethod
#     async def create_category(
#             db: AsyncSession,
#             user_id,
#             payload
#     ):

#         category = Category(
#             user_id=user_id,
#             name=payload.name,
#             color=payload.color
#         )

#         db.add(category)

#         await db.commit()

#         await db.refresh(category)

#         return category
    

#     @staticmethod
#     async def update_category(
#         db: AsyncSession,
#         category: Category,
#         payload: UpdateCategorySchema
# ):

#      if payload.name is not None:
#         category.name = payload.name

#      if payload.color is not None:
#         category.color = payload.color

#         if payload.icon is not None:
#          category.icon = payload.icon

#         await db.commit()
#         await db.refresh(category)

#         return category
     

#      @staticmethod
#      async def delete_category(
#         db: AsyncSession,
#         category: Category
# ):

#       await db.delete(category)
#       await db.commit()

#     @staticmethod
#     async def search_categories(
#         db: AsyncSession,
#         user_id,
#         keyword: str
# ):

#         result = await db.execute(
#          select(Category).where(
#             Category.user_id == user_id,
#             Category.name.ilike(f"%{keyword}%")
#         )
#     )

#         return result.scalars().all()
#     @staticmethod
#     async def paginated_categories(
#         db: AsyncSession,
#         user_id,
#         page: int,
#         limit: int
# ):

#      offset = (page - 1) * limit

#      result = await db.execute(
#         select(Category)
#         .where(Category.user_id == user_id)
#         .offset(offset)
#         .limit(limit)
#     )

#      return result.scalars().all()

#     @staticmethod
#     async def dashboard(
#         db: AsyncSession,
#         user_id
# ):
#         total_categories = await db.scalar(
#         select(func.count())
#         .select_from(Category)
#         .where(Category.user_id == user_id)
#     )
#     total_tasks = await db.scalar(
#         select(func.count())
#         .select_from(Task)
#         .where(Task.user_id == user_id)
#     )
#     return {
#         "total_categories": total_categories,
#         "total_tasks": total_tasks
#     }
#     @staticmethod
#     async def category_task_count(
#         db: AsyncSession,
#         user_id
# ):

#         result = await db.execute(
#         select(
#             Category.name,
#             func.count(Task.id)
#         )
#         .join(
#             Task,
#             Category.id == Task.category_id
#         )
#         .where(
#             Category.user_id == user_id
#         )
#         .group_by(Category.name)
#     )
#     return [
#         {
#             "category": row[0],
#             "task_count": row[1]
#         }
#         for row in result.all()
#     ]
#     @staticmethod
#     async def most_used_category(
#         db: AsyncSession,
#         user_id
# ):

#         result = await db.execute(
#         select(
#             Category.name,
#             func.count(Task.id).label("total")
#         )
#         .join(
#             Task,
#             Category.id == Task.category_id
#         )
#         .where(
#             Category.user_id == user_id
#         )
#         .group_by(Category.name)
#         .order_by(func.count(Task.id).desc())
#         .limit(1)
#     )

#     row = result.first()

#     if row:
#         return {
#             "category": row[0],
#             "tasks": row[1]
#         }

#     return {
#         "category": None,
#         "tasks": 0
#     }

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.models import Category, Task
from app.schemas.category_schema import UpdateCategorySchema


class CategoryService:

    @staticmethod
    async def create_category(
        db: AsyncSession,
        user_id,
        payload
    ):
        category = Category(
            user_id=user_id,
            name=payload.name,
            color=payload.color
        )

        db.add(category)
        await db.commit()
        await db.refresh(category)

        return category

    @staticmethod
    async def update_category(
        db: AsyncSession,
        category: Category,
        payload: UpdateCategorySchema
    ):
        if payload.name is not None:
            category.name = payload.name

        if payload.color is not None:
            category.color = payload.color

        if payload.icon is not None:
            category.icon = payload.icon

        await db.commit()
        await db.refresh(category)

        return category

    @staticmethod
    async def delete_category(
        db: AsyncSession,
        category: Category
    ):
        await db.delete(category)
        await db.commit()

    @staticmethod
    async def search_categories(
        db: AsyncSession,
        user_id,
        keyword: str
    ):
        result = await db.execute(
            select(Category).where(
                Category.user_id == user_id,
                Category.name.ilike(f"%{keyword}%")
            )
        )

        return result.scalars().all()

    @staticmethod
    async def paginated_categories(
        db: AsyncSession,
        user_id,
        page: int,
        limit: int
    ):
        offset = (page - 1) * limit

        result = await db.execute(
            select(Category)
            .where(Category.user_id == user_id)
            .offset(offset)
            .limit(limit)
        )

        return result.scalars().all()

    @staticmethod
    async def dashboard(
        db: AsyncSession,
        user_id
    ):
        total_categories = await db.scalar(
            select(func.count())
            .select_from(Category)
            .where(Category.user_id == user_id)
        )

        total_tasks = await db.scalar(
            select(func.count())
            .select_from(Task)
            .where(Task.user_id == user_id)
        )

        return {
            "total_categories": total_categories,
            "total_tasks": total_tasks
        }

    @staticmethod
    async def category_task_count(
        db: AsyncSession,
        user_id
    ):
        result = await db.execute(
            select(
                Category.name,
                func.count(Task.id)
            )
            .join(
                Task,
                Category.id == Task.category_id
            )
            .where(
                Category.user_id == user_id
            )
            .group_by(Category.name)
        )

        return [
            {
                "category": row[0],
                "task_count": row[1]
            }
            for row in result.all()
        ]

    @staticmethod
    async def most_used_category(
        db: AsyncSession,
        user_id
    ):
        result = await db.execute(
            select(
                Category.name,
                func.count(Task.id).label("total")
            )
            .join(
                Task,
                Category.id == Task.category_id
            )
            .where(
                Category.user_id == user_id
            )
            .group_by(Category.name)
            .order_by(func.count(Task.id).desc())
            .limit(1)
        )

        row = result.first()

        if row:
            return {
                "category": row[0],
                "tasks": row[1]
            }

        return {
            "category": None,
            "tasks": 0
        }