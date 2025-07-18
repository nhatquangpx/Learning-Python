from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./notes.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Giải thích:
# - create_engine tạo kết nối đến cơ sở dữ liệu SQLite.
# - echo=True để in ra các câu lệnh SQL được thực thi, giúp ta quan sát được khi đang chạy.
# - create_db_and_tables tạo các bảng trong cơ sở dữ liệu dựa trên mô hình đã định nghĩa.
# - SQLite sẽ tạo file notes.db trong thư mục hiện tại nếu nó chưa tồn tại.
