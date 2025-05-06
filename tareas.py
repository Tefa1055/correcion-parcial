from fastapi import HTTPException
from models import Tarea

tareas_db = []

def agregar_tarea(tarea: Tarea):
    if any(t.id == tarea.id for t in tareas_db):
        raise HTTPException(status_code=400, detail="La tarea ya existe.")
    tareas_db.append(tarea)
    return tarea

def obtener_tareas():
    return tareas_db

def eliminar_tarea(tarea_id: int):
    for tarea in tareas_db:
        if tarea.id == tarea_id:
            tareas_db.remove(tarea)
            return {"mensaje": "Tarea eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

def buscar_tarea(titulo: str):
    resultados = [t for t in tareas_db if titulo.lower() in t.titulo.lower()]
    return resultados
