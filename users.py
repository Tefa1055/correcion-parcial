from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from models import User
from database import get_session

router = APIRouter(prefix="/users")

@router.post("/")
def crear_usuario(user: User, session: Session = Depends(get_session)):
    if session.get(User, user.id):
        raise HTTPException(status_code=400, detail="ID ya existe")
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.put("/{user_id}")
def actualizar_usuario(user_id: int, user_data: User, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    user.nombre = user_data.nombre
    user.email = user_data.email
    user.activo = user_data.activo
    user.tipo = user_data.tipo
    session.commit()
    return user

@router.patch("/{user_id}")
def actualizar_especificamente(user_id: int, user_data: dict, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in user_data.items():
        setattr(user, key, value)
    session.commit()
    return user

@router.get("/")
def listar_usuarios(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()

@router.get("/activos")
def listar_activos(session: Session = Depends(get_session)):
    return session.exec(select(User).where(User.activo == True)).all()

@router.get("/premium-activos")
def listar_premium_activos(session: Session = Depends(get_session)):
    return session.exec(select(User).where(User.activo == True, User.tipo == "Premium")).all()

@router.delete("/{user_id}")
def eliminar_usuario(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    session.delete(user)
    session.commit()
    return {"mensaje": "Usuario eliminado correctamente"}
