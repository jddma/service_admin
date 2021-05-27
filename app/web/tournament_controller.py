from . import make_custom_response

from app.model.tournament import Tournament

from flask import request

from flask_restful import Resource

from flask_login import login_required, current_user

import json

class TournamentController(Resource):

    @login_required
    def post(self):
        try:
            data = json.loads(request.data)
            new_tournament = Tournament(data['name'], data['start_date'], data['end_date'], 0)
            if current_user.register_new_tournament(new_tournament):
                return make_custom_response('{"message": "ok"}', 200, 'application/json')

        except (json.decoder.JSONDecodeError, KeyError):
            return make_custom_response(
                '{"message": "Formato del cuerpo no valido"}',
                400,
                'Application/json'
            )
