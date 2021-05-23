from flask import Flask

from flask_login import LoginManager

from .config import Config

from .web import web_controllers, users

login_manager = LoginManager()


@login_manager.user_loader
def loader(admin_id):
    try:
        return users[int(admin_id)]

    except KeyError:
        return None


def create_app():
    # Instanciar y configurar la app
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(web_controllers)

    login_manager.init_app(app)

    return app
