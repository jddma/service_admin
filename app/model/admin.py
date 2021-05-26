from .database import Database
from .person import Person

import os

import json

from werkzeug.security import check_password_hash

from flask_login import login_user, UserMixin


class Admin(UserMixin, Person, Database):

    def __init__(self, email: str, password: str):
        self.__email = email
        self.__password = password

    def get_id(self):
        return self.id

    def login(self):
        self._open_connection()

        sql = json.loads(open(f"{os.getcwd()}/app/resources/querys.json").read())['findUserByEmail']
        with self._connection.cursor() as cursor:
            cursor.execute(sql, self.__email)
            result = cursor.fetchone()

            # Validar que el usaurio ingresado se encuentre registrado en la base de datos
            if result is None:
                self._close_connection()
                return False

            elif check_password_hash(result['password'], self.__password):
                del self.__password

                self.id = result['id']
                self.__document = result['document']
                self.__lastnames = result['lastnames']
                self.__names = result['names']

                self._close_connection()
                login_user(self)

                return True

            else:
                self._close_connection()
                return False
