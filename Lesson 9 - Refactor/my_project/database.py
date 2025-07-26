from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
# engine là một đối tượng kết nối đến cơ sở dữ liệu, trong trường hợp này là SQLite.
# create_db_and_tables là một hàm để tạo cơ sở dữ liệu và các bảng dựa trên các mô hình đã định nghĩa trong SQLModel.
# create_all(engine) sẽ tạo tất cả các bảng trong cơ sở dữ liệu dựa trên các mô hình đã được định nghĩa trong models.py