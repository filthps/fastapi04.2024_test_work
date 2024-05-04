""" Адаптеры для хранилищ """
import sqlite3
from sqlite3.dbapi2 import Cursor
from setup.init import connection


class Database:
    @property
    def _connection(self) -> Cursor:
        return connection.cursor()

    def create_sallary(self, emp_id: int):
        """ Выдать зарплату """
        ...

    def create_employee(self):
        """ Устроить нового сотрудника в штат """

class Cache:
    pass
