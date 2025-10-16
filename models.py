from sqlalchemy import Column, Integer, String, DateTime, func, create_engine
from db import Base
from sqlalchemy.orm import declarative_base,sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
#PostgreSQL connection string
DATABASE_URL = "postgresql+psycopg://local:pssw@localhost:5432/db"   

engine = create_engine(DATABASE_URL)

sessionLocal=sessionmaker(bind=engine)

session = sessionLocal()

Base.metadata.create_all(bind=engine)