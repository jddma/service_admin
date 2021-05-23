from flask_restful import Resource


class AdminInformatioContoller(Resource):

    def get(self):
        return 'hola';