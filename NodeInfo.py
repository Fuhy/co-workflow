from Database import DataManager
from PathOrName import *
from HashMaker import HashMaker
from Client import *


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
        self._graph_ID = select('graph_id', 'DAG_Node',
                                'task_id = {}'.format(task_ID))

        if HashMaker().check_task_exist(task_ID):
            self.restore_node(task_ID)
        else:
            self.init_node(task_ID, owner_ID)

    #TODO(): DAG_Node -> NodeInfo
    # A task must binds to a graph.
    def init_node(self, task_ID, owner_ID):
        self.owner_ID = select(
            'owner_id', 'DAG',
            "graph_id = (SELECT graph_id FROM DAG_Node WHERE task_id = {})".
            format(task_ID))[0][0]
        self.save_state()

    def restore_node(self, task_ID):
        (self.task_ID, self.owner_ID,
         self.task_name, self.version, self.status) = select(
             '*', 'NodeInfo', "task_ID = {}".format(task_ID))[0]
        group = select('user_id', 'NodeGroup', "task_ID = {}".format(task_ID))
        for member in [member for item in group for member in item]:
            self.group.add(member)

    def save_state(self):
        if HashMaker().check_task_exist(self.task_ID):
            attributes = "'owner_ID','task_name','version','status'"
            values = "'{}','{}','{}','{}'".format(
                self.owner_ID, self.task_name, self.version, self.status)
            update('NodeInfo', attributes, values, " task_id = '{}' ".format(
                self.task_ID))
        else:
            values = "('{}','{}','{}','{}','{}')".format(
                self.task_ID, self.owner_ID, self.task_name, self.version,
                self.status)
            insert('NodeInfo', values)

        self.update_version()

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
        update('NodeInfo',"'version'",self.version,"task_ID = {}".format(self.task_ID))

    def reverse_status(self):
        self.status = not self.status

    def alter_owner(self, new_owner_ID):
        self.owner_ID = new_owner_ID

    def add_group_member(self, member_list):
        for member in member_list:
            if insert('NodeGroup', "({},'{}')".format(self.task_ID, member)):
                self.group.add(member)
                self.update_version()

    def delete_group_member(self, member_list):
        for member in member_list:
            if delete('NodeGroup', " task_id = {} and user_id = {} ".format(
                    self.task_ID, member)):
                self.group.remove(member)
                self.update_version()

    def alter_status(self, new_status):
        self.status = new_status

    def rename_task(self, new_task_name):
        self.task_name = new_task_name
