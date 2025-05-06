from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from models import Tarea
from database import get_session

router = APIRouter(prefix="/tareas")

@router.post("/")
def agregar_tarea(tarea: Tarea, session: Session = Depends(get_session)):
    if session.get(Tarea, tarea.id):
        raise HTTPException(status_code=400, detail="Tarea con ese ID ya existe")
    session.add(tarea)
    session.commit()
    session.refresh(tarea)
    return tarea

@router.get("/")
def obtener_tareas(session: Session = Depends(get_session)):
    return session.exec(select(Tarea)).all()

@router.get("/{tarea_id}")
def buscar_tarea(tarea_id: int, session: Session = Depends(get_session)):
    tarea = session.get(Tarea, tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.delete("/{tarea_id}")
def eliminar_tarea(tarea_id: int, session: Session = Depends(get_session)):
    tarea = session.get(Tarea, tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    session.delete(tarea)
    session.commit()
    return {"mensaje": "Tarea eliminada correctamente"}
