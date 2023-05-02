import re


# # 1需求：在列表中["apple", "banana", "orange", "pear"]，匹配apple和pear
#
# fruit = ["apple", "banana", "orange", "pear"]
#
# # 获取字符串数据
# # |	匹配左右任意一个表达式
# for value in fruit:
#     result = re.match("apple|pear", value)
#     # 判断匹配是否成功
#     if result:
#         info = result.group()
#         print("我想吃的水果:",value)
#     else:
#         print("这个不是我想吃的水果")


# 2需求：匹配出163、126、qq等邮箱
# |	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \ 转义字符
# result = re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq)\.com", "hello@qq.com")
# info = result.group()
#
# print(info)


# 3需求：匹配qq:10567这样的数据，提取出来qq文字和qq号码
# group(0)代表的是匹配的所有数据 1:第一个分组的数据 2:第二个分组的数据 顺序是从左到右依次排序的
# result = re.match("(qq):([1-9]\d{4,11})", "qq:10567")
# if result:
#     info = result.group(0)
#     print(info)
#
#     num = result.group(2)
#     print(num)
#
#     type = result.group(1)
#     print(type)
# else:
#     print("匹配失败")
#

# 4需求：匹配出<html>hh</html>
# \num	引用分组num匹配到的字符串
# result = re.match("<([a-zA-Z1-6]{4})>.*</\\1>", "<html>hh</html>")
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("匹配失败")


# 5需求：匹配出<html><h1>www.flower.cn</h1></html>
# result = re.match("<([a-zA-Z1-6]{4})><([a-zA-Z1-6]{2})>.*</\\2></\\1>", "<html><h1>www.flower.cn</h1></html>")
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("匹配失败")


# 6需求：匹配出<html><h1>www.flower.cn</h1></html>
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串
result = re.match("<(?P<html>[a-zA-Z1-6]{4})><(?P<h1>[a-zA-Z1-6]{2})>.*</(?P=h1)></(?P=html)>", "<html><h1>www.flower.cn</h1></html>")
if result:
    info = result.group()
    print(info)
else:
    print("匹配失败")

