from flask_restful import Resource

from flask import request

from . import make_custom_response, users

from app.model.admin import Admin

import json


class LoginController(Resource):

    def post(self):
        try:
            credentials = json.loads(request.data)
            admin_object = Admin(credentials['email'], credentials['password'])

            if admin_object.login():
                users[admin_object.get_id()] = admin_object
                return make_custom_response('{"message": "éxito"}', 200, 'Application/json')
            else:
                return make_custom_response('{"message": "credenciales incorrectas"}', 200, 'Application/json')

        except (json.decoder.JSONDecodeError, KeyError):
            return make_custom_response(
                '{"message": "Formato del cuerpo no valido"}',
                400,
                'Application/json'
            )
