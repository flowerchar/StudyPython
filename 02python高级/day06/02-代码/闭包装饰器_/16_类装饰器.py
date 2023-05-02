# 定义类装饰器
class Check(object):
    def __init__(self, fn):  # fn = comment
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        print("登陆")
        self.__fn()  # comment()


# 被装饰的函数
@Check  # comment = Check(comment)
def comment():
    print("发表评论")


comment()