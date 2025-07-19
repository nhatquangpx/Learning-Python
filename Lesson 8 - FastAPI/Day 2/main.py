# Tạo route đăng ký/đăng nhập:
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from models import User
from auth import get_password_hash, authenticate_user, create_access_token, get_current_user
from auth import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm
from database import engine, create_db_and_tables
from datetime import timedelta

app = FastAPI()
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
@app.post("/register")
def register_user(user: User):
    with Session(engine) as session:
        existing_user = session.exec(select(User).where(User.username == user.username)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        
        user.hashed_password = get_password_hash(user.hashed_password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"measage": "User registered successfully", "user_id": user.id}
    
@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token({"sub": user.username}, access_token_expires)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return current_user