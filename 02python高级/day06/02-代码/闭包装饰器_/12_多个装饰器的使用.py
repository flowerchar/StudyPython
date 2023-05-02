# 定义装饰器1
def check1(fn1):
    def inner1():
        print("登陆验证1")
        fn1()

    return inner1


# 定义装饰器2
def check2(fn2):
    def inner2():
        print("登陆验证2")
        fn2()

    return inner2

# 被装饰器的函数

@check1
@check2
def comment():
    print("发表评论")


comment()


