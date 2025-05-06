from fastapi import FastAPI
from tareas import router as tareas_router
from database import crear_tablas

app = FastAPI()

# Crear las tablas al iniciar la app
crear_tablas()

# Incluir las rutas
app.include_router(tareas_router)
