from .database import Database
from .person import Person
from .tournament import Tournament

from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import login_user, UserMixin


class Admin(UserMixin, Person, Database):

    def __init__(self, email: str, password: str):
        self.set_email(email)
        self.__password = password

    def get_id(self):
        return self.id

    def login(self):
        self._open_connection()

        sql = self._get_query('findUserByEmail')
        with self._connection.cursor() as cursor:
            cursor.execute(sql, self._email)
            result = cursor.fetchone()

            # Validar que el usaurio ingresado se encuentre registrado en la base de datos
            if result is None:
                self._close_connection()
                return False

            elif check_password_hash(result['password'], self.__password):
                del self.__password

                self.id = result['id']
                self._document = result['document']
                self._lastnames = result['lastnames']
                self._names = result['names']
                self._phone = result['phone']
                self._address = result['address']

                self._close_connection()
                login_user(self)

                return True

            else:
                self._close_connection()
                return False

    def get_player_information(self, player: Person):
        self._open_connection()

        sql = self._get_query('findPlayerByDocument')
        with self._connection.cursor() as cursor:
            cursor.execute(sql, player.get_document())
            result = cursor.fetchone()

            if result is None:
                self._close_connection()
                return player, False

            else:
                player.set_id(result['id'])
                player.set_email(result['email'])
                player.set_document(result['document'])
                player.set_lastnames(result['lastnames'])
                player.set_names(result['names'])
                player.set_phone(result['phone'])
                player.set_address(result['address'])
                self._close_connection()
                return player, True

    def register_new_player(self, new_player: Person, password: str):
        self._open_connection()

        sql = self._get_query('insertNewPlayer')
        with self._connection.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    new_player.get_names(),
                    new_player.get_lastnames(),
                    new_player.get_document(),
                    new_player.get_address(),
                    new_player.get_phone(),
                    new_player.get_email(),
                    generate_password_hash(password)
                )
            )
            self._connection.commit()
            self._close_connection()
            return True

    def register_new_tournament(self, new_tournament: Tournament):
        self._open_connection()

        sql = self._get_query('insertNewTournament')
        with self._connection.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    new_tournament.get_name(),
                    new_tournament.get_start_date(),
                    new_tournament.get_end_date()
                )
            )
            self._connection.commit()
            self._close_connection()

            return True
