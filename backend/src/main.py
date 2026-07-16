from fastapi import FastAPI
from src.models.task import TaskModel
from src.routers import task,user
from src.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(task.router)
app.include_router(user.router)