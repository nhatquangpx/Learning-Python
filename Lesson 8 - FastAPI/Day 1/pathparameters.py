# Path parameteres in FastAPI
# Là dữ liệu trực tiếp trong URL, thường dùng để xác định tài nguyên cụ thể.
# Ví dụ: chỉ định ID, tên, slug, v.v.
from fastapi import FastAPI
app = FastAPI()
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Giải thích:
# item_id là tham số đường dẫn (path parameter).
# FastAPI tự động chuyển đổi item_id sang kiểu int.
# Ví dụ: Khi truy cập /items/5, hàm read_item sẽ nhận item_id là 5.