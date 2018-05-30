import pymysql

class DataManager(object):
    """docstring for DataManager"""

    def __init__(self, database):
        self.connect = self._connect(database)

    def _connect(self,
                 database,
                 host='localhost',
                 user='root',
                 passwd='',
                 charset='utf8'):
        return pymysql.connect(
            host, user, passwd, db=database, charset=charset)

    def close(self):
        self.connect.close()

    def select_from_where(self, what="", where="", predicate=""):
        """Select something from table where predicates are True.

        Return:
            Return the cursor If it's SUCCESS,
            otherwise return None.
        """
        if predicate == "":
            command = 'SELECT ' + what + ' FROM ' + where + ';'
        else:
            command = 'SELECT ' + what + ' FROM ' + where + ' WHERE ' + predicate + ';'
        cursor = self.connect.cursor()
        try:
            cursor.execute(command)
        except Exception:
            return None
        return cursor


    def insert_values(self, where, values, which=""):
        """Insert values into table's given column.

        Args:
            which: `which` indicates the attributes you will insert in.

        Return:
            Return True If it's SUCCESS,
            otherwise return FALSE.
        """
        if which == "":
            command = 'INSERT INTO ' + where + ' VALUES ' + values + ' ;'
        else:
            command = 'INSERT INTO ' + where + '(' + which + ') VALUES ' + values + ' ;'
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(command)
        except Exception:
            print(command)
            self.connect.rollback()
            return False
        self.connect.commit()
        return True


