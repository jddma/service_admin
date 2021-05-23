from flask import Flask

from.config import Config

from .web import web_controllers

def create_app():

    #Instanciar y configurar la app
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(web_controllers)

    return app