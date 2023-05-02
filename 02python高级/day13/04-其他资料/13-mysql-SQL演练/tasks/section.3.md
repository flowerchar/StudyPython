# 企业笔试题

1. Python 中操作 Mysql 步骤

   ![python与mysql交互流程](../pytosql.png)

   代码实现:

   ```python
   #首先安装包-pymysql sudo pip install pymysql
   #之后在程序中调用 from pymysql import * 
   ''' connection 对象 用于建立与数据库的连接 创建对象：调用 connect()方法 ''' 
   conn = connect(参数列表）
   ''' 参数列表：
   host:连接 MySQL 主机，如果是本机则为”localhost“
   port:连接 MySQL 主机端口，默认 3306
   database:数据库名称
   user：连接的用户名
   password：连接的密码
   charset:通信采用的编码方式，推荐采用 utf8
   ''' 
   ''' connection 对象方法
   close() 关闭连接
   commit() 提交
   rollback() 回滚
   cursor() 返回
   cursor 对象，用于执行 sql 语句
   例如：select,insert,update,delete ''' 
   cs1 = conn.cursor()
   ''' cursor 对象方法
   close() 关闭
   execute(operation[,parameters])执行语句，返回受影响的行数，主要用于执行 insert、update、delete 语句，
   也可以执行 create、alter、drop 等语句
   fetchone()执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
   fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回 ''' 
                  
   ''' 
   cursor 对象属性
   rowcount 只读属性，表示最近一次
   execute()执行后受影响的行数
   connection 获得当前连接对象 ''' 
   #例子
   #创建 Connection 连接
   conn = connect(host='localhost', port=3306, user='root', password='mysql', database='python1', charset='utf8')
   #获得 Cursor 对象 
   cs = conn.cursor()
   # 更新 
   # sql = 'update students set name="刘邦" where id=6' 
   #删除
   # sql = 'delete from students where id=6' 
   #执行 select 语句，并返回受影响的行数：查询一条学生数据
   sql = 'select id,name from students where id = 7' 
   # sql = 'SELECT id,name FROM students WHERE id = 7' 
   count=cs.execute(sql)
   #打印受影响的行数
   print count
   ```

   

2. Sql 注入是如何产生的，如何防止？

3. Mysql 数据库中怎么实现分页？

4. 数据库的设计？

   

   
