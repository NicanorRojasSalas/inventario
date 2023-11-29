import os

from flask import Flask, render_template
from web.core.acceso.usro.rutas import bpUsro
from web.core.acceso.rutas import bpAcceso

def create_app():

    app = Flask(__name__,static_folder='web/estaticos', template_folder='web/plantillas')
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG = True, 
        PORT = 5000,   
              
    )
    
    
    bpAcceso.register_blueprint(bpUsro)
    app.register_blueprint( bpAcceso )    
    
    @app.route('/')
    def Inicio():
        return render_template("inicio.html")

    return app


if __name__ == "__main__":
    web = create_app()
    web.run()
    
    