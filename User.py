import random
from HashMaker import HashMaker
from Register import *
import Database


#TODO(): Since Signed up, then we have user_ID,user_name(account),and password.
class UserInfo(object):
    """docstring for UserInfo"""

    def __init__(self, user_ID):
        self.user_ID = user_ID
        self.restore_user(user_ID)

    def restore_user(self, user_ID):
        db = Database.DataManager(DATABASE)
        self.user_name = db.select_from_where(
            'user_name', 'User',
            "user_ID = '{}'".format(user_ID)).fetchone()[0]
        db.close()
        self.save_state()

    def save_state(self):
        db = Database.DataManager(DATABASE)
        #TODO: EXPANDS THE ATTRIBUTES HERE
        attributes = ('user_name', )
        values = (self.user_name, )
        db.update_set_where('User', attributes, values,
                            " user_id = '{}' ".format(self.user_ID))

    def get_ID(self):
        return self.user_ID

    def update_password(self, old_password, new_password):
        if sha1_encode(
                str(old_password)) == Database.DataManager().select_from_where(
                    'password', 'User',
                    "user_id = {}".format(self.user_ID)).fetchone()[0]:

            Database.DataManager().update_set_where(
                'User', ('password', ), (sha1_encode(str(new_password)), ),
                " user_id = {} ".format(self.user_ID))
            return True
        else:
            return False

    def rename(self, new_user_name):
        self.user_name = new_user_name

    # Log in and Sign up
