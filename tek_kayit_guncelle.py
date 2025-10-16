from models import User, session
from sqlalchemy.orm import sessionmaker, declarative_base
from db import Base, engine, SessionLocal

#User to be updated
user_id=2

#New details
new_username="hakan"
new_email="hakan@hotmail.com"

user_to_update = session.query(User).filter_by(id=user_id).first()

if user_to_update:
    print(f"Güncelleniyor: {user_to_update.username} ({user_to_update.email})")

    user_to_update.username = new_username
    user_to_update.email = new_email
    
    session.commit()
    print(f"Güncellendi: {user_to_update.username} ({user_to_update.email})")
    
else:
    print("Belirtilen kullanıcı bulunamadı.")
    