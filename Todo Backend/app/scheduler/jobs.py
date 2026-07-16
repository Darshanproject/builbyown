from app.core.database import AsyncSessionLocal
from app.scheduler.r_scheduler import recurring_job


async def recurring_task_job():

    async with AsyncSessionLocal() as db:

        await recurring_job(db)