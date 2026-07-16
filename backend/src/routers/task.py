# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# from src.models.task import TaskModel
# from ..schemas import task
# from ..database import session

# router = APIRouter(prefix="/tasks", tags=["tasks"])


# def get_db():
#     db = session()
#     try:
#         yield db
#     finally:
#         db.close()


# # @router.post("/create-task")
# # def create_task(task: task.Task):

# #     return {"message": "Task created successfully", "task": task}
# @router.post("/create-task")
# def create_task(task: task.Task, db: Session = Depends(get_db)):
#     new_task = TaskModel(title=task.title)
#     db.add(new_task)
#     db.commit()
#     db.refresh(new_task)

#     return {
#         "message": "Task created successfully",
#         "task": new_task
#     }


# @router.get("/get-tasks")
# def get_tasks(db: Session = Depends(get_db)):
#     try:
#         tasks = db.query(TaskModel).all()
#         return tasks
#     except Exception as e:
#         print(f"Error occurred while fetching tasks: {e}")
#         return []

# @router.get("/get-task/{task_id}")
# def get_task(task_id: int, db: Session = Depends(get_db)):
#     try:
#         task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
#         return task
#     except Exception as e:
#         print(f"Error occurred while fetching task: {e}")
#         return None

# @router.put("/update-task/{task_id}")
# def update_task(task_id: int, task: task.Task, db: Session = Depends(get_db)):
#     try:
#         existing_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
#         if not existing_task:
#             return {"message": "Task not found"}

#         existing_task.title = task.title
#         existing_task.description = task.description
#         existing_task.completed = task.completed

#         db.commit()
#         db.refresh(existing_task)

#         return {
#             "message": "Task updated successfully",
#             "task": existing_task
#         }
#     except Exception as e:
#         print(f"Error occurred while updating task: {e}")
#         return {"message": "Error updating task"}

# @router.delete("/delete-task/{task_id}")
# def delete_task(task_id: int, db: Session = Depends(get_db)):
#     existing_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
#     if not existing_task:
#         return {"message": "Task not found"}

#     db.delete(existing_task)
#     db.commit()

#     return {"message": "Task deleted successfully"}


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.models.task import TaskModel
from src.schemas.task import Task, TaskResponse
from src.database import SessionLocal,get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])


# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# ✅ CREATE TASK
@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: Task, db: Session = Depends(get_db)):
    new_task = TaskModel(**task.model_dump())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# ✅ GET ALL TASKS
@router.get("/", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(TaskModel).all()


# ✅ GET SINGLE TASK
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# ✅ UPDATE TASK
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: Task, db: Session = Depends(get_db)):
    existing_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in task.model_dump().items():
        setattr(existing_task, key, value)

    db.commit()
    db.refresh(existing_task)

    return existing_task


# ✅ DELETE TASK
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return