# co-workflow

### 一些可能有用的文件

#### Database

使用了`PyMySQL`库来进行数据库操作。将执行语句封装成了`select_from_where()`,  `insert_values()`,  `update_set_where()`, `delete_from_where()`四个基本操作。实例化`DataManager`类时，先会与数据库建立连接。每个操作会根据函数参数动态生成SQL命令并作为事务执行，若中途失败则会回滚。

#### WebServer

使用`Tornado`库将上面的`Database`封装成一个使用**HTTP协议**的数据库**服务器**。实现了四个处理函数`SelectHandler`, `InsertHandler`, `DeleteHandler`, `UpdateHandler`, 将HTTP报文转化成具体的数据库操作。

#### Client

将`request`库中的HTTP请求操作封装成`select`, `insert`, `delete`, `update`操作, 与上文中的WebServer通信。

#### MyPickle

`Pickle`库能将**内存**中的对象**序列化**成字符串，或把序列化的对象装载进内存中。换而言之，就是能把对象以字节的形式存储起来。`MyPickle`库封装了`Pickle`。

`select_from_where()`语句会传回元组列表(e.g. `[(a,b,c,),(d,e,f,),]`)。与其在客户端将收到的字符串手动转换成列表，不如直接传递整个对象。

使用`MyPickle`库，WebServer会将结果序列化后发送给Client，而Client再将其实例化，并返回这个列表。