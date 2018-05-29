class Constraint(object):
    """docstring for Constraint"""

    def __init__(self, graph_ID):
        self.graph_ID = graph_ID
        self.records = set()

    def add_constraintt(self,relation):
        self.records.add(relation)

    def get_all_constraint(self):
        return self.records