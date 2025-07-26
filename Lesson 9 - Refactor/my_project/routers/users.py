from fastapi import APIRouter, Depends, HTTPException
from my_project.schemas import UserCreate, UserRead
from my_project.services import user_service
from my_project.models import User
from my_project.utils.auth import get_current_user
from sqlmodel import Session
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserRead)
def register(user: UserCreate):
    return user_service.register_user(user)

@router.get("/me", response_model=UserRead)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/", response_model=List[UserRead])
def get_all_users():
    return user_service.get_all_users()
