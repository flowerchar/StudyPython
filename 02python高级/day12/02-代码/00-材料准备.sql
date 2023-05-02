--01-数据库进阶操作-材料准备

-- 创建数据库
create database python_test_1 charset=utf8;

-- 使用数据库
use python_test_1;

-- students表
create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit default 0
);

-- classes表
create table classes (
    id int unsigned auto_increment primary key not null,
    name varchar(30) not null
);


-- 向students表中插入数据
insert into students values
(0,'小明',18,180.00,2,1,0),
(0,'小月月',18,180.00,2,2,1),
(0,'彭于晏',29,185.00,1,1,0),
(0,'刘德华',59,175.00,1,2,1),
(0,'黄蓉',38,160.00,2,1,0),
(0,'凤姐',28,150.00,4,2,1),
(0,'王祖贤',18,172.00,2,1,1),
(0,'周杰伦',36,NULL,1,1,0),
(0,'程坤',27,181.00,1,2,0),
(0,'刘亦菲',25,166.00,2,2,0),
(0,'金星',33,162.00,3,3,1),
(0,'静香',12,180.00,2,4,0),
(0,'郭靖',12,170.00,1,4,0),
(0,'周杰',34,176.00,2,5,0),
(0,'凌小小',28,180.00,2,1,0),
(0,'司马二狗',28,120.00,1,1,0);

-- 向classes表中插入数据
insert into classes values (0, "python_01期"), (0, "python_02期"),(8,'Python_03期');



--查询练习

	-- 使用 as 给字段起别名
	-- select 字段 as 名字.... from 表名;
	select name from students;
	select name as "姓名" from students;

	-- select 表名.字段 .... from 表名;
	select students.name from students;

	-- 可以通过 as 给表起别名
	-- select 别名.字段 .... from 表名 as 别名;
	select s.name from students as s;

	-- 消除重复行(查性别)
	-- distinct 字段 
	select gender from students;
	select distinct gender from students;















-- 知识要点

as 可以为字段起别名
as 可以为表起别名（用来区分有相同字段的不同表）

select distinct 可以去重查询