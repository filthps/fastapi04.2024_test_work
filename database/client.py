import sqlite3
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Callable
from dotenv import dotenv_values


conf = dotenv_values(dotenv_path="../../conf.env")


class API(HTTPServer, BaseHTTPRequestHandler):
    _server = None
    path_roots = {
        "add_employee": "emp/add-emp/",
        "dismiss_employee": "emp/dis-emp/",
        "issue_wages": "sallary/issue/",
        "change_sallary": "sallary/change/",
        "request_sal_token": "token/request/",
        "destroy_token": "token/close/",
        "change_bookkeeping": "bookkeeping/change/",
    }

    def run(self, server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()


    def select_item(self, api_url, name, model_name=None):
        ...

    def insert_item(self):
        ...

    def __getattribute__(self, item, *args, **kwargs) -> Callable:
        return super().__getattribute__(item)(self.path_roots[item])


class DatabaseClient:
    _connection = None

    def __new__(cls, path=conf["DATABASE_URL"]):
        ...  # sqlite3.connection

    def insert(self, table_name):
        pass

    def delete(self):
        pass

    def update(self):
        pass


if __name__ == "__main__":
    API().run()
