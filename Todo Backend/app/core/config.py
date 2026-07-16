from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 6589

    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    REDIS_URL: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str

    MAIL_PORT: int
    MAIL_SERVER: str

    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool

    OTP_EXPIRE_MINUTES: int = 5

    class Config:
        env_file = ".env"


settings = Settings()