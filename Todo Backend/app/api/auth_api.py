from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.auth_schema import ForgotPasswordSchema, RegisterSchema, LoginSchema, ResetPasswordSchema
from app.services.auth_services import AuthService
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth_schema import RefreshTokenSchema
from app.services.activity_service import ActivityService
from app.services.email_service import EmailService


from app.core.security import (
    create_access_token,
    create_refresh_token,
    create_reset_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
async def register(
        payload: RegisterSchema,
        db: AsyncSession = Depends(get_db)
):

    user = await AuthService.register(
        db,
        payload.username,
        payload.email,
        payload.password
    )
    await ActivityService.log(
    db,
    user.id,
    "Account Created"
)

    access_token = create_access_token(
        {"sub": str(user.id)}
    )

    refresh_token = create_refresh_token(
        {"sub": str(user.id)}
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

# @router.post("/login")
# async def login(
#         payload: LoginSchema,
#         db: AsyncSession = Depends(get_db)
# ):
#     print(payload)
#     user = await AuthService.authenticate(
#         db,
#         payload.email,
#         payload.password
#     )

#     if not user:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid credentials"
#         )

#     return {
#         "access_token": create_access_token(
#             {"sub": str(user.id)}
#         ),
#         "refresh_token": create_refresh_token(
#             {"sub": str(user.id)}
#         )
#     }


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await AuthService.authenticate(
        db,
        form_data.username,
        form_data.password
    )
    print("=" * 50)
    print("USERNAME:", form_data.username)
    print("PASSWORD:", form_data.password)
    print("=" * 50)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    user_id = str(user.id)

    await ActivityService.log(
        db,
        user.id,
        "Logged In"
    )

    return {
        "access_token": create_access_token(
            {"sub": user_id}
        ),
        "refresh_token": create_refresh_token(
            {"sub": user_id}
        ),
        "token_type": "bearer"
    }

@router.post("/refresh")
async def refresh_token(
        payload: RefreshTokenSchema
):

    access_token = create_access_token(
        {
            "sub": "user_id"
        }
    )

    return {
        "access_token": access_token
    }


@router.post("/forgot-password")
async def forgot_password(
        payload: ForgotPasswordSchema,
        db: AsyncSession = Depends(get_db)
):

    user = await AuthService.find_by_email(
        db,
        payload.email
    )
    reset_token = create_reset_token(
    {
        "sub": str(user.id)
    }
)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    reset_link = reset_token
    await EmailService.send_email(
    user.email,
    "Reset Password",
    {
        "reset_link": reset_link
    },
    "reset_password.html"
)
    await EmailService.send_email(
    user.email,
    "Reset Password",
    {
        "reset_link": reset_link
    },
    "reset_password.html"
)
    return {
        "message": f"http://localhost:3000/reset-password?token={reset_token}"
    }

@router.post("/reset-password")
async def reset_password(
        payload: ResetPasswordSchema,
        db: AsyncSession = Depends(get_db)
):

    await AuthService.reset_password(
        db,
        payload.email,
        payload.new_password
    )

    return {
        "message": "Password updated"
    }

@router.patch("/verify")
async def verify_email(
        current_user=Depends(AuthService),
        db: AsyncSession = Depends(get_db)
):

    current_user.is_verified = True

    await db.commit()

    return {
        "message": "Verified"
    }