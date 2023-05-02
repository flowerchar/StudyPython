# 1定义一个装饰器(装饰器的本质是闭包)
def check(fn):
    def inner():
        print("请先登陆")
        fn()

    return inner


# 2使用装饰器装饰函数（增加一个登陆功能）
# 解释器遇到@check 会立即执行 comment = check(comment)
@check
def comment():
    print("发表评论")

comment()

