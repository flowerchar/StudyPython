# 1定义一个装饰器(装饰器的本质是闭包)
def check(fn):
    def inner():
        print("登陆验证。。。")
        fn()

    return inner

# 需要被装饰的函数
def comment():
    print("发表评论")

# 2使用装饰器装饰函数（增加一个登陆功能）
comment = check(comment)
comment()



