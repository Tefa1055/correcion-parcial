from sqlalchemy import Column, Integer, String
from .database import Base # Asegúrate de importar Base desde tu archivo database.py

# --- Modelo SQLAlchemy para Usuarios ---
class User(Base):
    __tablename__ = "users" # Nombre de la tabla en la base de datos (plural)

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    tipo = Column(String) # Columna para el tipo (Premium/Normal)
    estado = Column(String) # Columna para el estado (Activo/Inactivo)

    # Si tienes relación con tareas, descomenta esto y ajústalo
    # tareas = relationship("Tarea", back_populates="owner")


# --- Modelo SQLAlchemy para Tareas ---
# (Asegúrate de tener este también como lo hicimos antes)
class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String)
    # Si tienes relación con usuario, descomenta esto y ajústalo
    # owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="tareas")