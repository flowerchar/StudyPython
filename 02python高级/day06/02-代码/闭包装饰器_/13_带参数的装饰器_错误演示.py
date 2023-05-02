# 装饰器
# 外部函数
def decorator(fn, flag):
    # 内部函数
    def inner(num1, num2):
        # 判断流程
        if flag == "+":
            print("--正在努力加法计算--")
        elif flag == "-":
            print("--正在努力减法计算--")
        result = fn(num1, num2)
        return result

    return inner


# 被带有参数的装饰器装饰的函数
@decorator('+')
def add(a, b):
    result = a + b
    return result


# 执行函数
result = add(1, 3)
print(result)