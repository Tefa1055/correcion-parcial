from sqlmodel import SQLModel, create_engine, Session

# URL de conexión a SQLite (base de datos local)
DATABASE_URL = "sqlite:///./tareas.db"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear las tablas en la base de datos si no existen
def crear_tablas():
    SQLModel.metadata.create_all(engine)

# Obtener sesión de conexión a la base de datos
def get_session():
    with Session(engine) as session:
        yield session
