| Schema       |                                                   |
| ------------ | ------------------------------------------------- |
| User         | **user_id**, user_name, password                  |
| User_Info    | **user_id**, user_name, nick_name, gender, about  |
| DAG          | **graph_id**, graph_name, owner_id, abstract      |
| DAG_Group    | **graph_id**, **user_id**                         |
| DAG_Node     | **task_id**, graph_id                             |
| DAG_Edge     | **begin_TID, end_TID**                            |
| Node         | **task_id**, owner_id, task_name, version, status |
| Node_Group   | **task_id, user_id**                              |
| Node_Details | **task_id**, abstract, due_date                   |







