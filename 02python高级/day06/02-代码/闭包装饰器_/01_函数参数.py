def func01():
    print("func01 is show")

# func01()
# 函数名存放的是函数所在空间的地址
# print(func01)
# 函数名也可以像普通变量一样赋值
# func02 = func01
# func02()

def foo(func):
    func()
    
foo(func01)