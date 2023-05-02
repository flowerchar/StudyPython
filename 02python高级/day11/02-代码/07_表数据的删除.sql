 -- 表数据的删除

        -- 物理删除
        -- delete from 表名 where 条件
        delete from students where id=4;

        -- 逻辑删除
        -- 用一个字段来表示 这条信息是否已经不能再使用了
        -- 给students表添加一个 is_delete 字段 bit 类型
		alter table students add is_delete bit default 0;
        update students set is_delete=1 where id=1;    