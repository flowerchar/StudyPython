-- 索引

-- 创建测试表
create table test_index(title varchar(10));

-- 向表中插入10万条数据
python3 insert_data.py



-- 验证索引性能


-- 没有索引
-- 开启时间检测：
set profiling=1;
-- 查找第1万条数据ha-99999
select * from test_index where title="ha-99999";
-- 查看执行时间
show profiles;


-- 有索引
-- 给title字段创建索引
alter table test_index add index(title);
-- 查找第1万条数据ha-99999
select * from test_index where title="ha-99999";
-- 查看执行时间
show profiles;
