import pymysql
from HashMaker import *
from DAG import DAG
from User import UserInfo
from NodeInfo import NodeInfo
from Client import *


class GraphPic(object):
    """docstring for GraphPic"""

    def __init__(self, graph_ID):
        self.graph = DAG(graph_ID)

    def analyse_graph(self):
        self.node_level = dict()
        # describe level
        for node in self.graph.graph.keys():
            parents = self.graph.show_all_predecessors(node)
            level = len(parents)
            if self.node_level.get(level):
                self.node_level[level].add(node)
            else:
                self.node_level[level] = set()
                self.node_level[level].add(node)
        # find the max level
        self.max_nodes_in_one_level = 0
        for level in self.node_level.keys():
            self.max_nodes_in_one_level = len(self.node_level[level]) if (len(
                self.node_level[level]) > self.max_nodes_in_one_level) else self.max_nodes_in_one_level

