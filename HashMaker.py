import random
import Database
from PathOrName import *


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


# Make sure it is singleton
class HashMaker(Singleton):
    """docstring for HashMaker"""

    def __init__(self):
        self._restore()

    #TODO():
    #   This part should connect to the database to restore its status.
    #   Because __new__() can make sure that only one instance exists
    #   and then it will call __init__() so it will lose its current status.
    def _restore(cls):
        cls.db = Database.DataManager(DATABASE)

    def hash_user(self):
        value = (random.randint(0, 100000000) % 100000)
        if self.check_user_exist(value):
            return self.hash_user()
        else:
            return value

    def hash_task(self):
        value = (random.randint(0, 100000000) % 100000)
        if self.check_task_exist(value):
            return self.hash_task()
        else:
            return value

    def hash_graph(self):
        value = (random.randint(0, 100000000) % 100000)
        if self.check_graph_exist(value):
            return self.hash_graph()
        else:
            return value

    def check_user_exist(self, ID, table='User'):
        predicate = " `user_ID` = " + '"' + str(ID) + '"'
        result = self.db.select_from_where('*', table, predicate)
        if result.rowcount == 0:
            return False
        else:
            return True

    def check_user_name_exist(self, account):
        predicate = " `user_name` = " + '"' + str(account) + '"'
        result = self.db.select_from_where('*', 'User', predicate)
        if result.rowcount == 0:
            return False
        else:
            return True

    def check_task_exist(self, ID, table='NodeInfo'):
        predicate = " `task_ID` = " + '"' + str(ID) + '"'
        result = self.db.select_from_where('*', table, predicate)
        if result.rowcount == 0:
            return False
        else:
            return True

    def check_graph_exist(self, ID, table='DAG'):
        predicate = " `graph_ID` = " + '"' + str(ID) + '"'
        result = self.db.select_from_where('*', table, predicate)
        if result.rowcount == 0:
            return False
        else:
            return True
