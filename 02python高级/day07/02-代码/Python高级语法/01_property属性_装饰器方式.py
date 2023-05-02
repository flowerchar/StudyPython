class Person(object):
    def __init__(self):
        self.__age = 0

    # 获取属性
    @property
    def age(self):
        return self.__age

    # 修改属性
    @age.setter
    def age(self, new_age):
        self.__age = new_age

# p = Person()
# age = p.age()
# print(age)

p = Person()
print(p.age)
# 修改属性
p.age = 100
print(p.age)
