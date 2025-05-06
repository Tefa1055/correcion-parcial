from fastapi import FastAPI
from usuarios import router as usuarios_router
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

# Incluir el router de usuarios
app.include_router(usuarios_router)

# ====================
# MODELO DE TAREA
# ====================
class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str

# Base de datos temporal en memoria
tareas_db = []

# ====================
# ENDPOINTS DE TAREAS
# ====================

@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    if any(t.id == tarea.id for t in tareas_db):
        raise HTTPException(status_code=400, detail="La tarea ya existe.")
    tareas_db.append(tarea)
    return tarea

@app.get("/tareas")
def listar_tareas():
    return tareas_db

@app.delete("/tareas/{tarea_id}")
def borrar_tarea(tarea_id: int):
    for tarea in tareas_db:
        if tarea.id == tarea_id:
            tareas_db.remove(tarea)
            return {"mensaje": "Tarea eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.get("/tareas/buscar/")
def buscar_tareas(titulo: str):
    resultados = [t for t in tareas_db if titulo.lower() in t.titulo.lower()]
    return resultados
