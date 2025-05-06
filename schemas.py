# schemas.py
from pydantic import BaseModel

# --- Esquemas Pydantic para Usuarios ---

# Schema base para un usuario (campos comunes)
class UserBase(BaseModel):
    nombre: str
    tipo: str
    estado: str

# Schema para crear un usuario (usado en el POST)
class UserCreate(UserBase):
    pass # Si UserCreate es igual a UserBase

# Schema para leer/obtener un usuario (incluye el ID generado por la DB)
class User(UserBase):
    id: int

    class Config:
        orm_mode = True # Habilita la compatibilidad con modelos ORM de SQLAlchemy


# Schema para actualizar el estado de un usuario (basado en tu EstadoUsuario)
class EstadoUsuario(BaseModel):
    estado: str # "Activo" o "Inactivo"


# --- Esquemas Pydantic para Tareas ---
# (Asegúrate de tener estos también como lo hicimos antes)

# Schema base para una tarea
class TareaBase(BaseModel):
    titulo: str
    descripcion: str

# Schema para crear una tarea
class TareaCreate(TareaBase):
    pass

# Schema para leer/obtener una tarea
class Tarea(TareaBase):
    id: int
    # owner_id: int # Si hay relación con usuario

    class Config:
        orm_mode = True