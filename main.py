from fastapi import FastAPI
from tareas import router as tareas_router
from database import crear_tablas

app = FastAPI()

crear_tablas()
app.include_router(tareas_router)
