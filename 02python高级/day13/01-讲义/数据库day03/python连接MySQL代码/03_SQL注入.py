# 导入pymysql包
import pymysql


# 创建连接对象
conn = pymysql.connect(host="localhost", port=3306, user="root", password="mysql", database="python_test_1", charset="utf8")
# 获取游标对象
cs = conn.cursor()

# 不安全的方式
# 根据id查询学生信息
# find_name = input("请输入您要查询的学生姓名:")
# sql = "select * from students where name='%s'" % find_name
# # 显示所有的数据
# cs.execute(sql)
# content = cs.fetchall()
# for i in content:
#     print(i)

# 安全的方式
# 根据id查询学生信息
find_name = input("请输入您要查询的学生姓名:")
sql = "select * from students where name=%s"
# 显示所有的数据
cs.execute(sql, [find_name])
content = cs.fetchall()
for i in content:
    print(i)

# 关闭游标和连接
cs.close()
conn.close()
