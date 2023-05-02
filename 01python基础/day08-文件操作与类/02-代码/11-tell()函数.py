# -*- coding: utf-8 -*-
# @Author  : Chinesejun
# @Email   : flower@163.com
# @File    : 11-tell()函数.py
# @Software: PyCharm
#
# f = open("test.txt", "r")
# str = f.read(3)
# print("读取的数据是 : %s" % str)
# #
# # 查找当前位置
# position = f.tell()
# print("当前文件位置 : %s" % position)
# #
# str = f.read(3)
# print("读取的数据是 : %s" % str)
# #
# # 查找当前位置
# position = f.tell()
# print("当前文件位置 : %s" % position)
# #
# f.close()

# 打开文件
f = open("runoob.txt", "a+")
print("文件名为: ", f.name)

# f.seek(0)
# print(f.tell())
# f.write('hpythonpython')
# print(f.read())

# 刷新缓冲区
# fo.flush()

# 截取10个字节, 之后全部删除
f.truncate(5)

# str = fo.readline()
# print ("读取数据: %s" % (str))

# 关闭文件
f.close()

