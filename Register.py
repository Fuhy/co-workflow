import hashlib
import Database
from HashMaker import HashMaker
from PathOrName import *


def sign_up(account, password):
    if HashMaker().check_user_name_exist(account):
        return False
    else:
        db = Database.DataManager(DATABASE)
        user_ID = HashMaker().hash_user()
        code = sha1_encode(password)
        values = "({},'{}','{}')".format(user_ID,account,code)
        db.insert_values('`User`', values, which="user_ID, user_name, password")
        db.close()
        return True


def log_in(account, password):
    db = Database.DataManager(DATABASE)
    predicate = "`user_name` = '{}' ".format(account)
    result = db.select_from_where('password', 'User', predicate).fetchone()
    db.close()

    if sha1_encode(password) == result[0]:
        return True
    else:
        return False


#return 32bit hex string
def sha1_encode(password):
    result = hashlib.sha1()
    result.update(password.encode())
    return result.hexdigest()


