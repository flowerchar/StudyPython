-- 什么是视图?
	-- 通俗的讲，视图就是一条SELECT语句执行后返回的结果集。
	-- 所以我们在创建视图的时候，主要的工作就落在创建这条SQL查询语句上。
	
-- 视图的特点
	-- 视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，
	-- 不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）；
	
-- 视图的最主要的作用
	-- 如果数据库因为需求等原因发生了改变，为了保证查询出来的数据与之前相同，
	-- 则需要在多个地方进行修改，维护起来非常麻烦,这个时候使用视图就可解决这个问题
	
-- 视图的定义方式
	create view 视图名称(一般使用v开头) as select语句;
	
-- 查出学生的id,姓名,年龄,性别 和 学生的 班级
	select s.id,s.name,s.age,s.gender,c.name as cls_name 
	from students as s 
	inner join classes as c 
	on s.cls_id=c.id;

-- 创建上述结果的视图( v_students )
	create view v_students as 
	select s.id,s.name,s.age,s.gender,c.name as cls_name 
	from students as s 
	inner join classes as c 
	on s.cls_id=c.id;
	
-- 解决数据库发生改变 python程序也需要改变的问题
	
	
	
	
-- 删除视图
	-- drop view ;
	drop view xxx;
-- 注意
	-- 视图只能进行搜索
	
-- 视图作用总结

-- 1 提高了重用性，就像一个函数
-- 2 对数据库重构，却不影响已经编写好的程序运行
-- 3 提高了安全性能，可以对不同的用户
-- 4 让数据更加清

-- 视图最主要解决的问题 
	-- 程序对数据库操作,一旦数据库发生变化,程序需要修改,这时如果使用视图就可以解决这个问题






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

	
	
	-- 持久性
		-- 一旦事务提交，则其所做的修改会永久保存到数据库
		
	-- 注意 
		-- innodb能使用事物
		-- 使用python操作数据库的时候 默认开启事物的 
		-- 但是python对数据库进行增删改的时候 需要手动commit
		
		-- 使用终端操作数据库(也就是mysql的客户端)的时候 也是默认开始事物的
		-- 只是在回车确认操作的时候 终端会默认的commit 所以我们不需要commit
		
		
-- 事物最主要解决的问题
	-- 某些事情需要一次性完成 中途不允许出现中断 例如银行取钱 事物可以解决这种问题
		
		
		


		
		
-- 索引
	-- 注意
	-- 要注意的是，建立太多的索引将会影响更新和插入的速度，因为它需要同样更新每个索引文件。
	-- 对于一个经常需要更新和插入的表格，就没有必要为一个很少使用的where字句单独建立索引了，
	-- 对于比较小的表，排序的开销不会很大，也没有必要建立另外的索引。

	-- 建立索引会占用磁盘空间


-- 索引最主要解决的问题
	-- 当数据非常庞大时,并且这些数据不需要经常修改,为了加快查询速度,我们会使用索引
	
	
	
	
	
	
	
	
-- 权限管理(了解) 对用户的管理

	-- 查看有哪些账户
		1 使用root账户登录
		2 使用mysql数据库
		3 用户的信息存放在 user 表中 
			-- select host,user,authentication_string from user;
				Host表示允许访问的主机
				User表示用户名
				authentication_string表示密码，为加密后的值
			select host,user,authentication_string from user;
				
	-- 创建账户、授权 
		
		-- 案例一
		1 使用root账户登录
		
		2 创建账户并授予所有权限(部分权限)
		-- grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';(语法格式)
		grant select on jing_dong.* to "laoli"@"localhost" identified by "123";
			
			-- 注意
			-- 1 访问主机通常使用 百分号% 表示此账户可以使用任何ip的主机登录访问此数据库
			-- 2 访问主机可以设置成 localhost 或具体的ip，表示只允许本机或特定主机访问
			
		-- 查看用户有哪些权限
		-- show grants for 用户@访问主机;
		show grants for laowang@localhost;
			
		3 退出root的登录 使用laowang账户登录
		-- 使用查询操作是可以的
		
		-- 使用其他操作是不可以的
			
			
		
		-- 案例二
		1 使用root账户登录
		
		2 创建账户并授予所有权限(所有权限)
			grant all privileges on jing_dong.* to "laoli"@"%" identified by "12345678"
			-- 注意 访问链接设置成 % 十分危险 不要使用
			
			
		
		
		
	-- 修改权限
		1 使用root账户登录
		
		2 修改用户权限
		-- grant 权限名称 on 数据库 to 账户@主机 with grant option;(语法格式)
		例:grant select,insert on jing_dong.* to laowang@localhost where grant option;
		
		3 刷新权限
			flush privileges;
			
	-- 修改密码
		1 使用root账户登录
		
		2 选择mysql数据库
		
		3 使用password()函数进行密码加密 对user表进行修改
		-- update user set authentication_string=password('新密码') where user='用户名';(语法格式)
		
		例:update user set authentication_string=password('123') where user='laowang';
		
		
	-- 删除用户
		1 使用root账户登录
		
		2 删除用户
			第一种方式  drop user '用户名'@'主机';(语法格式)  卸载
			
						例:drop user 'laowang'@'localhost';
						
			第二种方式	delete from user where user='用户名';(语法格式)  手动删除
			
						例:delete from user where user='laowang';
						
						-- 操作结束之后需要刷新权限
						flush privileges
						
		-- 推荐使用语法1删除用户, 如果使用语法1删除失败，采用语法2方式
	
	
	-- 远程登录(谨慎使用)
	
	
	
	
	
	
	