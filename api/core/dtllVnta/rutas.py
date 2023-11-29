from fastapi import APIRouter, Depends,  HTTPException, status
from sqlalchemy.orm import Session

from api.config.datos import get_conexion

from comun.esquemas import EscribirDtllVnta
from api.core.dtllVnta.operaciones import *

routerDtllVnta= APIRouter(prefix="/DetallesVenta", tags=["DetallesVenta",] )


@routerDtllVnta.post("/",
                 name="Agregar Detalle",
                 description="Permite agregar un nuevo detalle",
                 status_code= status.HTTP_201_CREATED
                )
def crear_dtllVnta( Detalle : EscribirDtllVnta, conexion : Session = Depends(get_conexion)):
    return insertar_dtllVnta(conn = conexion, dtllVnta=Detalle) 


@routerDtllVnta.put("/{Id:int}",
                 name="Editar Detalle",
                 description ="Permite editar un detalle existente",
                 status_code = status.HTTP_202_ACCEPTED
               )
def editar_dtllVnta( Id : int, Detalle : EscribirDtllVnta, conexion : Session = Depends(get_conexion)):
    db_dtll = obtener_dtllVnta(conn = conexion, id = Id)
    if db_dtll is None:
        raise HTTPException(status_code=400, detail="Detalle no encontrado")
    return actualizar_dtllVnta(conn = conexion, id = Id, dtllVnta = Detalle)


@routerDtllVnta.delete("/{Id:int}",
                    name="Eliminar Detalle",
                    description="Permite eliminar un Detalle",
                    status_code= status.HTTP_202_ACCEPTED
                   )
def borrar_dtllVnta(Id : int, conexion : Session = Depends(get_conexion)):
    db_dtll = obtener_dtllVnta(conn = conexion, Id = Id)
    if db_dtll is None:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return eliminar_dtllVnta(conn = conexion, id=Id)


@routerDtllVnta.get("/venta/{Id:int}",
                name="Obtener Detalles" ,
                description="Permite obtener una lista de las detalles de una venta",
                status_code= status.HTTP_202_ACCEPTED               
               )
def leer_dtllsVnta(Id: int, Skip : int = 0, Limit : int = 100, conexion : Session = Depends(get_conexion)):
    detalles = obtener_dtllsVnta(vnta_id= Id, conn=conexion, skip=Skip, limit=Limit)
    return detalles


@routerDtllVnta.get("/{Id:int}",
                name="Obtener Detalle Venta por Id",
                description="Permite obtener la info de una detalle de venta",
                status_code= status.HTTP_202_ACCEPTED
               )
def leer_vnta( Id : int, conexion : Session = Depends(get_conexion)):
    db_dtll = obtener_dtllVnta(conn = conexion, id = Id)
    if db_dtll is None:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return db_dtll

