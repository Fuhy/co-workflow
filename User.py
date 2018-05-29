import random
from HashMaker import HashMaker

class UserInfo(object):
    """docstring for UserInfo"""

    def __init__(self, user_name):
        self.user_name = user_name
        self.user_ID = HashMaker().hash_user()

    def get_ID(self):
        return self.user_ID

    def rename(self, new_user_name)
        self.user_name = new_user_name

    # Log in and Sign up



