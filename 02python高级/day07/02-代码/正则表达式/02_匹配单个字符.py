import re


# .	    匹配任意1个字符（除了\n）
# 匹配数据
# result = re.match("flower.", "flower\n")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# [ ]	匹配[ ]中列举的字符
# 匹配数据
# result = re.match("flower[123abc]", "flower-")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# \d	匹配数字,即0-9 => [0123456789] => [0-9]
# 匹配数据
# result = re.match("flower\d", "flower5")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# \D	匹配非数字,即不是数字
# 匹配数据
# result = re.match("flower\D", "flower-")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# \s	匹配空白,即空格,tab键
# 匹配数据
# result = re.match("flower\s111", "flower\t111")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# \S	匹配非空白
# 匹配数据
# result = re.match("flower\S", "flower\t")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")
#

# \w	匹配非特殊字符，即a-z, A-Z, 0-9, _, 汉字
# 匹配数据
# result = re.match("flower\w", "flower!")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# \W	匹配特殊字符,即非字母, 非数字, 非_, 非汉字
# 匹配数据
result = re.match("flower\W", "flower0")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
