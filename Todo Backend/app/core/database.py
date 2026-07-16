from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.core.config import settings


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True
)
print(settings.DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db