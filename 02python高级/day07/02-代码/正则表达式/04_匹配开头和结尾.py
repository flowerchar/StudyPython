import re






# ^	          匹配字符串开头
# 匹配数据
# result = re.match("^\dflower", "22flower")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# 以数字为开头的字符串
# result = re.match("^\d.*", "2flower")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# $	          匹配字符串结尾
# result = re.match(".*\d$", "flower")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# 匹配以数字为开头以数字为结尾
# result = re.match("^\d.*\d$", "11flower22")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")
#


# [^指定字符]  匹配除了指定字符以外的所有字符
result = re.match("^\d.*[^4]$", "11flower@")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
