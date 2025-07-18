from typing import Optional
from sqlmodel import SQLModel, Field 
class Note(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str

# Giải thích:
# SQLModel là sự kết hợp giữa Pydantic và SQLAlchemy
# SQLModel giúp định nghĩa mô hình dữ liệu với các tính năng của ORM.
# class Note định nghĩa một bảng trong cơ sở dữ liệu với các trường id, title, content.
# table=True chỉ ra rằng đây là một bảng trong cơ sở dữ liệu.
# Field() xác định các field đặc biệt: primary key, default