# 每日必会题

1. **列举常见关系型数据库。**

   oracle: 银行,电信等项目

   ms sql server：在微软的项目中使用

   sqlite：轻量级数据库，主要应用在移动平台

   mysql：web时代使用最广泛的关系型数据库

   ​

2. **结构化查询语言SQL中，定义的DML，DQL分别包括哪些操作？**

   DML： 数据操作语言，包括insert插入，update 更新，delete删除操作

   DQL： 数据查询语言，包括 select 查询操作

   ​

3. **在使用命令终端连接数据库时，需要知道数据库的哪些条件？**

   数据库服务器的IP地址

   数据库服务器的端口号

   数据库登陆帐号和密码

   ​

4. **数据库中常用字段类型有哪些？**

   1.   整数类型
   2.   浮点类型
   3.   字符串类型
   4.   枚举类型
   5.   日期类型

5. 数据操作需要在MySQL数据库环境中进行操作练习。

   ​

   创建 公司 数据库 字符集 utf-8

    

   建立部门表

   部门编号： 整型，主键自动增长

   部门名称 ： 字符型 长度 20

    

   建立员工表，包含下列字段 ：

   员工编号 ： 整型，主键自动增长，

   员工姓名 ： 字符型 长度为20

   员工性别： 枚举类型 {‘male’，‘female’}

   员工年龄： 整型 

   员工工龄： 整型

   员工工资： 浮点类型，小数点保留两位

   员工部门编号：整型

   ```sql
   mysql> create database flower_db charset=utf8;

   mysql> use flower_db

   mysql> create table t_department( id int(3) unsigned zerofill auto_increment primary key, name char(20) );

   mysql> create table t_staff(
       -> id int(5) unsigned zerofill auto_increment primary key,
       -> name char(20),
       -> gender enum('male','female'),
       -> age int,
       -> working_years int,
       -> salary double(8,2),
       -> d_id int
       -> );

   ```

6. 向表格中插入数据 

   数据可以使用下面指定的，也可以自行插入数据

   ```sql
   mysql> insert into t_department values(0,'人事部');

   mysql> insert into t_department values(0,'销售部');

   mysql> insert into t_department values(0,'开发部');

   mysql> insert into t_staff values(0,'Tom','male',25,1,4500,1);

   mysql> insert into t_staff values(0,'Jack','male',28,3,6500,1);

   mysql> insert into t_staff values(0,'Rose','female',24,1,8500,2);

   mysql> insert into t_staff values(0,'Alice','female',24,1,8500,2);

   mysql> insert into t_staff values(0,'Alex','female',26,1,8500,2);

   mysql> insert into t_staff values(0,'Tony','male',30,4,12000,2);

   mysql> insert into t_staff values(0,'Lily','female',35,7,25000,2);

   mysql> insert into t_staff values(0,'Lucy','female',32,4,20000,2);

   mysql> insert into t_staff values(0,'Rose','female',26,2,10000,3);

   mysql> insert into t_staff values(0,'Max','male',28,3,15000,3);

   mysql> insert into t_staff values(0,'Jean','female',22,1,10000,3);

   mysql> insert into t_staff values(0,'Kate','female',23,1,10000,3);

   mysql> insert into t_staff values(0,'Karry','male',42,15,50000,3);

   mysql> insert into t_staff values(0,'Finn','male',35,7,30000,3);

   mysql> insert into t_staff values(0,'Kylo','male',32,6,35000,3);

   mysql> insert into t_staff values(0,'Rose','female',24,1,15000,3);

   ```

7. 将Tony的部门调整到开发部

    

   将工资低于10000的员工加薪1000

   ```sql
   mysql> update t_staff set d_id = 3 where name = 'Tony';

   mysql> update t_staff set salary = salary + 1000 where salary < 10000;

   ```

8. 删除工资大于30000 的员工

   ```sql
   mysql> delete from t_staff where salary > 30000;
   ```

   ​

