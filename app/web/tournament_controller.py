from . import make_custom_response

from app.model.tournament import Tournament

from flask import request

from flask_restful import Resource

from flask_login import login_required, current_user

import json

from datetime import datetime

class TournamentController(Resource):

    @login_required
    def post(self):
        try:
            data = json.loads(request.data)
            new_tournament = Tournament(
                name=data['name'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                is_active=0
            )
            if current_user.register_new_tournament(new_tournament):
                return make_custom_response('{"message": "ok"}', 200, 'application/json')

        except (json.decoder.JSONDecodeError, KeyError):
            return make_custom_response(
                '{"message": "Formato del cuerpo no valido"}',
                400,
                'Application/json'
            )

    @login_required
    def get(self, name=None):
        data = current_user.search_tournaments(name)
        if data is None:
            return make_custom_response('{"message": "not found"}', 404, 'application/json')
        else:
            response = []
            for i in data:
                i['start_date'] = i['start_date'].strftime("%Y-%m-%d")
                i['end_date'] = i['end_date'].strftime("%Y-%m-%d")
                response.append(i)
            return data
