from typing import Optional


class Model:
    def __init__(self):
        self._insert = False
        self._update = False
        self._delete = False

    def __str__(self):
        self.__is_valid()


    def insert(self):
        self._insert = True

    def update(self):
        self._update = True

    def delete(self):
        self._delete = True

    def __is_valid(self):
        if sum([self._delete, self._update, self._insert]) != 1:
            raise ValueError


class Sallary(Model):
    def __init__(self, **data, pk: Optional[dict] = None):
        self._data = data
        super().__init__()


class Employee(Model):
    pass


class Bookkeeping(Model):
    ...
