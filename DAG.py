from copy import copy, deepcopy
from collections import OrderedDict


class DAG(object):
    """docstring for DAG"""

    def __init__(self):
        self.reset_graph()

    def reset_graph(self):
        self.graph = OrderedDict()

    # Tools
    def size(self):
        return len(self.graph)

    def validate(self):
        """ Returns (Boolean, message) of whether DAG is valid. """
        pass

    def topological_sort(self, graph=None):
        """ Returns a topological ordering of the DAG.

        Raises an error if this is not possible (graph is not valid).
        """
        pass

    # Edit Node
    def add_node(self):
        pass

    def delete_node(self):
        pass

    def rename_task(self, old_task_name, new_task_name):
        """ Not just change the nodes but also the edges """
        pass

    # Edit Edge
    def add_edge(self):
        pass

    def delete_edge(self):
        pass

    # Show Something
    def get_one_predecessor(self, node):
        pass

    def show_predecessors(self, node):
        """ Returns a list of *all* predecessors of the given node """
        pass

    def show_downstream(self, node):
        """ Returns a list of all nodes this node has edges direct towards. """
        pass

    def show_all_downstream(self, node):
        pass


class Node(object):
    """docstring for Node"""

    def __init__(self, task_name, last_task):

        self.name = task_name
        # self.ID = ID()
        # self.info = Info()     class INFO
        self._last_node = last_task

        # some should be default to describe the relation
        self.next_edge = set()
        self.last_edge = set()
