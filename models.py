from sqlmodel import SQLModel, Field

class Tarea(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    titulo: str
    descripcion: str
    completado: bool = False

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    email: str
    activo: bool = True
    tipo: str = "Normal"  # Puede ser "Normal" o "Premium"
