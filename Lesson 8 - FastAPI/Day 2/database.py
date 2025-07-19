from sqlmodel import SQLModel, creat_engine

DATABASE_URL = "sqlite:///./user.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)