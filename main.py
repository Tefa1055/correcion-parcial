from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import get_db
from tareas import agregar_tarea, obtener_tareas, eliminar_tarea, buscar_tarea
from models import TareaCreate, Tarea

app = FastAPI()

# Endpoint para crear tarea
@app.post("/tareas/")
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    return agregar_tarea(tarea, db)

# Endpoint para listar todas las tareas
@app.get("/tareas/")
def listar_tareas(db: Session = Depends(get_db)):
    return obtener_tareas(db)

# Endpoint para eliminar tarea
@app.delete("/tareas/{tarea_id}")
def borrar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    return eliminar_tarea(tarea_id, db)

# Endpoint para buscar tareas por título
@app.get("/tareas/buscar/")
def buscar_tareas(titulo: str, db: Session = Depends(get_db)):
    return buscar_tarea(titulo, db)
