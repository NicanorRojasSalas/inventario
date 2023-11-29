from sqlalchemy.orm import Session

from comun.modelos import Invntr
from comun.esquemas import EscribirInvntr
from api.core import crud

 
def obtener_invntr(conn : Session, id : int) -> Invntr:
    return crud.obtener_uno(conexion=conn, modelo=Invntr, campo=Invntr.id, filtro=id)

def obtener_invntrs(conn : Session, skip : int = 0, limit : int = 100):
    return crud.obtener_todos(conexion=conn, modelo=Invntr, salto=skip, maximo=limit)

def insertar_invntr(conn : Session, prdct : EscribirInvntr):
    return crud.insertar(conexion=conn, esquema=prdct, modelo=Invntr )

def actualizar_invntr(conn : Session, id : int , invntr : EscribirInvntr):
    return crud.actualizar( conexion=conn, esquema=invntr, modelo=Invntr, campo=Invntr.id ,filtro=id )

def eliminar_invntr(conn : Session, id : int ):
    return crud.eliminar(conexion=conn,modelo=Invntr,campo=Invntr.id, filtro=id)


   
    
    
    
    
    
    
    



    
    
    
    


