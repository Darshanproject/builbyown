from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.websocket.connection_manager import manager
from app.models.task import Task
from app.services.notification_service import NotificationService

class TaskService:

    @staticmethod
    async def create_task(
        db: AsyncSession,
        user_id,
        payload
):

        task = Task(
        user_id=user_id,
        category_id=payload.category_id,
        title=payload.title,
        description=payload.description,
        due_date=payload.due_date,
        due_time=payload.due_time,
        priority=payload.priority,
        is_recurring=payload.is_recurring,
        recurring_type=payload.recurring_type
)
        db.add(task)
        await db.commit()
        await manager.send_personal_message(
    str(task.user_id),
    {
        "type": "task_created",
        "title": task.title,
        "message": "Task created successfully"
    }
)
        await db.refresh(task)
        return task

    @staticmethod
    async def get_tasks(
            db: AsyncSession,
            user_id
    ):

        result = await db.execute(
            select(Task)
            .where(Task.user_id == user_id)
        )

        return result.scalars().all()
    

    @staticmethod
    async def get_task(
        db: AsyncSession,
        task_id
):

     result = await db.execute(
        select(Task).where(Task.id == task_id)
    )

     return result.scalar_one_or_none()
    
    @staticmethod
    async def update_task(
        db: AsyncSession,
        task,
        payload
):

     data = payload.model_dump(exclude_unset=True)

     for key, value in data.items():
        setattr(task, key, value)

     await db.commit()

     await db.refresh(task)
     await NotificationService.create_notification(
    db,
    task.user_id,
    "Task Updated",
    f"{task.title} updated."
)

     return task
    
    @staticmethod
    async def delete_task(
        db: AsyncSession,
        task
):

     await db.delete(task)

     await db.commit()
     await db.refresh(task)
     await NotificationService.create_notification(
    db,
    task.user_id,
    "Task Deleted",
    f"{task.title} deleted."
)
     return {"message": "Task deleted successfully"}
    
    @staticmethod
    async def completed_task(
        db: AsyncSession,
        task
):
     task.is_completed = True
     await db.add(task)

     await db.commit()
     await db.refresh(task)
     await NotificationService.create_notification(
    db,
    task.user_id,
    "Task Completed",
    f"{task.title} marked as completed."
)
     return {"message": "Task marked as completed successfully"}
    
    @staticmethod
    async def assign_task(
    db,
    task,
    current_user,
    assigned_user
):

     task.assigned_to = assigned_user.id
     task.assigned_by = current_user.id

     await db.commit()
     await db.refresh(task)

     return task