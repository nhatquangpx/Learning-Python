# Request body
# Dữ liệu do client gửi đến server, dạng JSON, chứa nhiều field
# Thường dùng trong POST, PUT, PATCH để tạo hoặc cập nhật tài nguyên.

from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

# Giải thích:
# Item là một schema định nghĩa cấu trúc dữ liệu.
# BaseModel từ Pydantic giúp xác thực và chuyển đổi dữ liệu.
# Khi client gửi dữ liệu JSON, FastAPI sẽ:
# - Parse dữ liệu JSON thành đối tượng Item trong Python
# - Validate field có đúng kiểu dữ liệu không
# - Trả về dữ liệu đã được xác thực trong response
# - Trả lỗi 422 nếu sai định dạng hoặc thiếu field bắt buộc

# Kết hợp path parameters và request body:
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"id": item_id, "item": item}
