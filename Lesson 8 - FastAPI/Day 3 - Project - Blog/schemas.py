from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# POST Schemas
class PostCreate(BaseModel):
    title: str
    content: str
    
class PostRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    author_id: int
    
    class Config:
        orm_mode = True
        
# User Schemas
class UserCreate(BaseModel):
    username: str
    password: str
    
class UserRead(BaseModel):
    id: int
    username: str
    
    class Config:
        orm_mode = True