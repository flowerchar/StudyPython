# 导入pymysql包
import pymysql


# 创建连接对象
conn = pymysql.connect(host="localhost", port=3306, user="root", password="mysql", database="python_test_1", charset="utf8")
# 获取游标对象
cs = conn.cursor()

# 增加数据
# sql = "insert into students(name) values('老王')"
# cs.execute(sql)
# 删除数据
# sql = "delete from students where id=18"
# cs.execute(sql)
# 修改数据
sql = "update students set name='老王' where id=1;"
cs.execute(sql)

# pymysql完成数据的查询操作
sql = "select * from students;"
# for循环显示数据
cs.execute(sql)
content = cs.fetchall()
for i in content:
    print(i)

# 提交操作
conn.commit()

# 关闭游标和连接
cs.close()
conn.close()


