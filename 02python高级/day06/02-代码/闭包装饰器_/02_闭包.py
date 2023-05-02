# 闭包的构成条件:
# 1在函数嵌套(函数里面再定义函数)的前提下
def func_out(num1):
    def func_inner(num2):
# 2内部函数使用了外部函数的变量(还包括外部函数的参数)
        num = num1 + num2
        print("现在的值：", num)
# 3外部函数返回了内部函数
    return func_inner


# 创建闭包实例
f = func_out(10)
# 执行闭包
f(1)
f(2)

 