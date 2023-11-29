from sqlalchemy.orm import Session
from pydantic import BaseModel

from api.config.datos import modeloBase


def obtener_uno(conexion : Session, modelo : modeloBase , campo, filtro ):
    return conexion.query(modelo).filter(campo == filtro).first()


def obtener_varios(conexion : Session, modelo : modeloBase , campo, filtro, salto, maximo ):
    return conexion.query(modelo).filter(campo == filtro).offset(salto).limit(maximo).all()


def obtener_todos(conexion : Session, modelo : modeloBase, salto : int = 0, maximo : int = 100):
    return conexion.query(modelo).offset(salto).limit(maximo).all()


def insertar(conexion : Session, esquema : BaseModel , modelo : modeloBase):
    _dict = esquema.__dict__
    nuevo = modelo(**_dict)
    conexion.add(nuevo)
    conexion.commit()
    conexion.refresh(nuevo)
    return nuevo


def actualizar(conexion : Session, esquema : BaseModel, modelo : modeloBase , campo,  filtro ):
    query = conexion.query(modelo).filter(campo == filtro)
    actual = query.first()
    if actual:
        actual_dict = esquema.model_dump()
        query.update( actual_dict, synchronize_session=False)
        conexion.commit()
    return modelo(**actual_dict)

      

def eliminar(conexion : Session, modelo : modeloBase , campo, filtro):
    actual = conexion.query(modelo).filter(campo == filtro).first()
    if actual:
        conexion.delete(actual)
        conexion.commit()
    return actual

