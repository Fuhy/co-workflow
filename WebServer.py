import random
import tornado.ioloop
import tornado.web
from Database import DataManager
from MyPickle import *
import hashlib


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/select*", SelectHandler),
        (r"/insert*", InsertHandler),
        (r"/delete*", DeleteHandler),
        (r"/update*", UpdateHandler),
        (r"/login*", LoginHandler),
        (r"/signup*", SignupHandler),
    ])


class SelectHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = DataManagers()

    def get(self, *args, **kwarg):
        token = self.get_argument('token')
        if not check_login_status(token):
            self.write(write_to_stream('Authorised Failed!'))
            return
        content = self.get_argument('content')
        table = self.get_argument('table')
        predicate = self.get_argument('predicate', "")
        result = self.db.select_from_where(content, table, predicate)
        if result is not None:
            result = result.fetchall()
        else:
            result = []
        value = write_to_stream(result)
        self.write(value)


class InsertHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = DataManager()

    def post(self, *args, **kwarg):
        token = self.get_argument('token')
        if not check_login_status(token):
            self.write('Authorised Failed!')
            return
        table = self.get_argument('table')
        data = self.request.body.decode()
        column = self.get_argument('column', "")
        # print(table,column,data)
        self.write(str(self.db.insert_values(table, data, column)))


class UpdateHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = DataManager()

    def post(self, *args, **kwarg):
        token = self.get_argument('token')
        if not check_login_status(token):
            self.write('Authorised Failed!')
            return
        table = self.get_argument('table')
        predicate = self.get_argument('predicate', "")
        keys = tuple(
            [word[1:-1] for word in self.get_argument('keys').split(',')])
        values = tuple([
            word[1:-1] if word[0] == "'" else word
            for word in self.get_argument('values').split(',')
        ])
        # print(table,keys,values,predicate)
        self.write(
            str(self.db.update_set_where(table, keys, values, predicate)))


class DeleteHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = DataManager()

    def post(self, *args, **kwarg):
        token = self.get_argument('token')
        if not check_login_status(token):
            self.write('Authorised Failed!')
            return
        table = self.get_argument('table')
        predicate = self.request.body.decode()
        # print(table,predicate)
        self.write(str(self.db.delete_from_where(table, predicate)))


class LoginHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = DataManager()

    def post(self, *args, **kwarg):
        account = self.get_argument('account')
        password = self.request.body.decode()
        predicate = "`user_name` = '{}' ".format(account)
        if (self.log_in(account, password)):
            result = self.db.select_from_where('password', 'User',
                                               predicate).fetchone()[0]
            self.write(str(result))
        else:
            self.write(str(False))

    def log_in(self, account, password):
        predicate = "`user_name` = '{}' ".format(account)
        result = self.db.select_from_where('password', 'User',
                                           predicate).fetchone()
        if HashMaker().sha1_encode(password) == result[0]:
            return True
        else:
            return False


class SignupHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = DataManager()

    def post(self, *args, **kwarg):
        account = self.get_argument('account')
        password = self.request.body.decode()
        self.write(str(self.sign_up(account, password)))

    def sign_up(self, account, password):
        if HashMaker().check_user_name_exist(account):
            return False
        else:
            user_ID = HashMaker().hash_user()
            code = HashMaker().sha1_encode(password)
            values = "({},'{}','{}')".format(user_ID, account, code)
            self.db.insert_values(
                '`User`', values, which="user_ID, user_name, password")
            return True


class HashMaker(object):
    def __init__(self):
        self.db = DataManager()

    def sha1_encode(self, password):
        result = hashlib.sha1()
        result.update(password.encode())
        return result.hexdigest()

    def hash_user(self):
        value = (random.randint(0, 100000000) % 100000)
        if self.check_user_exist(value):
            return self.hash_user()
        else:
            return value

    def check_user_name_exist(self, account):
        result = self.db.select_from_where(
            '*', 'User', "user_name = '{}'".format(account)).fetchall()
        if len(result) == 0:
            return False
        else:
            return True

    def check_user_exist(self, value):
        result = self.db.select_from_where(
            '*', 'User', "user_ID = '{}'".format(value)).fetchall()
        if len(result) == 0:
            return False
        else:
            return True


def check_login_status(token):
    if token in [
            i for item in DataManager().select_from_where('password', 'User')
            .fetchall() for i in item
    ]:
        return True
    else:
        return False


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
