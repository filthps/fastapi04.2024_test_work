from typing import Callable
from dotenv import dotenv_values
from fastapi import FastAPI
from database.sqlite.init import connection, BASE_DIR
from database.models import Sallary, Bookkeeping, Employee

conf = dotenv_values(dotenv_path="../conf.env")
fastapi = FastAPI()


class API:
    path_roots = {
        "add_employee": "emp/add-emp/",
        "dismiss_employee": "emp/dis-emp/",
        "issue_wages": "sallary/issue/",
        "change_sallary": "sallary/change/",
        "request_sal_token": "token/request/",
        "destroy_token": "token/close/",
        "change_bookkeeping": "bookkeeping/change/",
    }


@fastapi.post("emp/add-emp/{emp_id}")
def add_employee(emp_id):
    ...


@fastapi.post("emp/dis-emp/{emp_id}")
def dismiss_employee(emp_id):
    pass


@fastapi.post()
def issue_wages(self):
    ...


def change_sallary(self):
    pass


def request_sal_token(self):
    pass


def destroy_token(self):
    pass


def change_bookkeeping(self):
    pass

