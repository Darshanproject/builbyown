from datetime import datetime, timedelta
import bcrypt
from jose import JWTError, jwt
# from passlib.context import CryptContext

from app.core.config import settings

# pwd_context = CryptContext(
#     schemes=["bcrypt"],
#     deprecated="auto"
# )


# def hash_password(password: str):
#      print(password)
#      print(type(password))
#      return pwd_context.hash(password)
def hash_password(password: str):
    print(password)
    print(type(password))
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        salt
    )
    return hashed.decode("utf-8")


# def verify_password(
#         plain_password: str,
#         hashed_password: str
# ):
#     return pwd_context.verify(
#         plain_password,
#         hashed_password
#     )
def verify_password(
        plain_password: str,
        hashed_password: str
):
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def create_access_token(data: dict):
    payload = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def create_refresh_token(data: dict):
    payload = data.copy()

    expire = datetime.utcnow() + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
def create_reset_token(data: dict):

    payload = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=15)

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
def verify_reset_token(token: str):

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        return payload

    except JWTError:
        return None
    
  
# def reset_password(
#     db,
#     token,
#     new_password
# ):
#      payload = verify_reset_token(token)

#      if payload is None:
#         raise Exception("Invalid token")

#      user_id = payload["sub"]

#      user =  UserService.get_user(
#         db,
#         user_id
#     )

#      user.password_hash = hash_password(new_password)

#      await db.commit()

#      return {
#         "message":"Password Updated Successfully"
#     }