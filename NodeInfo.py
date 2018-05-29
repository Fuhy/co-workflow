class NodeInfo(object):
    """docstring for NodeInfo

    Attributes:
        task_ID: A string for identifing tasks.
        task_name:  A string.
        owner_ID: A string for identifing owner. 
        group: A set which contains user's ID
        version: An integer count of times we have Modified the Infomation.
        status: Bool value.
    """

    def __init__(self, owner_ID, task_ID, task_name):
        self.task_ID = task_ID
        self.owner_ID = owner_ID
        self.task_name = 'new_task'
        self.group = set()
        self.version = 0
        self.status = False


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
