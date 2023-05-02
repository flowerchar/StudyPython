# 定义一个类,实现__call__方法
class Check(object):
    def __call__(self, *args, **kwargs):
        print("我是call方法")

c = Check()
c()