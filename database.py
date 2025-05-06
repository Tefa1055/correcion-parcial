# database.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos SQLite.
# './sql_app.db' creará un archivo llamado sql_app.db en el mismo directorio.
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Crear el motor de la base de datos.
# connect_args es necesario para SQLite para permitir múltiples hilos de solicitud.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear una fábrica de sesiones. Cada instancia de SessionLocal será una sesión de base de datos.
# autocommit=False: no confirmará transacciones automáticamente. Necesitas llamar a .commit().
# autoflush=False: no volcará las operaciones al DB hasta que llames a .commit() o .flush().
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar una base para tus clases de modelo.
Base = declarative_base()

# --- Definir tus modelos (clases de base de datos) ---

class User(Base):
    __tablename__ = "users" # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True) # Columna ID, clave primaria, indexada
    nombre = Column(String, index=True) # Columna Nombre, indexada
    email = Column(String, unique=True, index=True) # Columna Email, debe ser único, indexada
    # Puedes añadir más columnas según tus datos
    # tipo = Column(String)
    # estado = Column(String)

# Puedes definir otros modelos aquí, por ejemplo, para 'Tareas' si las necesitas.
# class Tarea(Base):
#     __tablename__ = "tareas"
#     id = Column(Integer, primary_key=True, index=True)
#     titulo = Column(String, index=True)
#     descripcion = Column(String)
#     # Puedes añadir una clave foránea si una tarea pertenece a un usuario
#     # owner_id = Column(Integer, ForeignKey("users.id"))
#     # owner = relationship("User", back_populates="tareas") # Si defines 'tareas' en el modelo User

# Para que los modelos User puedan tener tareas
# class User(Base):
#     __tablename__ = "users"
#     # ... otras columnas ...
#     tareas = relationship("Tarea", back_populates="owner")