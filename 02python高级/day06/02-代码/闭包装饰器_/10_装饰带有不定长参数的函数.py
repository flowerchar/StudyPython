# 定义装饰器
def logging(fn):  # fn = sum_num
    def inner(*args, **kwargs):
        fn(*args, **kwargs)

    return inner  # sum_num = inner

# 使用装饰器装饰函数
@logging
def sum_num(*args, **kwargs):
    print(args, kwargs)


sum_num(1, 2, 3, age="18")