from sqlalchemy.orm import Session

from comun.modelos import Vnta
from comun.esquemas import EscribirVnta
from api.core import crud

 
def obtener_vnta(conn : Session, id : int) -> Vnta:
    return crud.obtener_uno(conexion=conn, modelo=Vnta, campo=Vnta.id, filtro=id)

def obtener_vntas(conn : Session, skip : int = 0, limit : int = 100):
    return crud.obtener_todos(conexion=conn, modelo=Vnta, salto=skip, maximo=limit)

def insertar_vnta(conn : Session, vnta : EscribirVnta):
    return crud.insertar(conexion=conn, esquema=vnta, modelo=Vnta )

def actualizar_vnta(conn : Session, id : int , vnta : EscribirVnta):
    return crud.actualizar( conexion=conn, esquema=vnta, modelo=Vnta, campo=Vnta.id ,filtro=id )

def eliminar_vnta(conn : Session, id : int ):
    return crud.eliminar(conexion=conn,modelo=Vnta,campo=Vnta.id, filtro=id)


   
    
    
    
    
    
    
    



    
    
    
    


