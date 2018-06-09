import tornado.ioloop
import tornado.web
from Database import DataManager
from MyPickle import *


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/select*", SelectHandler),
        (r"/insert*", InsertHandler),
        (r"/delete*", DeleteHandler),
        (r"/update*", UpdateHandler),
    ])


class SelectHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = DataManager()

    def get(self, *args, **kwarg):
        content = self.get_argument('content')
        table = self.get_argument('table')
        predicate = self.get_argument('predicate', "")
        result = self.db.select_from_where(content, table,
                                           predicate).fetchall()
        value = write_to_stream(result)
        self.write(value)


class InsertHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = DataManager()

    def post(self, *args, **kwarg):
        table = self.get_argument('table')
        data = self.request.body.decode()
        column = self.get_argument('column', "")
        # print(table,column,data)
        self.write(str(self.db.insert_values(table, data, column)))


class UpdateHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = DataManager()

    def post(self, *args, **kwarg):
        table = self.get_argument('table')
        predicate = self.get_argument('predicate',"")
        keys = tuple(
            [word[1:-1] for word in self.get_argument('keys').split(',')])
        values = tuple([
            word[1:-1] if word[0] == "'" else word
            for word in self.get_argument('values').split(',')
        ])
        # print(table,keys,values,predicate)
        self.write(str(self.db.update_set_where(table,keys,values,predicate)))



class DeleteHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = DataManager()

    def post(self, *args, **kwarg):
        table = self.get_argument('table')
        predicate = self.request.body.decode()
        # print(table,predicate)
        self.write(str(self.db.delete_from_where(table, predicate)))


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
