from fastapi import FastAPI
from users import router as users_router
from tareas import router as tareas_router
from database import crear_tablas

app = FastAPI()

crear_tablas()

# Rutas requeridas por el taller
app.include_router(users_router)
app.include_router(tareas_router)

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}
