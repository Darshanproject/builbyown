from unittest import result

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.models.user import User
from app.models.otp import OTP
from datetime import datetime
from app.schemas.otp_schema import VerifyOTPSchema

router = APIRouter(
    prefix="/otp",
    tags=["OTP"]
)

@router.post("/verify-email")
async def verify_email(
        payload: VerifyOTPSchema,
        db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
    select(User).where(User.email == payload.email)
)

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
        status_code=404,
        detail="User not found"
    )
    otp = await db.execute(
        select(OTP).where(
            OTP.user_id == user.id,
            OTP.code == payload.otp
        )
    )
    otp = otp.scalar_one_or_none()
    if not otp:
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP"
        )

    if otp.expires_at < datetime.utcnow():
        raise HTTPException(
        status_code=400,
        detail="OTP Expired"
    )
    user.is_verified = True

    otp.is_used = True

    await db.commit()
    return {
    "message": "Email verified successfully"
}