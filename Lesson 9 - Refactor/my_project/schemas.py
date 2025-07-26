from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    
class UserRead(BaseModel):
    id: int
    username: str
    
class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int