from flask import Blueprint, make_response

from flask_restful import Api

users = {}


def make_custom_response(body: str, status_code: int, content_type: str):
    response = make_response(body)
    response.status_code = status_code
    response.headers['Content-Type'] = content_type
    return response


from .admin_information_controller import AdminInformationContoller
from .login_controller import LoginController
from .player_controller import PlayerController
from .tournament_controller import TournamentController

web_controllers = Blueprint('web_controller', __name__, url_prefix='/api')
api = Api(web_controllers)

api.add_resource(AdminInformationContoller, '/info')
api.add_resource(LoginController, '/login')
api.add_resource(PlayerController, '/player/<document>', '/player')
api.add_resource(TournamentController, '/tournament')

