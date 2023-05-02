# 每日必会题

1. **简述使用pymysql模块对数据库编程时，需要经过哪几步？每一步的作用是什么？**

   使用pymysql模块进行数据库编程时，需要经过五步。

   1.     建立数据库连接对象

   通过服务器的主机，端口，帐号，密码，以及要操作的数据库来确定程序和数据库之间的连接

   2.     获取游标对象

   用来对数据库执行操作的方法的对象，

   3.     执行SQL语句

   具体的数据库操作在这步完成，主要完成SQL语句的定义，执行，结果的获取。

   4.     关闭游标对象

   关闭数据库连接对象

   ​

2. **在使用pymysql 模块进行连接数据时，有几种连接方式？**

   只有三种：

   connect / Connection / Connect

    

   这两个函数实际都是指向同一个函数的三个不同的引用，

   模块中使用赋值的方式实现：

    

   connect = Connection = Connect

   ​

3. 连接数据，对员工表插入一条新数据

   并查询结果，将结果显示输出

   ```sql
   ''' 连接数据库，插入新数据并查询结果 '''

   # 导入模块
   from pymysql import *

   # 创建Connection连接
   conn = connect(host='localhost', port=3306, database='flower_db', user='root', password='123123', charset='utf8')

   # 获得Cursor对象
   cur = conn.cursor()

   # 插入SQL
   insert_str = '''  insert into t_staff values(0,'Boss','male',45,15,90000,2); '''

   # 执行插入语句
   cur.execute(insert_str)

   # 提交操作
   conn.commit()

   # 查询SQL
   query_str = """ select * from t_staff"""

   # 执行sql
   cur.execute(query_str)

   # 获取结果
   content = cur.fetchall()

   # 遍历结果并输出
   for temp in content:
       print(temp)

   # 3. 关闭
   cur.close()
   conn.close()

   ```

   ​

4. 查询所有工资大于20000的女性员工所在的部门名称

   ```sql
   ''' 连接数据库，插入新数据并查询结果 '''

   # 导入模块
   from pymysql import *

   # 创建Connection连接
   conn = connect(host='localhost', port=3306, database='flower_db', user='root', password='123123', charset='utf8')

   # 获得Cursor对象
   cur = conn.cursor()

   # 查询SQL
   query_str = """ select * from t_staff left  join t_department on t_staff.d_id = t_department.id where salary > 20000 and gender = 'female';"""

   # 执行sql
   cur.execute(query_str)

   # 获取结果
   content = cur.fetchall()

   # 遍历结果并输出
   for temp in content:
       print(temp)

   # 3. 关闭
   cur.close()
   conn.close()

   ```

   ​