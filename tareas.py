from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Tarea, TareaCreate

# Función para agregar tarea
def agregar_tarea(tarea: TareaCreate, db: Session):
    # Verificar si la tarea ya existe
    db_tarea = db.query(Tarea).filter(Tarea.titulo == tarea.titulo).first()
    if db_tarea:
        raise HTTPException(status_code=400, detail="La tarea ya existe.")
    
    db_tarea = Tarea(**tarea.dict())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

# Función para obtener todas las tareas
def obtener_tareas(db: Session):
    return db.query(Tarea).all()

# Función para eliminar tarea
def eliminar_tarea(tarea_id: int, db: Session):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db.delete(tarea)
    db.commit()
    return {"mensaje": "Tarea eliminada correctamente"}

# Función para buscar tareas por título
def buscar_tarea(titulo: str, db: Session):
    resultados = db.query(Tarea).filter(Tarea.titulo.ilike(f"%{titulo}%")).all()
    return resultados
