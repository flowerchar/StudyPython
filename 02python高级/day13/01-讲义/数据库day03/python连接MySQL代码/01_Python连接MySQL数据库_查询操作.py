# 导入pymysql包
import pymysql


# 创建连接对象
conn = pymysql.connect(host="localhost", port=3306, user="root", password="mysql", database="python_test_1", charset="utf8")
# 获取游标对象
cs = conn.cursor()

# pymysql完成数据的查询操作
sql = "select * from students;"
# 这里获取的是sql影响的行数
# content = cs.execute(sql)
# print(content)
cs.execute(sql)
content = cs.fetchone()
print(content)
content = cs.fetchall()
print(content)

# 关闭游标和连接
cs.close()
conn.close()


