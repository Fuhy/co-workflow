from HashMaker import HashMaker
from DAG import DAG
from User import UserInfo
from NodeInfo import NodeInfo
from Database import DataManager
from PathOrName import *
import pymysql



def fetch_gid(graph_name)
    db = Database.DataManager(DATABASE)
    predicate = "`graph_name` = '{}' ".format(graph_name)
    result = db.select_from_where('graph_id', 'DAG', predicate).fetchone()
    db.close()
    return result[0]

def fetch_uid(account):
    db = Database.DataManager(DATABASE)
    predicate = "`user_name` = '{}' ".format(account)
    result = db.select_from_where('user_id', 'User', predicate).fetchone()
    db.close()
    return result[0]


def fetch_nid(node_name):
    db = Database.DataManager(DATABASE)
    predicate = "`task_name` = '{}' ".format(node_name)
    result = db.select_from_where('task_id', 'NodeInfo', predicate).fetchone()
    db.close()
    return result[0]



def new_project(account, graph_name="New Project"):
    #create a new project
    g_id = HashMaker.hash_graph()
    u_id = fetch_uid(account)
    task = DAG(g_id, u_id, graph_name)
    #create the new DAG

    task.rename_graph(graph_name)
    #rename the DAG

    db = Database.DataManager(DATABASE)

    values = "({},'{}',{})".format(g_id, graph_name, u_id)
    db.insert_values('DAG', values)
    #insert to DAG

    values = "({},{})".format(g_id, u_id)
    db.insert_values('DAG_Group', values)
    #insert to DAG_Group

    db.close()

    return task



def new_task(account, graph_name, task_name = "New Task"):
    #create a new task
    u_id = fetch_uid(account)
    g_id = fetch_gid(graph_name)
    task = DAG(g_id, u_id)

    n_id = HashMaker.hash_task()
    task.add_node(n_id)
    node_info = NodeInfo(n_id, u_id, task_name)
    #add the first node

    db = Database.DataManager(DATABASE)

    values = "({},{})".format(g_id, n_id)
    db.insert_values('DAG_Node', values)
    #insert to DAG_Node

    values = "({},{},'{}',{},{})".format(n_id, u_id, task_name, node_info.version, node_info.status)
    db.insert_values('NodeInfo', values)
    #insert to NodeInfo

    values = "({},{})".format(n_id, u_id)
    db.insert_values('NodeGroup', values)
    #insert to NodeGroup
    
    db.close()

    return node_info