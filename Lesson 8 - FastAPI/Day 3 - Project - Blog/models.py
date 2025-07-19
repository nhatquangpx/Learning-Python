from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")
    author: Optional["User"] = Relationship(back_populates="posts")
    
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str
    
    posts: List[Post] = Relationship(back_populates="author")
    
# Giải thích:
# Relationships được sử dụng để kết nối các bảng với nhau.
# Ở đây, back_populates được sử dụng để xác định mối quan hệ hai chiều giữa User và Post.
# Optional dùng để chỉ ra rằng trường này có thể là None, tức là không bắt buộc phải có giá trị.
