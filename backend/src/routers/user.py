from fastapi import APIRouter, Depends
from python_settings import settings
from requests import Session
from src.security import auth
from src.schemas.user import UserCreate
from src.models.user import UserModel 
from src.database import get_db,SessionLocal
from src.security.auth import hash_password, verify_password

router =  APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
async def register_user(user: UserCreate,db = Depends(get_db)):
    # Implementation for saving user to database would go here
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user:
        return {"message": "User already exists"}
    # Save the new user to the database
    # new_user = UserModel(username=user.username, password=user.password)
    new_user = UserModel(username=user.username,password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

@router.post("/login")
async def user_login(
    user: UserCreate,
    db: Session = Depends(get_db)   # ✅ FIX
):
    try:
     existing_user = db.query(UserModel).filter(
        UserModel.username == user.username,
        UserModel.password == user.password
    ).first()
    #  if existing_user:
    #     if verify_password == True:
    #         return {"message": "Login Successfull"}
    
    #  elif(verify_password == False):
    #     return {"message":"Wrong Password"}
    #  else:
    #     return {"message":"No user exist"}
    # 
     if existing_user:
        if verify_password == True:
            token = auth.create_access_token(data={"sub": existing_user.username}, expires_delta=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            return {"message": "Login Successfull", "token": token}

     elif(verify_password == False):
        token = auth.create_access_token(data={"sub": existing_user.username}, expires_delta=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return {"message":"Wrong Password"}

     else:
        return {"message":"No user exist"}
    except Exception as e:
       return {f"Error:{e}"}


@router.get("/all-users")
async def getall_users(db= get_db):
    users = db.query(users).all()
    # db.add(users)
    # db.commit()
    # db.refresh()
    return users