-- 02-where之逻辑运算符

		-- and
		-- 18和28之间的所以学生信息
		select * from students where age>18 and age<28;
		
		失败：
		select * from students where 18<age<28;

		-- 18岁以上的女性
		select * from students where age>18 and gender="女";


		-- or
		-- 18以上或者身高高过180(包含)以上
		select * from students where age>18 or height>=180;


		-- not
		-- 不在 18岁以上的女性 这个范围内的信息
		select * from students where not (age>18 and gender="女");




















-- 知识要点

1 and  表示有多个条件时， 多个条件必须同时成立（值为True）
	
	注意：select * from students where 18<age<28;是错误的
	     select * from students where age>18 and age<28;


2 or   表示有多个条件时，满足任意一个条件时成立


3 not  表示取反操作

  注意：使用 “（）” 运算符优先级问题







		