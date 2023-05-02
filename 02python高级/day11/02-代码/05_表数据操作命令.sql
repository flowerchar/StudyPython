--05 增删改查(curd)(重点--记忆)
    --增加
        -- 全列插入
        -- insert [into] 表名 values(...)
        -- 主键字段 可以用 0  null   default 来占位
        -- 向classes表中插入 一个班级
+--------+-------------------+------+-----+---------+----------------+
| Field  | Type              | Null | Key | Default | Extra          |
+--------+-------------------+------+-----+---------+----------------+
| id     | int(10) unsigned  | NO   | PRI | NULL    | auto_increment |
| name   | varchar(20)       | NO   |     | NULL    |                |
| age    | int(10) unsigned  | YES  |     | 0       |                |
| high   | decimal(5,2)      | YES  |     | NULL    |                |
| gender | enum('男','女')   | YES  |     | NULL    |                |
| cls_id | int(10) unsigned  | YES  |     | NULL    |                |
+--------+-------------------+------+-----+---------+----------------+

    -- 向students表插入 一个学生信息
    insert into students values(0,"小花",18,166.66,"男",110);

        
    -- 部分插入
    -- insert into 表名(列1,...) values(值1,...)
    insert into students(name,age) values("德华",50);

    -- 多行插入
	insert into students values(0,"小花1",18,166.66,"男",110),(0,"小花2",18,166.66,"男",110);



























--01 mysql 数据库的操作
    ctrl + a 快速回到行首
    ctrl + e 回到行末
    ctrl + l 清屏
    ctrl + c + 回车  结束

    -- 链接数据库
    mysql -uroot -pmysql
    
    -- 不显示密码
    mysql -uroot -p
    mysql

    -- 退出数据库
    quit/exit/ctrl + d

    -- sql语句最后需要有分号;结尾
    -- 显示数据库版本 version
    select version();

    -- 显示时间
    select now();
    
    -- 查看当前使用的数据库
    select database();

    -- 查看所有数据库
    show databases;
    
    -- 创建数据库
    -- create database 数据库名 charset=utf8;
    create database python16;
    create database python16 charset=utf8;(注意)
    

    -- 查看创建数据库的语句
    -- show create database ....
    show create database python16;
     

    -- 使用数据库
    -- use 数据库的名字
    use python16;

    -- 删除数据库
    -- drop database 数据库名;
    drop database python16;

--02 数据表的操作

    -- 查看当前数据库中所有表
    show tables;
    

    -- 创建表
    -- int unsigned 无符号整形
    -- auto_increment 表示自动增长
    -- not null 表示不能为空
    -- primary key 表示主键
    -- default 默认值
    -- create table 数据表名字 (字段 类型 约束[, 字段 类型 约束]);
    create table xxxx (
        id int unsigned primary key not null auto_increment,
        name varchar(20)
    );
    

    -- 查看表结构
    -- desc 数据表的名字;
    desc xxxx;

   
    -- 创建 classes 表(id、name)
    create table classes(
        id int unsigned primary key not null auto_increment,
        name varchar(20) 
    );
    
    
    -- 创建 students 表(id、name、age、high (decimal)、gender (enum)、cls_id)
    create table students(
        id int unsigned primary key not null auto_increment,
        name varchar(20),
        age int unsigned,
        high decimal(5,2),
        gender enum("男","女","中性","保密") default "保密",
        cls_id int
    );


    -- 查看表的创建语句
    -- show create table 表名字;
    show create table students;


    -- 修改表-添加字段 mascot (吉祥物)
    -- alter table 表名 add 列名 类型;
    alter table classes add jixiangwu varchar(20);

    -- 修改表-修改字段：不重命名版
    -- alter table 表名 modify 列名 类型及约束;
    alter table classes modify jixiangwu varchar(30);


    -- 修改表-修改字段：重命名版
    -- alter table 表名 change 原名 新名 类型及约束;
    alter table classes change jixiangwu mascot varchar(20);


    -- 修改表-删除字段
    -- alter table 表名 drop 列名;
    alter table classes drop mascot;

    -- 删除表
    -- drop table 表名;
    -- drop database 数据库;
    drop table xxxx;

    
--03 增删改查(curd)(重点--记忆)

    -- 增加
+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(20)      | YES  |     | NULL    |                |
+-------+------------------+------+-----+---------+----------------+



        -- 全列插入
        -- insert [into] 表名 values(...)
        -- 主键字段 可以用 0  null   default 来占位
        -- 向classes表中插入 一个班级
        insert into classes values(1,"python16");
+--------+-------------------------------------+------+-----+---------+----------------+
| Field  | Type                                | Null | Key | Default | Extra          |
+--------+-------------------------------------+------+-----+---------+----------------+
| id     | int(10) unsigned                    | NO   | PRI | NULL    | auto_increment |
| name   | varchar(20)                         | YES  |     | NULL    |                |
| age    | int(10) unsigned                    | YES  |     | NULL    |                |
| high   | decimal(5,2)                        | YES  |     | NULL    |                |
| gender | enum('男','女','中性','保密')       | YES  |     | 保密    |                |
| cls_id | int(11)                             | YES  |     | NULL    |                |
+--------+-------------------------------------+------+-----+---------+----------------+

        -- 向students表插入 一个学生信息
        insert into students values(1,"班主任",18,172.66,default,111);

        
        -- 部分插入
        -- insert into 表名(列1,...) values(值1,...)
        insert into students(name,high,gender) values("吴彦祖",188.88,1);

        -- 多行插入
        insert into students values(0,"老谢",28,188.88,1,111),(0,"老王",28,155.55,1,111);


    -- 修改
    -- update 表名 set 列1=值1,列2=值2... where 条件;
        -- 全部修改
        update students set high=170.00;
        
            -- 按条件修改
                update students set high=188.88 where id=2;

        
        
    -- 查询基本使用
        -- 查询所有列
        -- select * from 表名;
        select * from students;

        ---定条件查询
        select * from students where id=2;


        -- 查询指定列
        -- select 列1,列2,... from 表名;
        select name,gender from students;


        -- 可以使用as为列或表指定别名
        -- select 字段[as 别名] , 字段[as 别名] from 数据表;
        select name as "姓名",gender as "性别" from students;

        -- 字段的顺序
        select gender as "性别",name as "姓名" from students;
    

    -- 删除
        -- 物理删除
        -- delete from 表名 where 条件
        delete from students where id=2;

        -- 逻辑删除
        -- 用一个字段来表示 这条信息是否已经不能再使用了
        -- 给students表添加一个 is_delete 字段 bit 类型
        alter table students add is_delete bit default 0;
        update students set is_delete=1 where id=4;    
        
    -- 数据库备份与恢复(了解)
        -- mysqldump –uroot –p 数据库名 > python.sql;
        -- mysql -uroot –p 新数据库名 < python.sql;

