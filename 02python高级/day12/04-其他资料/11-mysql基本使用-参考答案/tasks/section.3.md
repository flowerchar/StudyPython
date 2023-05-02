# 企业笔试题

1. SQL 的 select 语句完整的执行顺序

   1、from 子句组装来自不同数据源的数据；
   2、where 子句基于指定的条件对记录行进行筛选；
   3、group by 子句将数据划分为多个分组；
   4、使用聚集函数进行计算；
   5、使用 having 子句筛选分组；
   6、计算所有的表达式；
   7、select 的字段；
   8、使用 order by 对结果集进行排序。
   SQL 语言不同于其他编程语言的最明显特征是处理代码的顺序。在大多数据库语言中，代码按
   编码顺序被处理。但在 SQL 语句中，第一个被处理的子句式 FROM，而不是第一出现的 SELECT。
   SQL 查询处理的步骤序号：

   ```sql
   (1) FROM <left_table>
   (2) <join_type> JOIN <right_table>
   (3) ON <join_condition>
   (4) WHERE <where_condition>
   (5) GROUP BY <group_by_list>
   (6) WITH {CUBE | ROLLUP}
   (7) HAVING <having_condition>
   (8) SELECT
   (9) DISTINCT
   (9) ORDER BY <order_by_list>
   (10) <TOP_specification> <select_list>
   ```

   以上每个步骤都会产生一个虚拟表，该虚拟表被用作下一个步骤的输入。这些虚拟表对调用
   者(客户端应用程序或者外部查询)不可用。只有最后一步生成的表才会会给调用者。如果没有在
   查询中指定某一个子句，将跳过相应的步骤。
   逻辑查询处理阶段简介：
   1、 FROM：对 FROM 子句中的前两个表执行笛卡尔积(交叉联接)，生成虚拟表 VT1。
   2、 ON：对 VT1 应用 ON 筛选器，只有那些使为真才被插入到 TV2。
   3、 OUTER (JOIN):如果指定了 OUTER JOIN(相对于 CROSS JOIN 或 INNER JOIN)，保
   留表中未找到匹配的行将作为外部行添加到 VT2，生成 TV3。如果 FROM 子句包含两个以上的
   表，则对上一个联接生成的结果表和下一个表重复执行步骤 1 到步骤 3，直到处理完所有的表
   位置。
   4、 WHERE：对 TV3 应用 WHERE 筛选器，只有使为 true 的行才插入 TV4。
   5、 GROUP BY：按 GROUP BY 子句中的列列表对 TV4 中的行进行分组，生成 TV5。
   6、 CUTE|ROLLUP：把超组插入 VT5，生成 VT6。
   7、 HAVING：对 VT6 应用 HAVING 筛选器，只有使为 true 的组插入到 VT7。
   8、 SELECT：处理 SELECT 列表，产生 VT8。
   9、 DISTINCT：将重复的行从 VT8 中删除，产品 VT9。
   10、 ORDER BY：将VT9中的行按ORDER BY子句中的列列表顺序，生成一个游标(VC10)。
   11、 TOP：从 VC10 的开始处选择指定数量或比例的行，生成表 TV11，并返回给调用者。
   where 子句中的条件书写顺序

2. NoSQL 和关系数据库的区别？

   a. SQL 数据存在特定结构的表中；而 NoSQL 则更加灵活和可扩展，存储方式可以省是 JSON 文档、
   哈希表或者其他方式。
   b. 在 SQL 中，必须定义好表和字段结构后才能添加数据，例如定义表的主键(primary key)，索引
   (index),触发器(trigger),存储过程(stored procedure)等。表结构可以在被定义之后更新，但是如果有
   比较大的结构变更的话就会变得比较复杂。在 NoSQL 中，数据可以在任何时候任何地方添加，不需要
   先定义表。
   c. SQL 中如果需要增加外部关联数据的话，规范化做法是在原表中增加一个外键，关联外部数据表。
   而在 NoSQL 中除了这种规范化的外部数据表做法以外，我们还能用如下的非规范化方式把外部数据直
   接放到原数据集中，以提高查询效率。缺点也比较明显，更新审核人数据的时候将会比较麻烦。
   d. SQL 中可以使用 JOIN 表链接方式将多个关系数据表中的数据用一条简单的查询语句查询出来。
   NoSQL 暂未提供类似 JOIN 的查询方式对多个数据集中的数据做查询。所以大部分 NoSQL 使用非规范
   化的数据存储方式存储数据。
   e. SQL 中不允许删除已经被使用的外部数据，而 NoSQL 中则没有这种强耦合的概念，可以随时删
   除任何数据。
   f. SQL 中如果多张表数据需要同批次被更新，即如果其中一张表更新失败的话其他表也不能更新成
   功。这种场景可以通过事务来控制，可以在所有命令完成后再统一提交事务。而 NoSQL 中没有事务这
   个概念，每一个数据集的操作都是原子级的。
   g. 在相同水平的系统设计的前提下，因为 NoSQL 中省略了 JOIN 查询的消耗，故理论上性能上是
   优于 SQL 的。

3. Mysql 数据库的操作?

   修改表-修改字段，重命名版：
   alter table 表名 change 原名 新名 类型及约束；
   alter table students change birthday birth datetime not null;
   修改表-修改字段，不重名版本：
   alter table 表名 modify 列名 类型和约束；
   alter table students modify birth date not null
   全列插入：insert into 表名 values(...)
   insert into students values(0,"郭靖", 1,"内蒙","2017-6");
   部分插入：值的顺序与给出的列顺序对应：
   insert into students(name, birthday) values("黄蓉","2017-8");
   修改：update 表名 set 列 1=值 1，列 2=值 2.。。where
   update students set gender=0, homwtown="古墓"， where id = 5;
   备份：mysqldump -uroot -p 数据库名 》 python.sql, 恢复：mysql -uroot -p 数据库名 < python.sql

4. Mysql 日志

   错误日志：记录启动，运行或者停止 mysql 时出现的问题；
   通用日志：记录建立的客户端连接和执行的语句；
   二进制日志：记录所有更改数据的语句；

   慢查询日志：记录所有执行时间超过 long_query_time 秒的查询或者不适用索引的查询）
   通过使用--slow_query_log[={0|1}]选项来启用慢查询日志，所有执行时间超多 long_query_time 的语
   句都会被记录。