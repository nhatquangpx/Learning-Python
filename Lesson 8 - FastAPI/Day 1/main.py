# Trước khi chạy, cần tạo môi trường ảo:
# Trong trường hợp này, ta tạo môi trường ảo tại thư mục venv:
# python -m venv venv
# Sau đó kích hoạt môi trường ảo:
# Windows: venv\Scripts\activate
# Sau đó cài đặt FastAPI và Uvicorn:
# pip install fastapi uvicorn
# Chạy ứng dụng FastAPI:
# uvicorn main:app --reload

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Welcome to FastAPI!"}

# Giải thích:
# FastAPI() là khởi tạo app backend.
# @app.get("/"): định nghĩa route GET tại /
# Hàm read_root() chạy khi người dùng truy cập /
# Trả về dữ liệu dạng dictionary (sẽ được tự động chuyển thành JSON)
# Swagger UI và ReDoc UI sẽ tự động sinh ra từ các route đã định nghĩa.
# --reload tự động restart server khi có thay đổi trong source code.

# Truy cập: 
# http://127.0.0.1:8000	Kết quả JSON trả về từ route /
# http://127.0.0.1:8000/docs	Swagger UI tự sinh
# http://127.0.0.1:8000/redoc	ReDoc UI tự sinh