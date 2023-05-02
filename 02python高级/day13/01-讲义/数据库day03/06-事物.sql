-- 事物(ACID)
	
	-- 原子性 一致性
		第一步 打开 终端1 终端2
		第二步 终端1 打开事物 begin
			   终端1 update 表名 set 字段="xxx" where ...;
			   终端1 select * from 表名;  发现数据改变
		第三步 终端2 select * from 表名;  
			   发现数据其实并没有改变 其实这个时候对数据的相关操作信息存在缓存中,
			   当commit之后,这些操作才会一次性的完成
		第四步 终端1 commit 数据数数据真的改变
			   终端2 select * from 表名,数据改变了
			
	-- 隔离性
		第一步 打开 终端1 终端2
		第二步 终端1 打开事物 begin
			   终端1 update 表名 set 字段="xxx" where ...;
		第三步 终端2 update 表名 set 字段="yyy" where ...;
			   发现 处于阻塞状态 
		第四步 终端1 commit
			   终端2 阻塞状态解除 数据修改成 yyy
			   
	-- 回滚(rollback)
		第一步 打开 终端1 begin
		第二步 终端1 update 表名 set 字段="xxx" where ...;
		第三步 rollback 数据返回最开始的原始值

		
	-- 注意 
		-- innodb能使用事物
		
