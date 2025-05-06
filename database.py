# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos SQLite.
# './sql_app.db' creará un archivo llamado sql_app.db en el mismo directorio que main.py.
# Usamos una ruta relativa simple aquí.
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

# Declarar una base para tus clases de modelo SQLAlchemy.
# Todos tus modelos SQLAlchemy deben heredar de esta clase Base.
Base = declarative_base()

# --- Dependencia para obtener una sesión de base de datos ---
# Esta función se usa en los endpoints (con Depends) para obtener una sesión de DB.
# Asegura que cada solicitud obtenga su propia sesión de base de datos independiente
# y que la sesión se cierre automáticamente después de que la solicitud termine.
def get_db():
    db = SessionLocal()
    try:
        yield db # Proporciona la sesión a la ruta que la solicita
    finally:
        db.close() # Cierra la sesión de la base de datos al finalizar la solicitud
