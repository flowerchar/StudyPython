# 定义装饰器
def logging(fn):  # fn = sum_num
    def inner(a, b):
        fn(a, b)

    return inner  # sum_num = inner

# 使用装饰器装饰函数
@logging
def sum_num(a, b):
    result = a + b
    print(result)


sum_num(1, 2)