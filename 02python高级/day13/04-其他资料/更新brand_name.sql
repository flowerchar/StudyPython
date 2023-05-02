第一步	创建表 (商品种类表 goods_brand )

create table if not exists goods_brand(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
);


第二步	同步 商品分类表 数据 将商品的所有 (种类信息) 写入到 (商品种类表) 中

-- 按照 分组 的方式查询 goods 表中的所有 种类(brand_name)
select brand_name from goods group by brand_name;

insert into goods_brand(name) (select brand_name from goods group by brand_name);

第三部 同步 商品表 数据 通过 goods_brand 数据表来更新 goods 表

-- 因为要通过 goods_cates表 更新 goods 表 所以要把两个表连接起来
select * from goods inner join goods_brand on goods.brand_name=goods_brand.name;	
 
-- 把 商品表 goods 中的 brand_name 全部替换成 商品分类表中的 商品id ( update ... set )
update (goods inner join goods_brand on goods.brand_name=goods_brand.name) set goods.brand_name=goods_brand.id;

第四部 修改表结构

-- 查看表结构(注意 两个表中的 外键类型需要一致)
desc goods;

-- 修改表结构 alter table 字段名字不同 change,把 brand_name 改成 brand_id int unsigned not null
alter table goods change brand_name brand_id int unsigned not null;