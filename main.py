# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# Importa la base y el motor que definiste en database.py
from .database import SessionLocal, engine, Base
# Importa tus modelos SQLAlchemy (User, Tarea) y esquemas Pydantic
from . import models, schemas

# Si tienes un router separado para usuarios en usuarios.py
# from usuarios import router as usuarios_router

# Crear todas las tablas definidas en Base.metadata si no existen
# Esto se hace solo una vez al iniciar la aplicación (o en un script de inicialización)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Si tienes un router separado para usuarios, inclúyelo
# app.include_router(usuarios_router)

# --- Dependencia para obtener una sesión de base de datos ---
# (Asegúrate de tener esta función como se explicó en la guía anterior)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ====================
# MODELO DE TAREA - ¡ELIMINA O COMENTA ESTO!
# Ya no usaremos la lista en memoria
# ====================
# class Tarea(BaseModel):
#     id: int
#     titulo: str
#     descripcion: str
#
# Base de datos temporal en memoria - ¡ELIMINA O COMENTA ESTO!
# tareas_db = []

# ENDPOINTS DE TAREAS - Adaptados para usar la base de datos

# Usamos el esquema Pydantic TareaCreate para la entrada y Tarea para la salida
@app.post("/tareas/", response_model=schemas.Tarea)
def crear_tarea(tarea: schemas.TareaCreate, db: Session = Depends(get_db)):
    # Crear una instancia del modelo SQLAlchemy Tarea con los datos recibidos
    # SQLAlchemy asignará el ID automáticamente
    db_tarea = models.Tarea(titulo=tarea.titulo, descripcion=tarea.descripcion)

    # Añadir el objeto a la sesión y guardar en la base de datos
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea) # Actualiza el objeto db_tarea con el ID asignado

    return db_tarea # Retorna el objeto db_tarea (que Pydantic serializará usando schemas.Tarea y orm_mode=True)

# Usamos el esquema Pydantic Tarea para la salida (lista de tareas)
@app.get("/tareas/", response_model=list[schemas.Tarea])
def listar_tareas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Consulta la base de datos para obtener tareas
    # Puedes usar skip y limit para paginación
    tareas = db.query(models.Tarea).offset(skip).limit(limit).all()
    return tareas # Retorna la lista de objetos Tarea de SQLAlchemy (que Pydantic serializará)

@app.delete("/tareas/{tarea_id}")
def borrar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    # Busca la tarea por ID
    db_tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    # Elimina la tarea de la sesión y confirma la transacción
    db.delete(db_tarea)
    db.commit()

    return {"mensaje": "Tarea eliminada correctamente"}

# Usamos el esquema Pydantic Tarea para la salida (lista de tareas encontradas)
@app.get("/tareas/buscar/", response_model=list[schemas.Tarea])
def buscar_tareas(titulo: str, db: Session = Depends(get_db)):
    # Busca tareas cuyo título contenga la subcadena (insensible a mayúsculas/minúsculas)
    # Usamos .ilike() para búsqueda insensible a mayúsculas/minúsculas con comodines SQL (%)
    resultados = db.query(models.Tarea).filter(models.Tarea.titulo.ilike(f"%{titulo}%")).all()
    return resultados # Retorna la lista de objetos Tarea de SQLAlchemy
