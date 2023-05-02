 -- 06表数据的修改查询命令

    -- update 表名 set 列1=值1,列2=值2... where 条件;
        -- 全部修改
        update students set gender="女";
		
		-- 按条件修改
		update students set gender="男" where id=2;

		
		
    -- 查询基本使用
        -- 查询所有列
        -- select * from 表名;
        select * from students;

        ---定条件查询
        select * from students where id=2;


        -- 查询指定列
        -- select 列1,列2,... from 表名;
        select name,age from students;


        -- 可以使用as为列或表指定别名
        -- select 字段[as 别名] , 字段[as 别名] from 数据表;
        select name as "名字",age as "年龄" from students;

        -- 字段的顺序
        select age as "年龄",name as "名字" from students;