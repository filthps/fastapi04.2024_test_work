import uuid
from typing import Callable
from dotenv import dotenv_values
from fastapi import FastAPI
from cryptography.fernet import Fernet
from database.sqlite.init import connection, BASE_DIR
from database.models import Sallary, Bookkeeping, Employee

conf = dotenv_values(dotenv_path="../conf.env")
fastapi = FastAPI()
clipper = ...  # Держим это в секрете


@fastapi.get("auth/{ui_id}")
def get_token(ui_id):
    """  """
    session_key = Fernet.generate_key()
    fernet_instance = Fernet(session_key)
    token = fernet_instance.encrypt(clipper)  # fernet_instance.decrypt(token)
    return token


@fastapi.post("emp/add-emp/{emp_id}")
def add_employee(emp_id):
    ...


@fastapi.post("emp/dis-emp/{emp_id}")
def dismiss_employee(emp_id):
    pass


@fastapi.post()
def issue_wages(self):
    ...


@fastapi.post("sallary/change/{emp_id}")
def change_sallary(self):
    pass


@fastapi.post("token/request/{emp_id}")
def request_sal_token(self):
    pass


@fastapi.post("token/close/{token}")
def destroy_token(self):
    pass


@fastapi.post("bookkeeping/change/")
def change_bookkeeping(self):
    pass
