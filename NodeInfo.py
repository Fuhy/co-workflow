from Database import DataManager
from PathOrName import *
from HashMaker import HashMaker


class NodeInfo(object):
    """docstring for NodeInfo

    Cautions:
        The table `DAG_Node` must be set up BEFORE you instantiate a NEW node!

    Attributes:
        task_ID: A string for identifing tasks.
        task_name:  A string.
        owner_ID: A string for identifing owner. 
        group: A set which contains user's ID
        version: An integer count of times we have Modified the Infomation.
        status: Bool value.
    """

    def __init__(self, task_ID, owner_ID="", task_name=""):
        self.task_ID = task_ID
        self.owner_ID = owner_ID
        self.task_name = 'New Task'
        self.group = set()
        self.version = 0
        self.status = False

        if HashMaker().check_task_exist(task_ID):
            self.restore_node(task_ID)
        else:
            self.init_node(task_ID, owner_ID)

    #TODO(): DAG_Node -> NodeInfo
    # A task must binds to a graph.
    def init_node(self, task_ID, owner_ID):
        db = DataManager(DATABASE)

        owner_ID = db.select_from_where(
            'owner_id', 'DAG',
            "graph_id = (SELECT graph_id FROM DAG_Node WHERE task_id = {})".
            format(task_ID)).fetchone()[0]

        values = "('{}','{}','{}','{}','{}')".format(task_ID, owner_ID,
                                                     'New Task', 0, False)
        db.insert_values('NodeInfo', values)
        db.close()

    def restore_node(self, task_ID):
        db = DataManager(DATABASE)
        (self.task_ID, self.owner_ID, self.task_name,
         self.version, self.status) = db.select_from_where(
             '*', 'NodeInfo', "task_ID = {}".format(task_ID)).fetchall()[0]
        group = db.select_from_where(
            'user_id', 'NodeGroup', "task_ID = {}".format(task_ID)).fetchall()
        for member in [member for item in group for member in item]:
            self.group.add(member)
        db.close()

    def get_task_ID(self):
        return self.task_ID

    def get_version(self):
        return self.version

    def get_owner_ID(self):
        return self.owner_ID

    def get_status(self):
        return self.status

    def get_group(self):
        return self.group()

    def update_version(self):
        self.version += 1

    def reverse_status(self):
        self.status = not self.status

    # TODO(): Handle the exception AND the database
    # check_user_exist()
    # User should be identified with ID
    # or there will be lots of modifying when rename a user.

    def alter_owner(self, new_owner_ID):
        self.owner_ID = new_owner_ID

    def add_group_member(self, member_list):
        for member in member_list:
            self.group.add(member)

    def delete_group_member(self, member_list):
        for member in member_list:
            self.group.remove(member)

    def alter_status(self, new_status):
        self.status = new_status

    def rename_task(self, new_task_name):
        self.task_name = new_task_name
