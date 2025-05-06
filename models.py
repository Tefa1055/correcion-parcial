from sqlmodel import SQLModel, Field

class Tarea(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    titulo: str
    descripcion: str
    completado: bool = False
 