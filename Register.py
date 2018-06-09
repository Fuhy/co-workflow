import hashlib
import Database
from HashMaker import HashMaker
from PathOrName import *
from Client import *

def sign_up(account, password):
    if HashMaker().check_user_name_exist(account):
        return False
    else:
        user_ID = HashMaker().hash_user()
        code = sha1_encode(password)
        values = "({},'{}','{}')".format(user_ID,account,code)
        insert('`User`', values, which="user_ID, user_name, password")
        return True


def log_in(account, password):
    predicate = "`user_name` = '{}' ".format(account)
    result = select('password', 'User', predicate)[0]

    if sha1_encode(password) == result[0]:
        return True
    else:
        return False


#return 32bit hex string
def sha1_encode(password):
    result = hashlib.sha1()
    result.update(password.encode())
    return result.hexdigest()


