from fastapi import HTTPException
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.models.user import User
from app.services.otp_service import OTPService
from app.models.otp import OTP
from app.services.email_service import EmailService
from datetime import datetime, timedelta
from app.models.user import User
from app.core.security import (
    hash_password,
    verify_password
)


class AuthService:

    
    # @staticmethod
    # async def authenticate(
    #         db: AsyncSession,
    #         email: str,
    #         password: str
    # ):

    #     result = await db.execute(
    #         select(User).where(User.email == email)
    #     )

    #     user = result.scalar_one_or_none()

    #     if not user:
    #         return None

    #     if not verify_password(
    #             password,
    #             user.password_hash
    #     ):
    #         return None

    #     return user
    @staticmethod
    async def authenticate(
        db: AsyncSession,
        email: str,
        password: str
    ):
        print("=" * 50)
        print("EMAIL:", repr(email))
        print("PASSWORD:", password)

        result = await db.execute(
            select(User).where(User.email == email.strip())
        )

        user = result.scalar_one_or_none()

        print("USER:", user)

        if user is None:
            print("USER NOT FOUND")
            return None

        print("HASH:", user.password_hash)

        valid = verify_password(
            password,
            user.password_hash
        )

        print("VERIFY:", valid)

        if not valid:
            print("WRONG PASSWORD")
            return None

        print("LOGIN SUCCESS")
        return user

    @staticmethod
    async def reset_password(
        db,
        email,
        password
):

        result = await db.execute(
        select(User).where(
            User.email == email
        )
    )

        user = result.scalar_one()

        user.password_hash = hash_password(
        password
    )

        await db.commit()
        return user

    @staticmethod
    async def find_by_email(
            db,
            email: str
    ):
        result = await db.execute(
            select(User).where(User.email == email)
        )

        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_all_users(db):

        result = await db.execute(
        select(User)
    )

        return result.scalars().all()


    @staticmethod
    async def get_total_users(db):

        total = await db.scalar(
        select(func.count())
        .select_from(User)
    )

        return total
    @staticmethod
    async def register(
        db: AsyncSession,
        username: str,
        email: str,
        password: str
):

        result = await db.execute(
        select(User).where(User.email == email)
    )

        existing_user = result.scalar_one_or_none()

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already exists")

        user = User(
        username=username,
        email=email,
        password_hash=hash_password(password)
    )

        db.add(user)


        await db.flush()      # Generates UUID

        print(user.id) 
        otp = OTPService.generate()
        await EmailService.send_email(
    user.email,
    "OTP Verification",
    {
        "otp": otp
    },
    "otp.html"
)
        otp_record = OTP(
        user_id=user.id,
        code=otp,
        purpose="verify_email",
        expires_at=datetime.utcnow() + timedelta(minutes=5)
)
        
        db.add(otp_record)
        await EmailService.send_email(
    user.email,
    "Welcome to Todo Backend",
    {
        "username": user.username
    },
    "welcome.html"
)
        await db.commit()
        await db.refresh(user)
        return user