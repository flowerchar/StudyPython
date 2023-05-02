-- 视图的作用
	
-- 视图的定义方式
	create view 视图名称(一般使用v开头) as select语句;
	
-- 查出学生的id,姓名,年龄,性别 和 学生的 班级
	select s.id,s.name,s.age,s.gender,c.name as cls_name 
	from students as s 
	inner join classes as c 
	on s.cls_id=c.id;

-- 创建上述结果的视图( v_students )
-- create view v_students as 
create view v_students as 
select s.id,s.name,s.age,s.gender,c.name as cls_name 
	from students as s 
	inner join classes as c 
	on s.cls_id=c.id;

-- 删除视图（drop view 视图名字）
drop view