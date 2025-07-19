from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from auth import get_password_hash, authenticate_user, create_access_token, get_current_user
from auth import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm
from database import engine, create_db_and_tables
from datetime import timedelta
from auth import get_current_user
from models import User, Post

app = FastAPI()

@app.on_event("startup")
def on_strartup():
    create_db_and_tables()
  
# Tạo route đăng ký/đăng nhập:
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

@app.post("/posts/")
def create_post(post: Post, current_user: User = Depends(get_current_user)):
    post.author_id = current_user.id
    with Session(engine) as session:
        session.add(post)
        session.commit()
        session.refresh(post)
        return post

@app.get("/posts/")
def get_all_posts():
    with Session(engine) as session:
        return session.exec(select(Post)).all()

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

@app.put("/posts/{post_id}")
def update_post(post_id: int, updated: Post, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        if not post or post.author_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
        post.title = updated.title
        post.content = updated.content
        session.add(post)
        session.commit()
        session.refresh(post)
        return post

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        if not post or post.author_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
        session.delete(post)
        session.commit()
        return {"deleted": True}