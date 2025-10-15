from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#PostgreSQL connection string
DATABASE_URL = "postgresql+psycopg://tahaerkan34:12345@localhost:5432/alchemy_db"

# Create Engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# ORM Base Class
Base = declarative_base()

# Session Factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
