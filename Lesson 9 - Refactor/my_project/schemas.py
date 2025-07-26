from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    
class UserRead(BaseModel):
    id: int
    username: str
    
    class Config:
        from_attributes = True
    
class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int
    
class PostRead(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True   # Tương đương "orm_mode=True" trong Pydantic, cho phép chuyển đổi từ mô hình SQLModel sang Pydantic