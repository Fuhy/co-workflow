class NodeInfo(object):
    """docstring for NodeInfo"""

    def __init__(self, owner_ID, task_ID):
        self.task_ID = task_ID
        self.owner_ID = owner_ID
        self.group = set()
        self.version = 0
        self.status = False

    # Get something
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

    # Modify
    def update_version(self):
        self.version += 1

    def reverse_status(self):
        self.status = not self.status

    # TODO(): Handle the exception AND the database
    # check_user_exist()
    # User should be identified with ID
    # or there will be lots of modifying when rename a user.
    def alter_owner(self, owner_ID):
        # owner_name should be a validated account
        self.owner_ID = owner_ID

    def add_group_member(self, member_list):
        for member in member_list:
            self.group.add(member)

    def delete_group_member(self, member_list):
        for member in member_list:
            self.group.remove(member)

    def rename_task():
        pass
