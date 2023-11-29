from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

motorDB = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

conexion_db = sessionmaker(autocommit=False, autoflush=False, bind=motorDB)

modeloBase = declarative_base()


# Dependencias.
def get_conexion():
    conn = conexion_db()
    try:
        yield conn
    finally:
        conn.close()
