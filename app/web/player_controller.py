from app.model.person import Person

from . import make_custom_response

import json

from flask import request

from flask_restful import Resource

from flask_login import login_required, current_user


class PlayerController(Resource):

    @login_required
    def get(self, document=None):
        if document is None:
            return make_custom_response(
                '{"message": "El parametro de búsqueda no se envio correctamente"}',
                400,
                'Application/json'
            )

        player = Person(document)
        player, player_exists = current_user.get_player_information(player)

        if player_exists:
            return player.__dict__
        else:
            return make_custom_response('{"message": "not found"}', 404, 'application/json')

    @login_required
    def post(self):
        try:
            data = json.loads(request.data)
            new_player = Person(
                document=data['document'],
                names=data['names'],
                lastnames=data['lastnames'],
                phone=data['phone'],
                address=data['address'],
                email=data['email']
            )
            if current_user.register_new_player(new_player, data['password']):
                return make_custom_response('{"message": "ok"', 200, 'application/json}')

        except (json.decoder.JSONDecodeError, KeyError):
            return make_custom_response(
                '{"message": "Formato del cuerpo no valido"}',
                400,
                'Application/json'
            )
