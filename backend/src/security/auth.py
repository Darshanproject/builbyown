import datetime

import jwt
from passlib.context import CryptContext
from python_settings import settings

pwd_context = CryptContext(schemes=["argon2"],deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password: str):
    return pwd_context.verify(plain_password,hash_password)


def create_access_token(data: dict, expires_delta: int):
    to_encode = data.copy()
    expire = datetime.utcnow() + datetime.timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")