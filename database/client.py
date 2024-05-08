from abc import ABC, abstractmethod
from dotenv


class Connection(ABC):


    def __init__(self):
        ...


class Client:
    def insert(self, table_name):
        pass

    def delete(self):
        pass

    def update(self):
        pass
