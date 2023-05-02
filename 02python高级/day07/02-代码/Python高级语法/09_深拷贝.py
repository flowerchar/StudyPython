import copy

# 深拷贝可变类型
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = [a, b]
#
# d = copy.deepcopy(c)
#
# print(id(c))
# print(id(d))

# 深拷贝-深层数据
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = [a, b]
#
# d = copy.deepcopy(c)
#
# print(id(a))
# print(id(c[0]))
# print(id(d[0]))


# 深拷贝不可变类型
a = (1, 2, 3)
b = (11, 22, 33)
c = (a, b)

d = copy.deepcopy(c)

print(id(c))
print(id(d))

