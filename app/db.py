from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./tienda.db"

engine = create_engine(DATABASE_URL, echo=True)

def crear_db():
    SQLModel.metadata.create_all(engine)
