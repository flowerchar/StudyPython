# 每日练习题

1. 传统记录数据方式的缺点

   - 不易保存
   - 备份困难
   - 查找不便

   ​

2. 使用文件记录数据的特点

   - 使用简单，例如python中的open可以打开文件，用read/write对文件进行读写，close关闭文件
   - 对于数据容量较大的数据，不能够很好的满足，而且性能较差
   - 不易扩展

   ​

3. 使用数据库记录数据的特点

   - 持久化存储
   - 读写速度极高
   - 保证数据的有效性
   - 对程序支持性非常好，容易扩展

   ​

4. 关系型数据库核心元素(可以类比excel来理解)

   - 数据行(记录)
   - 数据列(字段)
   - 数据表(数据行的集合)
   - 数据库(数据表的集合)

   ​

5. 关系型数据库主要产品有哪些

   - oracle：在以前的大型项目中使用,银行,电信等项目
   - mysql：web时代使用最广泛的关系型数据库
   - ms sql server：在微软的项目中使用
   - sqlite：轻量级数据库，主要应用在移动平台

   ​

6. 什么是SQL

   SQL(Structured Query Language)是结构化查询语言，是一种用来操作RDBMS的数据库语言，当前关系型数据库都支持使用SQL语言进行操作,也就是说可以通过 SQL 操作 oracle,sql server,mysql,sqlite 等等所有的关系型的数据库

   ​

7. mysql的特点有哪些?

   - 使用C和C++编写，并使用了多种编译器进行测试，保证源代码的可移植性
   - 支持多种操作系统，如Linux、Windows、AIX、FreeBSD、HP-UX、MacOS、NovellNetware、OpenBSD、OS/2 Wrap、Solaris等
   - 为多种编程语言提供了API，如C、C++、Python、Java、Perl、PHP、Eiffel、Ruby等
   - 支持多线程，充分利用CPU资源
   - 优化的SQL查询算法，有效地提高查询速度
   - 提供多语言支持，常见的编码如GB2312、BIG5、UTF8
   - 提供TCP/IP、ODBC和JDBC等多种数据库连接途径
   - 提供用于管理、检查、优化数据库操作的管理工具
   - 大型的数据库。可以处理拥有上千万条记录的大型数据库
   - 支持多种存储引擎
   - MySQL 软件采用了双授权政策，它分为社区版和商业版，由于其体积小、速度快、总体拥有成本低，尤其是开放源码这一特点，一般中小型网站的开发都选择MySQL作为网站数据库
   - MySQL使用标准的SQL数据语言形式
   - Mysql是可以定制的，采用了GPL协议，你可以修改源码来开发自己的Mysql系统
   - 在线DDL更改功能
   - 复制全局事务标识
   - 复制无崩溃从机
   - 复制多线程从机

   ​

8. mysql的数据类型有哪些?

   - 常用数据类型如下：
     - 整数：int，bit
     - 小数：decimal
     - 字符串：varchar,char
     - 日期时间: date, time, datetime
     - 枚举类型(enum)
   - 特别说明的类型如下：
     - decimal表示浮点数，如decimal(5,2)表示共存5位数，小数占2位
     - char表示固定长度的字符串，如char(3)，如果填充'ab'时会补一个空格为`'ab '`
     - varchar表示可变长度的字符串，如varchar(3)，填充'ab'时就会存储'ab'
     - 字符串text表示存储大文本，当字符大于4000时推荐使用
     - 对于图片、音频、视频等文件，不存储在数据库中，而是上传到某个服务器上，然后在表中存储这个文件的保存路径
   - 更全的数据类型可以参考<http://blog.csdn.net/anxpp/article/details/51284106>

   ​

9. mysql的约束有哪些?

   - 主键primary key：物理上存储的顺序
   - 非空not null：此字段不允许填写空值
   - 惟一unique：此字段的值不允许重复
   - 默认default：当不填写此值时会使用默认值，如果填写时以填写为准
   - 外键foreign key：对关系字段进行约束，当为关系字段填写值时，会到关联的表中查询此值是否存在，如果存在则填写成功，如果不存在则填写失败并抛出异常
   - 说明：虽然外键约束可以保证数据的有效性，但是在进行数据的crud（增加、修改、删除、查询）时，都会降低数据库的性能，所以不推荐使用，那么数据的有效性怎么保证呢？答：可以在逻辑层进行控制

   ​

10. 什么是数据完整性?

   - 一个数据库就是一个完整的业务单元，可以包含多张表，数据被存储在表中
   - 在表中为了更加准确的存储数据，保证数据的正确有效，可以在创建表的时候，为表添加一些强制性的验证，包括数据字段的类型、约束

   ​

11. 命令行登录mysql数据库

    ```shell
    mysql -u用户名 -p密码
    ```

    ​

12. 查看所有数据库

    ```sql
    show databases;
    ```

    ​

13. 创建test数据库

    **注意不要忘记charset**

    ```sql
    create database test charset=utf8;
    ```

    ​

14. 使用test数据库

    ```sql
    use test;
    ```

    ​

15. 查看test数据库内的所有数据表

    ```sql
    show tables;
    ```

    ​

16. 查看数据库的创建语句

    ```sql
    show create database test;
    ```

    ​

17. 创建test数据表

    ```sql
    create table test(
    	column1 datatype contrai,
        column2 datatype,
        column3 datatype,
        .....
    );
    ```

    ​

18. 查看数据表的创建语句

    ```sql
    show create table test;
    ```

    ​

19. 删除test数据表

    ```sql
    drop table test;
    ```

    ​

20. 删除test数据库

    ```sql
    drop database test;
    ```

    ​

21. 创建数据库pythonxx

    **注意不要忘记charset**

    ```sql
    create database python99 charset=utf8;
    ```

    ​

22. 创建小组表group，包含id，学号，姓名，性别

    ```sql
    create table group(
    	id int unsigned auto_increment primary key not null, 
    	stu_number varchar(10) default '',
      	name varchar(10) not null,
      	gender enum('男','女','人妖','保密')
    )
    ```

    ​

23. 在小组表增加生日字段birth

    ```sql
    alter table group add birth varchar(10);
    ```

    ​

24. 查看group表的结构

    ```sql
    desc group;
    ```

    ​

25. 修改生日字段为birthday，类型为datetime

    ```mysql
    alter table students change birth birthday datetime not null;
    ```

    ​

26. 查看group表的创建语句

    ```mysql
    show create table group;
    ```

    ​

27. 把自己小组的相关信息添加到数据库

    ```mysql
    --自行添加

    ```

    ​

28. 查看自己小组成员的所有信息

    ```mysql
    select * from group;
    ```

    ​

29. 修改birthday约束类型为date

    ```mysql
    alter table group modify birthday date not null;
    ```

    ​

30. 删除小组表的生日字段

    ```mysql
    alter table group drop birthday;
    ```

    ​

31. 删除group表

    ```mysql
    drop table group;
    ```

    ​

32. 删除pythonxx数据库

    ```mysql
    drop database python99;
    ```

    ​