from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import User, session

app = FastAPI()

#---Şema Tanımları---
class UserSchema(BaseModel):
    username : str
    email : str
    

@app.post("/users")
def create_user(user: UserSchema):
    new_user = User(username=user.username, email=user.email)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message":"Kullanıcı oluşturuldu.", "user_id": new_user.id }

@app.get("/users")
def get_users():
    users=session.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
    return [{"id": u.id, "username": u.username, "email": u.email} for u in users]
