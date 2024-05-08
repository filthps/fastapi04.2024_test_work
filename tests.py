import time
import unittest
from database.sqlite.init import set_up


def restore_database(test_m):
    def wrap(*a, **k):
        set_up()
        time.sleep(2)
        test_m(*a, **k)
    return wrap


class TestDatabase(unittest.TestCase):
    def test_...
