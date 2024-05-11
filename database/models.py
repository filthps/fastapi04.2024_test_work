import sys
from typing import Union


class Model:
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


class Sallary(Model):
    pass


class Employee(Model):
    pass


class Bookkeeping(Model):
    pass
