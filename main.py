from fastapi import FastAPI
from usuarios import router as usuarios_router

app = FastAPI()

app.include_router(usuarios_router)
