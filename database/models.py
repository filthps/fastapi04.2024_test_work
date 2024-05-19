import sys
from typing import Union, Literal
from itertools import groupby


class Model:
    fields: tuple = ...

    def __init__(self, primary_key="autoincr", insert=False, update=False, delete=False, **kwargs):
        self._primary_key: Union[dict, str] = primary_key  # Python >= 3.7 required! (dict keys ordering)
        self._insert = insert
        self._update = update
        self._delete = delete
        self._data = kwargs
        self.__is_valid()

    @property
    def insert(self) -> str:
        data = self._data.copy()
        data.update(self._primary_key)
        return f"INSERT INTO ({', '.join(data.keys())}) VALUES ({', '.join(data.values())});"

    @property
    def update(self) -> str:
        return f"UPDATE {self.__class__.__name__} SET {', '.join(map(lambda i: ' = '.join(i), self._data.items()))} " \
               f"WHERE {' = '.join(tuple(self._primary_key.items())[0])};"

    @property
    def delete(self) -> str:
        return f"DELETE FROM {self.__class__.__name__} WHERE {' = '.join(tuple(self._primary_key.items())[0])};"

    def __str__(self):
        if self._insert:
            return self.insert
        if self._update:
            return self.update
        if self._delete:
            return self.delete
        return "Invalid"

    def __repr__(self):
        return f"{type(self).__name__}({self.__str__()})"

    def __is_valid(self):
        def check_field_names():
            pass
        if not (sys.version_info.major == 3 and sys.version_info.minor) >= 7:
            raise RuntimeError
        if sum([self._delete, self._update, self._insert]) != 1:
            raise ValueError
        if not isinstance(self._primary_key, (dict, str,)):
            raise TypeError
        if type(self._primary_key) is str:
            if self._primary_key != "autoincr":
                raise TypeError
        if len(self._primary_key) != 1:
            raise ValueError
        if self._update or self._insert:
            if not self._data:
                raise ValueError
        if type(self.fields) is not tuple:
            raise TypeError
        if not self.fields:
            raise ValueError
        if not all(map(lambda x: isinstance(x, str), self.fields)):
            raise TypeError
        if any(map(lambda x: any([1 if len(i) > 1 else 0 for i in x[1]]), groupby(self.fields))):
            raise ValueError
        check_field_names()


class Sallary(Model):
    fields = ("sid", "emplid", "nid", "totalhour", "date_",)


class Employee(Model):
    fields = ("emplid", "firstname", "lastname", "surname", "payperhour", "empstartdate", "dismissdate", "emstatus",
              "ismanager",)


class Bookkeeping(Model):
    fields = ("id", "ndfltax", "tax", "yearindexpercently", "editdate",)


class Session(Model):
    fields = ("sessionid", "emp", "token", "clientid", "from_",)
