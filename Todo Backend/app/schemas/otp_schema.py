from pydantic import BaseModel, EmailStr


class VerifyOTPSchema(BaseModel):
    email: EmailStr
    otp: str


class ForgotPasswordSchema(BaseModel):
    email: EmailStr


class ResetPasswordSchema(BaseModel):
    email: EmailStr
    otp: str
    password: str