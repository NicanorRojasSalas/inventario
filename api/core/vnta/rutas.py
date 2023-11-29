from fastapi import APIRouter, Depends,  HTTPException, status
from sqlalchemy.orm import Session

from api.config.datos import get_conexion

from comun.esquemas import EscribirVnta
from api.core.vnta.operaciones import *

routerVnta= APIRouter(prefix="/ventas", tags=["Ventas",] )


@routerVnta.post("/",
                 name="Agregar Venta",
                 description="Permite agregar una nueva venta",
                 status_code= status.HTTP_201_CREATED
                )
def crear_vnta( Venta : EscribirVnta, conexion : Session = Depends(get_conexion)):
    return insertar_vnta(conn = conexion, vnta=Venta) 


@routerVnta.put("/{Id:int}",
                 name="Editar Venta",
                 description ="Permite editar una venta existente",
                 status_code = status.HTTP_202_ACCEPTED
               )
def editar_vnta( Id : int, Venta : EscribirVnta, conexion : Session = Depends(get_conexion)):
    db_vnta = obtener_vnta(conn = conexion, id = Id)
    if db_vnta is None:
        raise HTTPException(status_code=400, detail="Venta no encontrado")
    return actualizar_vnta(conn = conexion, id = Id, vnta = Venta)


@routerVnta.delete("/{Id:int}",
                    name="Eliminar Venta",
                    description="Permite eliminar una venta",
                    status_code= status.HTTP_202_ACCEPTED
                   )
def borrar_vnta(Id : int, conexion : Session = Depends(get_conexion)):
    db_vnta = obtener_vnta(conn = conexion, Id = Id)
    if db_vnta is None:
        raise HTTPException(status_code=404, detail="Venta no encontrado")
    return eliminar_vnta(conn = conexion, id=Id)


@routerVnta.get("/",
                name="Obtener Ventas" ,
                description="Permite obtener una lista de las ventas",
                status_code= status.HTTP_202_ACCEPTED               
               )
def leer_vntas(Skip : int = 0, Limit : int = 100, conexion : Session = Depends(get_conexion)):
    ventas = obtener_vntas(conn=conexion, skip=Skip, limit=Limit)
    return ventas


@routerVnta.get("/{Id:int}",
                name="Obtener Venta por Id",
                description="Permite obtener la info de una venta",
                status_code= status.HTTP_202_ACCEPTED
               )
def leer_vnta( Id : int, conexion : Session = Depends(get_conexion)):
    db_vnta = obtener_vnta(conn = conexion, id = Id)
    if db_vnta is None:
        raise HTTPException(status_code=404, detail="Venta no encontrado")
    return db_vnta

