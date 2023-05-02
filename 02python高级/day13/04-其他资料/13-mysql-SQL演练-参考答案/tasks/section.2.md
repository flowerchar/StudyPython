# 每日练习题

1. 将每日作业根目录下的sql脚本恢复到数据库中（例如python99）

   ```sql
   mysql -uroot -p python99 < python99.sql
   ```

2. 进入你恢复到的数据库（上题中的python29）

   ```sql
   use python99
   ```

3. 将数据分页，每页显示10个，显示第一页，并同时显示其状态（status表中的detail字段）

   ```sql
   select * from dg_taobao as t inner join status as s on t.status=s.id limit 0,10;
   ```

4. 查询状态为下架的商品的分类中文名称（字段为zh）

   ```sql
   select t.zh as '类别',s.detail as '状态' from dg_taobao as t inner join status as s on t.status=s.id where s.id=0;
   ```

5. 查询“运动户外”分类的所有商品分类名以及状态（detail字段）

   ```sql
   select s.zh from dg_taobao as s inner join dg_taobao as p on s.parent_id=p.id where p.zh='运动户外';
   ```

6. 使用子查询方式查询“女装男装”分类下的中文商品分类（zh）

   ```sql
   select zh from dg_taobao where parent_id=(select id from dg_taobao where zh='女装男装');
   ```

7. 按照一级分类分组，显示每组的所有小分类

   ```sql
   select s.zh as '分类',group_concat(t.zh) as '二级分类' from (select * from dg_taobao where level=1) as s inner join dg_taobao as t on s.id=t.parent_id group by s.zh;
   ```

8. 查询“汽车摩托”分类下的小分类数目

   ```sql
   select count(*) from dg_taobao as f inner join dg_taobao as s on f.id=s.parent_id where f.zh='汽车摩托';
   ```

9. 可自己新增其他相关的数据表进行其他SQL语句练习

   略

10. 根据如下数据，设计数据库及数据表：

   包含id、name、gender、email字段

   略

11. 使用python程序完成如下功能：

    ```python
    # 1.连接上题中创建的数据库

    # 2.添加自己小组成员到上题的数据表中

    # 3.打印出小组成员中性别为男的新成员信息

    # 4.为某个成员修改信息，如修改性别信息

    # 5.删除刚刚被修改信息的成员记录
    ```

    tips:对数据进行增加、修改、删除操作，记得commit

    略