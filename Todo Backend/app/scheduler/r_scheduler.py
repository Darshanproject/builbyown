from datetime import timedelta
from dateutil.relativedelta import relativedelta
from sqlalchemy import select

from app.models.task import Task


def get_next_date(task):

    if task.recurring_type == "daily":
        return task.due_date + timedelta(days=1)

    if task.recurring_type == "weekly":
        return task.due_date + timedelta(days=7)

    if task.recurring_type == "monthly":
        return task.due_date + relativedelta(months=1)

    if task.recurring_type == "yearly":
        return task.due_date + relativedelta(years=1)

    return None
async def recurring_job(db):

    result = await db.execute(
        select(Task).where(
    Task.completed == True,
    Task.is_recurring == True,
    Task.recurring_generated == False
)
    )

    tasks = result.scalars().all()

    for task in tasks:

        next_date = get_next_date(task)

        new_task = Task(
            user_id=task.user_id,
            category_id=task.category_id,
            title=task.title,
            description=task.description,
            priority=task.priority,
            due_date=next_date,
            due_time=task.due_time,
            is_recurring=True,
            recurring_type=task.recurring_type
        )

        db.add(new_task)

        task.completed = False

    await db.commit()