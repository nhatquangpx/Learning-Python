from sqlmodel import SQLModel, Field
from typing import Optional # Thư viện này cung cấp kiểu dữ liệu Optional, ví dụ như Optional[str] có nghĩa là giá trị có thể là chuỗi hoặc None
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str 
    hashed_password: str
    
class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    author_id: int
    created_at: datetime 

# Giải thích tại sao id lai là Optional[int]:
# Trong SQLModel, khi bạn định nghĩa một trường với kiểu dữ liệu là Optional[int], điều này có nghĩa là trường đó có thể chứa giá trị là một số nguyên (int) hoặc có thể không có giá trị nào (None).
# Điều này thường được sử dụng cho các trường khóa chính (primary key) trong cơ sở dữ liệu, nơi mà giá trị của khóa chính có thể được tự động tạo ra bởi cơ sở dữ liệu khi một bản ghi mới được chèn vào.   
# Khi bạn tạo một đối tượng User hoặc Post mới mà không cung cấp giá trị cho trường id, SQLModel sẽ tự động gán giá trị None cho trường này. 
# Khi bản ghi được lưu vào cơ sở dữ liệu, cơ sở dữ liệu sẽ tự động tạo ra một giá trị duy nhất cho trường id và cập nhật lại đối tượng với giá trị này.