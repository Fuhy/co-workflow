import random


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


# Make sure it is singleton
class HashMaker(Singleton):
    """docstring for HashMaker"""

    user_table = set()
    task_table = set()
    graph_table = set()

    def __init__(self):
        self._restore()

    #TODO():
    #   This part should connect to the database to restore its status.
    #   Because __new__() can make sure that only one instance exists
    #   and then it will call __init__() so it will lose its current status.
    def _restore(cls):
        pass

    def hash_user(self):
        value = (random.randint(0, 10000000) % 100000)
        if value in self.user_table:
            return hash_user()
        else:
            self.user_table.add(value)
            return value

    def hash_task(self):
        value = (random.randint(0, 10000000) % 100000)
        if value in self.task_table:
            return hash_task()
        else:
            self.task_table.add(value)
            return value

    def hash_graph(self):
        value = (random.randint(0, 10000000) % 100000)
        if value in self.graph_table:
            return hash_graph()
        else:
            self.graph_table.add(value)
            return value

    def check_user_exist(self, ID):
        if ID in self.user_table:
            return True
        else:
            return False

    def check_task_exist(self, ID):
        if ID in self.task_table:
            return True
        else:
            return False

    def check_graph_exist(self, ID):
        if ID in self.graph_table:
            return True
        else:
            return False