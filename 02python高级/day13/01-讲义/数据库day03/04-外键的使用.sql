-- 外键的使用

-- 向goods表里插入任意一条数据
insert into goods (name,cate_id,brand_id,price) values('老王牌拖拉机', 10, 10,'6666');

-- 约束 数据的插入 使用 外键 foreign key
-- alter table goods add foreign key (brand_id) references goods_brands(id);
alter table goods add foreign key(cate_id) references goods_cates(id); 
alter table goods add foreign key(brand_id) references goods_brands(id);	

-- 失败原因 老王牌拖拉机 delete
-- delete from goods where name="老王牌拖拉机";
delete from goods where name="老王牌拖拉机";

-- 如何取消外键约束
-- 需要先获取外键约束名称,该名称系统会自动生成,可以通过查看表创建语句来获取名称
show create table goods;

-- 获取名称之后就可以根据名称来删除外键约束
alter table goods drop foreign key goods_ibfk_1;
alter table goods drop foreign key goods_ibfk_2;




































-- 外键的使用

-- 向goods表里插入任意一条数据
insert into goods (name,cate_id,brand_id,price) values('老王牌拖拉机', 10, 10,'6666');

-- 约束 数据的插入 使用 外键 foreign key
-- alter table goods add foreign key (brand_id) references goods_brands(id);
alter table goods add foreign key (cate_id) references goods_cates(id);
alter table goods add foreign key(brand_id) references goods_brands(id);

-- 失败原因 老王牌拖拉机 delete
-- delete from goods where name="老王牌拖拉机";
delete from goods where name="老王牌拖拉机";

-- 创建表的同时设置外键 (注意 goods_cates 和 goods_brands 两个表必须事先存在)
create table goods(
    id int primary key auto_increment not null,
    name varchar(40) default '',
    price decimal(5,2),
    cate_id int unsigned,
    brand_id int unsigned,
    is_show bit default 1,
    is_saleoff bit default 0,
    foreign key(cate_id) references goods_cates(id),
    foreign key(brand_id) references goods_brands(id)
);


-- 如何取消外键约束

-- 需要先获取外键约束名称,该名称系统会自动生成,可以通过查看表创建语句来获取名称
show create table goods;

-- 获取名称之后就可以根据名称来删除外键约束
alter table goods drop foreign key goods_ibfk_1;
alter table goods drop foreign key goods_ibfk_2;
