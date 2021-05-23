from flask import Blueprint

from flask_restful import Api


web_controllers = Blueprint('web_controller', __name__, url_prefix='/api')
api = Api(web_controllers)

from .admin_information_controller import AdminInformatioContoller

api.add_resource(AdminInformatioContoller, '/info')