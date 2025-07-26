from my_project.models import User
from my_project.database import engine
from sqlmodel import Session, select
from my_project.utils.security import get_password_hash
from my_project.schemas import UserCreate
from fastapi import HTTPException

def register_user(user_data: UserCreate):
    with Session(engine) as session:
        existing_user = session.exec(select(User).where(User.usernam == user_data.username)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        user = User(
            username=user_data.username,
            hashed_password=get_password_hash(user_data.password),
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
def get_all_users():
    with Session(engine) as session:
        return session.exec(select(User)).all()