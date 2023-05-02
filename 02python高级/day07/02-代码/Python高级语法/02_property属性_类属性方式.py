class Person(object):
    def __init__(self):
        self.__age = 0

    def get_age(self):
        """当获取age属性时会使用该方法"""
        return self.__age

    def set_age(self, new_age):
        """当设置属性时会使用该方法"""
        if new_age >= 150:
            print("年龄错误")
        else:
            self.__age = new_age

    age = property(get_age, set_age)

p = Person()
print(p.age)
# 设置属性
p.age = 100
print(p.age)