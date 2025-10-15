from models import session, User
from db import Base, engine, SessionLocal
from sqlalchemy.orm import sessionmaker, declarative_base

#Users To Be Deleted

user_id = 1

user_to_delete = session.query(User).filter_by(id=user_id).first()

#Check if user exists

if user_to_delete:
    print(f"Siliniyor: {user_to_delete.username} ({user_to_delete.email})")
    session.delete(user_to_delete)
    session.commit()
    print("Kullanıcı silindi!")
else:
    print("Belirtilen kullanıcı bulunamadı.")
    