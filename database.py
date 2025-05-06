from sqlmodel import SQLModel, create_engine, Session
from models import Tarea

DATABASE_URL = "sqlite:///./tareas.db"  # o usa PostgreSQL si Render lo requiere

engine = create_engine(DATABASE_URL, echo=True)

def crear_tablas():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
