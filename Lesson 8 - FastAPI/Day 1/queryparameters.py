# Query parameters in FastAPI
# Là các cặp key-value được gửi trong URL đằng sau dấu hỏi chấm (?).
# Dùng trong GET, search, lọc, phân trang, v.v.
from fastapi import FastAPI
app = FastAPI()
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Giải thích:
# skip và limit là tham số truy vấn (query parameters).
# Có thể đặt giá trị mặc định cho chúng

