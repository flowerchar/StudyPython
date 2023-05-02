# 定义装饰器
def logging(fn):  # fn = sum_num
    def inner(a, b):
        result = fn(a, b)
        return result

    return inner  # sum_num = inner

# 使用装饰器装饰函数
@logging
def sum_num(a, b):
    result = a + b
    return result


result = sum_num(1, 2)
print(result)