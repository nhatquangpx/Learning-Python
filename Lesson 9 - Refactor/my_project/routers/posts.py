from fastapi import APIRouter, Depends, HTTPException
from my_project.schemas import PostCreate, PostRead
from my_project.services import post_service
from my_project.models import User
from my_project.utils.auth import get_current_user
from typing import List

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/")
def create(
    post: PostCreate, 
    curent_user: User = Depends(get_current_user)
):
    return post_service.create_post(post, curent_user)

@router.get("/", response_model=List[PostRead])
def get_all_posts():
    return post_service.get_all_posts()

@router.get("/mine", response_model=List[PostRead])
def get_my_posts(current_user: User = Depends(get_current_user)):
    return post_service.get_user_posts(current_user)

# Hàm Depends(get_current_user) sẽ đảm bảo rằng người dùng đã đăng nhập trước khi thực hiện các thao tác liên quan đến bài viết.
# Nếu người dùng chưa đăng nhập, hàm get_current_user sẽ ném ra một HTTPException với mã lỗi 401 (Unauthorized).
