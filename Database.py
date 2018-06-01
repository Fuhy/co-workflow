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
            command = "SELECT {} FROM {} ;".format(what, where)
        else:
            command = "SELECT {} FROM {} WHERE {};".format(
                what, where, predicate)

        cursor = self.connect.cursor()
        try:
            cursor.execute(command)
        except Exception:
            print(command)
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
            command = "INSERT INTO {} VALUES {} ;".format(where, values)
        else:
            command = "INSERT INTO {}({}) VALUES {} ;".format(
                where, which, values)

        try:
            with self.connect.cursor() as cursor:
                cursor.execute(command)
        except Exception:
            print(command)
            self.connect.rollback()
            return False

        self.connect.commit()
        return True

    def delete_from_where(self, where, predicate=""):
        """Delete from table where predicates are True.

        Return:
            Return True If it's SUCCESS,
            otherwise return FALSE.
        """
        if predicate == "":
            command = "DELETE FROM {} ;".format(where)
        else:
            command = "DELETE FROM {} WHERE {} ;".format(where, predicate)

        try:
            with self.connect.cursor() as cursor:
                cursor.execute(command)
        except Exception:
            print(command)
            self.connect.rollback()
            return False

        self.connect.commit()
        return True

    def update_set_where(self, where, operate, predicate=""):
        """Update table Set operates where predicate is True.

        Return:
            Return True If it's SUCCESS,
            otherwise return FALSE.
        """
        if predicate == "":
            command = "UPDATE {} SET {} ;".format(where, operate)
        else:
            command = "UPDATE {} SET {} WHERE {} ;".format(where, operate, predicate)

        try:
            with self.connect.cursor() as cursor:
                cursor.execute(command)
        except Exception:
            print(command)
            self.connect.rollback()
            return False

        self.connect.commit()
        return True
