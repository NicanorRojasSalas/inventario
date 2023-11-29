import uvicorn 

from fastapi import FastAPI
from api.core.prdct.rutas import routerPrdct
from api.core.vnta.rutas import routerVnta
from api.core.invntr.rutas import routerInvntr
from api.core.dtllVnta.rutas import routerDtllVnta

from api.config.datos import modeloBase, motorDB 


# Crea la estructura de tablas en DB
modeloBase.metadata.create_all(bind=motorDB)

api = FastAPI()

api.include_router(routerPrdct)
api.include_router(routerVnta)
api.include_router(routerInvntr)
api.include_router(routerDtllVnta)



@api.get("/")
def root():
    return {"mensaje" : "Bienvenidos"}

if __name__ == "__main__":
    uvicorn.run("inicio_api:api", port=8080, log_level="info", reload=True)
    
