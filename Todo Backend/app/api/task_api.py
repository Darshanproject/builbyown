# from asyncio import Task

# from fastapi import APIRouter, Depends
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.core.database import get_db
# from app.dependencies.authy_dependencies import get_current_user

# from app.schemas.task_schemas import CreateTaskSchema, UpdateTaskSchema

# from app.services.task_services import TaskService
# from sqlalchemy import select
# from app.models.task import Task
# from sqlalchemy import func

# router = APIRouter(
#     prefix="/tasks",
#     tags=["Tasks"]
# )


# @router.post("/")
# async def create_task(
#         payload: CreateTaskSchema,
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     return await TaskService.create_task(
#         db,
#         current_user.id,
#         payload
#     )

# @router.post("/")
# async def create_task(
#         payload: CreateTaskSchema,
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     return await TaskService.create_task(
#         db,
#         current_user.id,
#         payload
#     )
# @router.get("/")
# async def get_tasks(
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     return await TaskService.get_tasks(
#         db,
#         current_user.id
#     )

# @router.get("/{task_id}")
# async def get_task(
#         task_id: str,
#         db: AsyncSession = Depends(get_db)
# ):

#     task = await TaskService.get_task(
#         db,
#         task_id
#     )

#     return task
# @router.put("/{task_id}")
# async def update_task(
#         task_id: str,
#         payload: UpdateTaskSchema,
#         db: AsyncSession = Depends(get_db)
# ):

#     task = await TaskService.get_task(
#         db,
#         task_id
#     )

#     return await TaskService.update_task(
#         db,
#         task,
#         payload
#     )
# @router.delete("/{task_id}")
# async def delete_task(
#         task_id: str,
#         db: AsyncSession = Depends(get_db)
# ):

#     task = await TaskService.get_task(
#         db,
#         task_id
#     )

#     await TaskService.delete_task(
#         db,
#         task
#     )

#     return {
#         "message": "Task deleted successfully"
#     }


# @router.patch("/{task_id}/complete")
# async def complete_task(
#         task_id: str,
#         db: AsyncSession = Depends(get_db)
# ):

#     task = await TaskService.get_task(
#         db,
#         task_id
#     )

#     task.completed = True

#     await db.commit()

#     return task

# @router.patch("/{task_id}/important")
# async def important_task(
#         task_id: str,
#         db: AsyncSession = Depends(get_db)
# ):

#     task = await TaskService.get_task(
#         db,
#         task_id
#     )

#     task.is_important = True

#     await db.commit()

#     return task

# from datetime import date

# @router.get("/today/list")
# async def today_tasks(
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     result = await db.execute(
#         select(Task).where(
#             Task.user_id == current_user.id,
#             Task.due_date == date.today()
#         )
#     )

#     return result.scalars().all()

# from datetime import timedelta

# @router.get("/tomorrow/list")
# async def tomorrow_tasks(
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     tomorrow = date.today() + timedelta(days=1)

#     result = await db.execute(
#         select(Task).where(
#             Task.user_id == current_user.id,
#             Task.due_date == tomorrow
#         )
#     )

#     return result.scalars().all()

# @router.get("/important/list")
# async def important_tasks(
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     result = await db.execute(
#         select(Task).where(
#             Task.user_id == current_user.id,
#             Task.is_important == True
#         )
#     )

#     return result.scalars().all()

# @router.get("/completed/list")
# async def completed_tasks(
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     result = await db.execute(
#         select(Task).where(
#             Task.user_id == current_user.id,
#             Task.completed == True
#         )
#     )

#     return result.scalars().all()


# @router.get("/search")
# async def search_tasks(
#         keyword: str,
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     result = await db.execute(
#         select(Task).where(
#             Task.user_id == current_user.id,
#             Task.title.ilike(f"%{keyword}%")
#         )
#     )

#     return result.scalars().all()
# @router.get("/page")
# async def paginated_tasks(
#         page: int = 1,
#         limit: int = 10,
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     offset = (page - 1) * limit

#     result = await db.execute(
#         select(Task)
#         .where(Task.user_id == current_user.id)
#         .offset(offset)
#         .limit(limit)
#     )

#     return result.scalars().all()

# @router.get("/dashboard")
# async def dashboard(
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     total = await db.scalar(
#         select(func.count())
#         .select_from(Task)
#         .where(Task.user_id == current_user.id)
#     )

#     completed = await db.scalar(
#         select(func.count())
#         .select_from(Task)
#         .where(
#             Task.user_id == current_user.id,
#             Task.completed == True
#         )
#     )

#     important = await db.scalar(
#         select(func.count())
#         .select_from(Task)
#         .where(
#             Task.user_id == current_user.id,
#             Task.is_important == True
#         )
#     )

#     pending = total - completed

#     return {
#         "total_tasks": total,
#         "completed_tasks": completed,
#         "important_tasks": important,
#         "pending_tasks": pending
#     }


from genericpath import samefile
from uuid import UUID
from datetime import date, timedelta
from app.services.user_services import UserService  
from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.dependencies.authy_dependencies import get_current_user
from app.models.task import Task
from app.schemas.task_schemas import (
    AssignTaskSchema,
    CreateTaskSchema,
    UpdateTaskSchema
)
from app.services.task_services import TaskService
from app.services.activity_service import ActivityService
from app.services.notification_service import NotificationService


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# ---------------- CREATE TASK ----------------

@router.post("/")
async def create_task(
        payload: CreateTaskSchema,
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):
    await ActivityService.log(
    db,
    current_user.id,
    f'Created task "{payload.title}"'
)
    await NotificationService.create_notification(
    db,
    current_user.id,
    "Recurring Task Created",
    f"Next occurrence of '{Task.title}' has been scheduled."
)
    return await TaskService.create_task(
        db,
        current_user.id,
        payload
    )


# ---------------- ALL TASKS ----------------

@router.get("/")

# async def get_tasks(
#         db: AsyncSession = Depends(get_db),
#         current_user=Depends(get_current_user)
# ):

#     return await TaskService.get_tasks(
#         db,
#         current_user.id
#     )
async def get_tasks(
    date: date | None = Query(None),
    start_date: date | None = Query(None),
    end_date: date | None = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: Task.user_id = Depends(get_current_user), # type: ignore
):
    query = select(Task).where(
        Task.user_id == current_user.id
    )

    if date:
        query = query.where(
            Task.due_date == date
        )

    if start_date:
        query = query.where(
            Task.due_date >= start_date
        )

    if end_date:
        query = query.where(
            Task.due_date <= end_date
        )

    query = query.order_by(
        Task.due_date.asc()
    )

    result = await db.execute(query)

    tasks = result.scalars().all()

    return tasks

# ---------------- SEARCH ----------------

@router.get("/search")
async def search_tasks(
        keyword: str,
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    result = await db.execute(
        select(Task).where(
            Task.user_id == current_user.id,
            Task.title.ilike(f"%{keyword}%")
        )
    )

    return result.scalars().all()


# ---------------- PAGINATION ----------------

@router.get("/page")
async def paginated_tasks(
        page: int = 1,
        limit: int = 10,
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    offset = (page - 1) * limit

    result = await db.execute(
        select(Task)
        .where(Task.user_id == current_user.id)
        .offset(offset)
        .limit(limit)
    )

    return result.scalars().all()


# ---------------- TODAY ----------------

@router.get("/today/list")
async def today_tasks(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    result = await db.execute(
        select(Task).where(
            Task.user_id == current_user.id,
            Task.due_date == date.today()
        )
    )

    return result.scalars().all()


# ---------------- TOMORROW ----------------

@router.get("/tomorrow/list")
async def tomorrow_tasks(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    tomorrow = date.today() + timedelta(days=1)

    result = await db.execute(
        select(Task).where(
            Task.user_id == current_user.id,
            Task.due_date == tomorrow
        )
    )

    return result.scalars().all()


# ---------------- IMPORTANT ----------------

@router.get("/important/list")
async def important_tasks(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    result = await db.execute(
        select(Task).where(
            Task.user_id == current_user.id,
            Task.is_important == True
        )
    )

    return result.scalars().all()


# ---------------- COMPLETED ----------------

@router.get("/completed/list")
async def completed_tasks(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    result = await db.execute(
        select(Task).where(
            Task.user_id == current_user.id,
            Task.completed == True
        )
    )

    return result.scalars().all()


# ---------------- DASHBOARD ----------------

@router.get("/dashboard")
async def dashboard(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    total = await db.scalar(
        select(func.count())
        .select_from(Task)
        .where(Task.user_id == current_user.id)
    )

    completed = await db.scalar(
        select(func.count())
        .select_from(Task)
        .where(
            Task.user_id == current_user.id,
            Task.completed == True
        )
    )

    important = await db.scalar(
        select(func.count())
        .select_from(Task)
        .where(
            Task.user_id == current_user.id,
            Task.is_important == True
        )
    )

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "important_tasks": important,
        "pending_tasks": total - completed
    }


# ---------------- GET SINGLE TASK ----------------

@router.get("/{task_id}")
async def get_task(
        task_id: UUID,
        db: AsyncSession = Depends(get_db)
):

    return await TaskService.get_task(
        db,
        task_id
    )


# ---------------- UPDATE TASK ----------------

# @router.put("/{task_id}")
# async def update_task(
#         task_id: UUID,
#         payload: UpdateTaskSchema,
#         db: AsyncSession = Depends(get_db)
# ):
#     await ActivityService.log(
#     db,
#     task.user_id,
#     f'Updated task "{task.title}"'
# )
#     task = await TaskService.get_task(
#         db,
#         task_id
#     )

#     return await TaskService.update_task(
#         db,
#         task,
#         payload
#     )

@router.put("/{task_id}")
async def update_task(
    task_id: UUID,
    payload: UpdateTaskSchema,
    db: AsyncSession = Depends(get_db)
):
    task = await TaskService.get_task(
        db,
        task_id
    )

    await ActivityService.log(
        db,
        task.user_id,
        f'Updated task "{task.title}"'
    )

    return await TaskService.update_task(
        db,
        task,
        payload
    )

# ---------------- DELETE TASK ----------------

# @router.delete("/{task_id}")
# async def delete_task(
#         task_id: UUID,
#         db: AsyncSession = Depends(get_db)
# ):
#     await ActivityService.log(
#     db,
#     task.user_id,
#     f'Deleted task "{task.title}"'
# )
#     task = await TaskService.get_task(
#         db,
#         task_id
#     )

#     await TaskService.delete_task(
#         db,
#         task
#     )

#     return {
#         "message": "Task deleted successfully"
#     }
@router.delete("/{task_id}")
async def delete_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    task = await TaskService.get_task(
        db,
        task_id
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    await ActivityService.log(
        db,
        task.user_id,
        f'Deleted task "{task.title}"'
    )

    return await TaskService.delete_task(
        db,
        task
    )

# ---------------- COMPLETE TASK ----------------

@router.patch("/{task_id}/complete")
async def complete_task(
        task_id: UUID,
        db: AsyncSession = Depends(get_db)
):

    task = await TaskService.get_task(
        db,
        task_id
    )

    task.completed = True

    await db.commit()

    await db.refresh(task)

    return task


# ---------------- IMPORTANT TASK ----------------

@router.patch("/{task_id}/important")
async def important_task(
        task_id: UUID,
        db: AsyncSession = Depends(get_db)
):

    task = await TaskService.get_task(
        db,
        task_id
    )

    task.is_important = True

    await db.commit()

    await db.refresh(task)

    return task

@router.get("/recurring")
async def recurring_tasks(
        db: AsyncSession = Depends(get_db),
        current_user=Depends(get_current_user)
):

    result = await db.execute(
        select(Task).where(
            Task.user_id == current_user.id,
            Task.is_recurring == True
        )
    )

    return result.scalars().all()
@router.post("/task/{task_id}")
async def upload_task_attachment(
        task_id: str,
        file: UploadFile = File(...),
        db: AsyncSession = Depends(get_db)
):

    task = await TaskService.get_task(
        db,
        task_id
    )

    path = await samefile(
        file,
        "tasks"
    )

    task.attachment_url = path

    await db.commit()

    return task
# @router.patch("/{task_id}/assign")
# async def assign_task(
#     task_id: UUID,
#     payload: AssignTaskSchema,
#     db: AsyncSession = Depends(get_db),
#     current_user=Depends(get_current_user)
# ):

#     task = await TaskService.get_task(
#         db,
#         task_id
#     )

#     user = await UserService.get_user(
#         db,
#         payload.user_id
#     )

#     return await TaskService.assign_task(
#         db,
#         task,
#         current_user,
#         user
#     )
@router.patch("/{task_id}/assign")
async def assign_task(
    task_id: UUID,
    payload: AssignTaskSchema,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task = await TaskService.get_task(
        db,
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    assigned_user = await UserService.get_user(
        db,
        payload.user_id
    )

    if not assigned_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return await TaskService.assign_task(
        db,
        task,
        current_user,
        assigned_user
    )