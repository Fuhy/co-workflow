import pymysql
from PathOrName import *


class DataManager(object):
    """docstring for DataManager"""

    def __init__(self,
                 database=DATABASE,
                 host=DBHOST,
                 user=DBUSER,
                 passwd=DBPASSWORD):
        self.connect = self._connect(database, host, user, passwd)

    def _connect(self, database, host, user, passwd, charset='utf8'):
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

    def update_set_where(self, where, attributes, values, predicate=""):
        """Update table Set the attributes in the values where predicate is True.

        Args:
            attributes: a tuple of the attributes you wanna modified.
            values: the values you wanna assign them into the attributes. 

        Cautions:
            attributes and values should be passed in the correct orders.

        Return:
            Return True If it's SUCCESS,
            otherwise return FALSE.
        """
        if len(attributes) != len(values):
            return False

        manipulation = []

        for i, name in enumerate(attributes):
            if i != len(attributes) - 1:
                manipulation.append(" `{}` = '{}' , ".format(name, values[i]))
            else:
                manipulation.append(" `{}` = '{}' ".format(name, values[i]))

        if predicate == "":
            command = "UPDATE {} SET {} ;".format(where, "".join(manipulation))
        else:
            command = "UPDATE {} SET {} WHERE {} ;".format(
                where, "".join(manipulation), predicate)
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(command)
        except Exception:
            print(command)
            self.connect.rollback()
            return False

        self.connect.commit()
        return True
