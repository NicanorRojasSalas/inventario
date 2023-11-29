from sqlalchemy.orm import Session

from comun.modelos import DtllVnta
from comun.esquemas import EscribirDtllVnta
from api.core import crud

 
def obtener_dtllVnta(conn : Session, id : int) -> DtllVnta:
    return crud.obtener_uno(conexion=conn, modelo=DtllVnta, campo=DtllVnta.id, filtro=id)

def obtener_dtllsVnta(vnta_id: int, conn : Session, skip : int = 0, limit : int = 100):
    return crud.obtener_varios(conexion=conn, modelo=DtllVnta,  campo=DtllVnta.vnta_id, filtro=vnta_id, salto=skip, maximo=limit)

def insertar_dtllVnta(conn : Session, dtllVnta : EscribirDtllVnta):
    return crud.insertar(conexion=conn, esquema=dtllVnta, modelo=DtllVnta )

def actualizar_dtllVnta(conn : Session, id : int , dtllVnta : EscribirDtllVnta):
    return crud.actualizar( conexion=conn, esquema=dtllVnta, modelo=DtllVnta, campo=DtllVnta.id ,filtro=id )

def eliminar_dtllVnta(conn : Session, id : int ):
    return crud.eliminar(conexion=conn,modelo=DtllVnta,campo=DtllVnta.id, filtro=id)


   
    
    
    
    
    
    
    



    
    
    
    


