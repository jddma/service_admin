import pymysql.cursors

import os

import logging

import sys


class Database():

    def _open_connection(self):
        try:
            self._connection = pymysql.connect(
                host=os.environ['MY_HOST'],
                user=os.environ['MY_USER'],
                password=os.environ['MY_PASSWORD'],
                db=os.environ['MY_DB_NAME'],
                cursorclass = pymysql.cursors.DictCursor
            )
        except KeyError:
            logging.fatal('Variables de conexión no configuradas')
            sys.exit()

    def _close_connection(self):
        self._connection.close()
        del self._connection
