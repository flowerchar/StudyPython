 -- sql强化演练( goods 表练习)

-- 查询类型 cate_name 为 '超级本' 的商品名称 name 、价格 price ( where )
select name,price from goods where cate_name="超级本";

-- 显示商品的种类
-- 1 分组的方式( group by ) 
select cate_name from goods group by cate_name;

-- 2 去重的方法( distinct )
select distinct cate_name from goods;


-- 求所有电脑产品的平均价格 avg ,并且保留两位小数( round )
select round(avg(price),2) from goods;

-- 显示 每种类型 cate_name (由此可知需要分组)的 平均价格
select avg(price),cate_name from goods group by cate_name;


-- 查询 每种类型 的商品中 最贵 max 、最便宜 min 、平均价 avg 、数量 count
select cate_name,max(price),min(price),avg(price),count(*) from goods group by cate_name;

-- 查询所有价格大于 平均价格 的商品，并且按 价格降序 排序 order desc

-- 1 查询平局价格(avg_price)
select avg(price) as avg_price from goods;


-- 2 使用子查询
select * from goods where price>(select avg(price) as avg_price from goods) order by price desc;

-- 查询每种类型中最贵的电脑信息(难)

-- 1 查找 每种类型 中 最贵的 max_price 价格
select max(price) as max_price,cate_name from goods group by cate_name;

-- 2 关联查询 inner join 每种类型 中最贵的物品信息
-- select * from goods 
-- inner join
-- (select cate_name,max(price) as max_price from goods group by cate_name) as max_price_goods
-- on goods.cate_name=max_price_goods.cate_name and goods.price=max_price_goods.max_price;
select * from goods
inner join
(select max(price) as max_price,cate_name from goods group by cate_name) as max_price_goods
on goods.cate_name=max_price_goods.cate_name and goods.price=max_price_goods.max_price;















































 -- sql强化演练( goods 表练习)

-- 查询类型 cate_name 为 '超级本' 的商品名称 name 、价格 price ( where )
select name,price from goods where cate_name="超级本";

-- 显示商品的种类
-- 1 分组的方式( group by ) 
select cate_name from goods group by cate_name;

-- 2 去重的方法( distinct )
select distinct cate_name from goods;


-- 求所有电脑产品的平均价格 avg ,并且保留两位小数( round )
select round(avg(price),2) from goods;

-- 显示 每种类型 cate_name (由此可知需要分组)的 平均价格
select avg(price),cate_name from goods group by cate_name;


-- 查询 每种类型 的商品中 最贵 max 、最便宜 min 、平均价 avg 、数量 count
select max(price),min(price),avg(price),count(*),cate_name from goods group by cate_name;


-- 查询所有价格大于 平均价格 的商品，并且按 价格降序 排序 order desc

-- 1 查询平局价格(avg_price)
select avg(price) from goods;


-- 2 使用子查询
select * from goods where price > (select avg(price) from goods) order by price desc;

-- 查询每种类型中最贵的电脑信息(难)

-- 1 查找 每种类型 中 最贵的 max_price 价格
select max(price),cate_name from goods group by cate_name;

-- 2 关联查询 inner join 每种类型 中最贵的物品信息
-- select * from goods 
-- inner join
-- (select cate_name,max(price) as max_price from goods group by cate_name) as max_price_goods
-- on goods.cate_name=max_price_goods.cate_name and goods.price=max_price_goods.max_price;
select * from goods
inner join
(select max(price) as max_price,cate_name from goods group by cate_name) as max_price_goods
on goods.cate_name=max_price_goods.cate_name and goods.price=max_price_goods.max_price;

-- 创建"商品分类"表

第一步	创建表 (商品种类表 goods_cates )

create table if not exists goods_cates(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
);



第二步	同步 商品分类表 数据 将商品的所有 (种类信息) 写入到 (商品种类表) 中

-- 按照 分组 的方式查询 goods 表中的所有 种类(cate_name)
select cate_name from goods group by cate_name;

!!!!没有values
insert into goods_cates(name) (select cate_name from goods group by cate_name);

第三部 同步 商品表 数据 通过 goods_cates 数据表来更新 goods 表

-- 因为要通过 goods_cates表 更新 goods 表 所以要把两个表连接起来
select * from goods_cates inner join goods on goods_cates.name=goods.cate_name;     	
 
-- 把 商品表 goods 中的 cate_name 全部替换成 商品分类表中的 商品id ( update ... set )
update (goods_cates inner join goods on goods_cates.name=goods.cate_name) set goods.cate_name=goods_cates.id;

第四部 修改表结构

-- 查看表结构(注意 两个表中的 外键类型需要一致)


-- 修改表结构 alter table 字段名字不同 change,把 cate_name 改成 cate_id int unsigned not null
alter table goods change cate_name cate_id int unsigned not null;





-- 创建 商品品牌表 goods_brands

第一步 创建 "商品品牌表" 表
-- 第一种方式 先创建表
create table goods_brands (
    id int unsigned primary key auto_increment,
    name varchar(40) not null);
	
-- 插入数据 brand_name(分组)
-- 按照 分组 的方式查询 goods 表中的所有 种类(brand_name)
insert into goods_brands(name) (select brand_name from goods group by brand_name);
--(注意) 把查询出来的 结果 写入 goods_brands 表里去 ( insert into ) 只插入name



-- 第二种方式 创建表的同时插入数据(了解,不建议使用)
create table goods_brands (
    id int unsigned primary key auto_increment,
    name varchar(40) not null) select brand_name as name from goods group by brand_name;
	
		
第二步 同步数据

-- 通过goods_brands数据表来更新goods数据表 g.brand_name=b.id
update (goods inner join goods_brands on goods.brand_name=goods_brands.name) set goods.brand_name=goods_brands.id;

第三部 修改表结构
-- 通过alter table语句修改表结构 brand_id int unsigned not null
alter table goods change brand_name brand_id int unsigned not null;




-- 外键的使用(了解)

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


总结:在实际开发中,很少会使用到外键约束,会极大的降低表更新的效率







-- python与mysql的交互使用
-- 基本流程 1 connection对象 |2 cursor对象 |3 关闭cursor |4 关闭connection


	
	
-- sql注入  ' or 1=1 or '1
select * from goods where name = '%s' % name   





select * from goods where name = '' or 1 or '';









