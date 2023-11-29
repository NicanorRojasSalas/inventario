from sqlalchemy.orm import Session

from comun.modelos import Prdct
from comun.esquemas import EscribirPrdct
from api.core import crud

 
def obtener_prdct(conn : Session, id : int) -> Prdct:
    return crud.obtener_uno(conexion=conn, modelo=Prdct, campo=Prdct.id, filtro=id)

def obtener_prdcts(conn : Session, skip : int = 0, limit : int = 100):
    return crud.obtener_todos(conexion=conn, modelo=Prdct, salto=skip, maximo=limit)

def insertar_prdct(conn : Session, prdct : EscribirPrdct):
    return crud.insertar(conexion=conn, esquema=prdct, modelo=Prdct )

def actualizar_prdct(conn : Session, id : int , prdct : EscribirPrdct):
    return crud.actualizar( conexion=conn, esquema=prdct, modelo=Prdct, campo=Prdct.id ,filtro=id )

def eliminar_prdct(conn : Session, id : int ):
    return crud.eliminar(conexion=conn,modelo=Prdct,campo=Prdct.id, filtro=id)


   
    
    
    
    
    
    
    



    
    
    
    


