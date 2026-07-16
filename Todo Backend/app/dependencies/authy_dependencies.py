import uuid

from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.models.user import User

from sqlalchemy import select

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


# async def get_current_user(
#         token: str = Depends(oauth2_scheme),
#         db: AsyncSession = Depends(get_db)
# ):

#     try:
#         payload = jwt.decode(
#             token,
#             settings.SECRET_KEY,
#             algorithms=[settings.ALGORITHM]
#         )
#         print("****************************************")
#         print(payload)
#         print(payload.get("sub"))
#         user_id = payload.get("sub")

#         result = await db.execute(
#             select(User).where(User.id == user_id)
#         )

#         user = result.scalar_one_or_none()

#         if not user:
#             raise HTTPException(
#                 status_code=401,
#                 detail="Invalid token"
#             )

#         return user

#     except JWTError:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid token"
#         )

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    print("TOKEN:", token)

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        print("PAYLOAD:", payload)

        user_id = payload.get("sub")
        print("USER ID:", user_id)

        user_id = uuid.UUID(user_id)

        result = await db.execute(
            select(User).where(User.id == user_id)
        )

        user = result.scalar_one_or_none()

        print("USER:", user)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return user

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )