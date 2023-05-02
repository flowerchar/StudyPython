# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fb(num):
    a = 0
    b = 1

    # 记录生成了几个数字
    index = 0

    while index < num:
        result = a
        #1  1      1   1
        #1  2      1   2
        #2  3      2   3
        a, b = b, a+b
        yield result
        index += 1

f = fb(5)
# print(next(f))
# print(next(f))
for i in f:
    print(i)
