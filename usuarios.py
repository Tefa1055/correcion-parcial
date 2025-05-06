from fastapi import APIRouter, HTTPException
from typing import List
from models import Usuario, EstadoUsuario

router = APIRouter()

# Base de datos simulada
usuarios_db: List[dict] = [
    {"id": 1, "nombre": "Ana", "tipo": "Premium", "estado": "Activo"},
    {"id": 2, "nombre": "Luis", "tipo": "Normal", "estado": "Inactivo"},
]

# Primero rutas fijas para evitar conflictos
@router.get("/usuarios/premium-activos")
def listar_premium_activos():
    return [u for u in usuarios_db if u["tipo"] == "Premium" and u["estado"] == "Activo"]

@router.get("/usuarios")
def listar_usuarios():
    return usuarios_db

@router.post("/usuarios")
def crear_usuario(usuario: Usuario):
    usuarios_db.append(usuario.dict())
    return {"mensaje": "Usuario creado exitosamente"}

@router.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario_actualizado: Usuario):
    for i, usuario in enumerate(usuarios_db):
        if usuario["id"] == usuario_id:
            usuarios_db[i] = usuario_actualizado.dict()
            return {"mensaje": "Usuario actualizado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.patch("/usuarios/{usuario_id}/estado")
def cambiar_estado(usuario_id: int, nuevo_estado: EstadoUsuario):
    for usuario in usuarios_db:
        if usuario["id"] == usuario_id:
            usuario["estado"] = nuevo_estado.estado
            return {"mensaje": "Estado actualizado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    for i, usuario in enumerate(usuarios_db):
        if usuario["id"] == usuario_id:
            del usuarios_db[i]
            return {"mensaje": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario["id"] == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
 