# crud.py (o el nombre que le des a este archivo)

from sqlalchemy.orm import Session
from fastapi import HTTPException # Si quieres mantener las excepciones aquí
# Importa el modelo SQLAlchemy Tarea
from . import models # Asegúrate de importar models desde tu estructura de proyecto
# Si también necesitas Pydantic Schemas aquí para validación o retorno específico
# from . import schemas

# ELIMINA O COMENTA ESTO: Ya no usaremos la lista en memoria
# tareas_db = []

# ELIMINA O COMENTA ESTO: No importes el modelo Pydantic Tarea desde aquí
# from models import Tarea # Esto parece importar un modelo Pydantic, no SQLAlchemy


# --- Funciones de manejo de tareas adaptadas para usar la base de datos ---

# La función recibe la sesión 'db' y una tarea (probablemente un esquema Pydantic TareaCreate)
def crear_tarea(db: Session, tarea: schemas.TareaCreate): # Asumiendo que usas schemas.TareaCreate para la entrada
    # Opcional: Verificar si una tarea con el mismo título o descripción ya existe si es necesario
    # db_tarea_existente = db.query(models.Tarea).filter(models.Tarea.titulo == tarea.titulo).first()
    # if db_tarea_existente:
    #     raise HTTPException(status_code=400, detail="La tarea ya existe.") # Considera manejar excepciones en los endpoints

    # Crea una instancia del modelo SQLAlchemy Tarea
    db_tarea = models.Tarea(titulo=tarea.titulo, descripcion=tarea.descripcion)

    # Añade y guarda en la base de datos
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea) # Actualiza el objeto con el ID generado

    return db_tarea # Retorna el objeto Tarea de SQLAlchemy

# La función recibe la sesión 'db' y puede incluir parámetros de paginación
def obtener_tareas(db: Session, skip: int = 0, limit: int = 100):
    # Consulta todas las tareas con paginación
    return db.query(models.Tarea).offset(skip).limit(limit).all()

# La función recibe la sesión 'db' y el ID de la tarea
def eliminar_tarea(db: Session, tarea_id: int):
    # Busca la tarea por ID
    db_tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

    # Considera manejar la excepción 404 en el endpoint que llama a esta función
    # if db_tarea is None:
    #     raise HTTPException(status_code=404, detail="Tarea no encontrada")

    if db_tarea:
        db.delete(db_tarea)
        db.commit()
        return {"mensaje": "Tarea eliminada correctamente"}
    return None # Retorna None si la tarea no fue encontrada (para que el endpoint decida el 404)


# La función recibe la sesión 'db' y el título a buscar
def buscar_tarea(db: Session, titulo: str):
    # Busca tareas cuyo título contenga la subcadena (insensible a mayúsculas/minúsculas)
    resultados = db.query(models.Tarea).filter(models.Tarea.titulo.ilike(f"%{titulo}%")).all()
    return resultados # Retorna la lista de objetos Tarea de SQLAlchemy