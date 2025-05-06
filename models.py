from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

# Configuración de la base de datos (usamos SQLite por simplicidad)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Crea una base de datos para SQLAlchemy
Base = declarative_base()

# Configuración de la sesión de SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definir el modelo de Tarea
class Tarea(Base):
    __tablename__ = "tareas"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String)
    done = Column(Boolean, default=False)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Pydantic model para las tareas (para la validación de datos en FastAPI)
class TareaCreate(BaseModel):
    titulo: str
    descripcion: str
