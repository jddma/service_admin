from flask_restful import Resource

from flask_login import login_required, current_user


class AdminInformationContoller(Resource):

    @login_required
    def get(self):
        return current_user.__dict__
