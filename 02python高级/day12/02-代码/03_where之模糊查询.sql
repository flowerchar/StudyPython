-- 模糊查询(where name like 要查询的数据)

		-- like 
		-- % 替换任意个
		-- _ 替换1个

		-- 查询姓名中 以 "小" 开始的名字
		select * from students where name like "小%";
		

		-- 查询姓名中 有 "小" 所有的名字
	    select * from students where name like "%小%";
		

		-- 查询有2个字的名字
		select * from students where name like "__";
		

		-- 查询至少有2个字的名字
		select * from students where name like "__%";






















--知识要点

like 
		 % 替换任意个
		 _ 替换1个









