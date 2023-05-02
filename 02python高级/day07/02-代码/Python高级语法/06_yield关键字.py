def generater(num):
    for i in range(num):
        print("开始")
        yield i
        print("生成完成")

g = generater(5)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
for i in g:
    print(i)
