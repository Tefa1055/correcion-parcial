from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    tipo: str  # Puede ser "Premium" o "Normal"
    estado: str  # Puede ser "Activo" o "Inactivo"

class EstadoUsuario(BaseModel):
    estado: str  # "Activo" o "Inactivo"
