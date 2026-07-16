# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from .security import config
# from sqlalchemy.orm import sessionmaker,declarative_base

# engine = create_engine(config.settings.DATABASE_URL)
# session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:darshan123@localhost:5432/taskdb"  # or PostgreSQL later

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()