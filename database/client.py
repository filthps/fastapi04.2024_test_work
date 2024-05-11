from http.server import HTTPServer
from typing import Callable
from dotenv import dotenv_values


conf = dotenv_values(dotenv_path="../../conf.env")


class APi:
    _server = None
    path_roots = {
        "select_item": ...,
        "insert_item": ...,
        "request_sal_token": ...,

    }

    def __new__(cls, *args, **kwargs):
        ...  # http.server.HTTPServer

    def select_item(self, api_url, name, model_name=None):
        ...

    def insert_item(self):
        ...

    def __getattribute__(self, item, *args, **kwargs) -> Callable:
        return super().__getattribute__(item)(self.path_roots[item])


class DatabaseClient:
    _connection = None

    def __new__(cls):
        ...  # sqlite3.connection

    def insert(self, table_name):
        pass

    def delete(self):
        pass

    def update(self):
        pass
