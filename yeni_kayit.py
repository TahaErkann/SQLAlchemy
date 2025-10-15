from db import Base, engine, SessionLocal
from models import User
from sqlalchemy.orm import sessionmaker, declarative_base

#Create the tables
Base.metadata.create_all(bind=engine)

#CRUD Examples
def create_user(username, email):
    session = SessionLocal()
    
    try:
        user = User(username=username, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        print("User created:", user.id, user.username)
        
    except Exception as e:
        session.rollback()
        print("Hata:", e)
    
    finally:
        session.close()

def get_users():
    session = SessionLocal()
    users = session.query(User).all()
    for u in users:
        print(u.id, u.username, u.email)
    session.close()
    
if __name__ == "__main__":
    create_user("mehmet","mehmet@hotmail.com")
    create_user("taha","taha@hotmail.com")
    create_user("ahmet","ahmet@hotmail.com")
    get_users()      