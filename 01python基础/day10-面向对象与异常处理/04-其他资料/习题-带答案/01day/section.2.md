# 每日练习题

## 题目1 

### 题干

定义一个Animal类(动物类)，拥有

​	公有类属性name"动物大家族"

​	私有类属性leg"四条腿"

创建对象分别打印name

类方法run，打印“使用yyy再跑” yyy表示腿

### 训练目标

- 公有类属性
- 私有类属性

### 训练提示

- 什么是公有属性？
- 什么是私有属性？
- 类对象是否可以直接调用私有属性？

### 参考方案

- 类属性的定义
- 私有属性方法是两个下划线加属性名

### 操作步骤

- 创建类
- 定义公有类属性name
- 定义私有类属性__leg

### 参考答案

```python
class Animal():
    name = "动物大家族"
    __leg = "四条腿"

a = Animal()
print(a.name)
print(Animal.name)
```

## 题目2 

### 题干

定义一个Animal类(动物类)，拥有

​	公有类属性name"动物大家族"

​	私有类属性leg"四条腿"

定义类Cat()，继承自Animal。

初始化名字为波斯猫

​	定义方法play，打印“xxx在玩耍” xxx表示名字

​	增加静态方法run，打印“动物们跑起来了”

​	增加类方法eat，打印“xxx在吃饭”

打印cat对象的name

### 训练目标

- 静态方法的使用
- 类方法的使用
- 当类属性和实例属性重名时，打印是哪一个？

### 训练提示

- 子类继承父类时是否继承私有属性？
- 当实例的属性名和类属性名相同时，实例对象调用时使用的是哪一个？
- 如何创静态方法？
- 如何创建类方法？

### 参考方案

- 创建静态方法时，使用装饰器staticmethod
- 创建类方法时，使用装饰器classmethod

### 操作步骤

- 定义Animal
- 定义子类Cat
- 初始化名字
- 定义play方法
- 定义静态方法run
- 定义类方法eat

### 参考答案

```python
class Animal():
    name = "动物大家族"
    __leg = "四条腿"

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def play(self):
        print("%s在玩耍"%self.name)

    @classmethod
    def eat(cls):
        print("%s在吃饭"%cls.name)

    @staticmethod
    def run():
        print("动物们跑起来了")

c = Cat("波斯猫")
c.play()
c.eat()
print(c.name)
```

## 题目3 

### 题干

用捕获异常的方式，获取用户的一个整数类型并转换为int类型，如果输入错误提示重新输入

### 训练目标

- 异常捕获

### 训练提示

- 什么是异常捕获
- 异常捕获的作用是什么
- 异常捕获的基本格式是什么

### 参考方案

- 使用try...except来捕获异常
- except什么时候运行
- else什么时候运行

### 操作步骤

- 使用while循环
- try捕获异常
- except打印出异常信息
- else当程序正常没有异常时执行

### 参考答案

```python
while True:
    try:
        num = int(input("请输入一个数字："))
        print(num)
    except:
        print("请输入正确的数字")
    else:
        break
```

## 题目4 

### 题干

创建一个动物的基类,其中有一个run方法

创建一个Cat类继承于动物类，具有私有属性__name = "波斯猫"

创建一个Dog类继承于动物类,具有私有属性__name = "京巴狗"

Cat类中不仅有run方法还有eat方法

Dog类中方法同上

创建一个letRun函数，可以接收动物及其子类对象，并调用run方法 class Cat(Animal):

编写测试代码以验证功能正常

### 训练目标

- 多态的使用
- 私有属性的使用

### 训练提示

- 多态的使用地点
- 函数接收的参数可以为一个对象

### 参考方案

- 定义一个函数，接收一个类的对象
- 创建出的对象传入到方法中
- 在方法中调用对应的方法

### 操作步骤

- 创建一个动物的基类,其中有一个run方法
- 创建一个Cat类继承于动物类
- 创建一个Dog类继承于动物类
- cat和dog中创建属性和方法
- 创建一个letRun函数，可以接收动物及其子类对象，并调用run方法 class Cat(Animal)
- 创建不同的对象，分别传入到letRun函数中，测试结果

### 参考答案

```python
# 1.创建一个动物的基类,其中有一个run方法
class Animal(object):
    def run(self):
        print('跑起来')
        
# 2.创建一个Cat类继承于动物类
class Cat(Animal):
    # 4.Cat类中不仅有run方法还有eat方法
    def __init__(self):
        self.__name = "波斯猫"

    def run(self):
        print('%s在跑'%self.__name)

    def eat(self):
        print('%s在吃'%self.__name)

# 3.创建一个Dog类继承于动物类
class Dog(Animal):
	#5.方法同上
    def __init__(self):
        self.__name = "京巴狗"

    def run(self):
        print('%s在跑'%self.__name)

    def eat(self):
        print('%s在吃'%self.__name)

# 6.创建一个letRun函数，可以接收动物及其子类对象，并调用run方法 class Cat(Animal):
def letRun(animal):
    animal.run()
    
# 7.编写测试代码以验证功能正常
# 动物测试
animal = Animal()
letRun(animal)

# 猫测试
cat = Cat()
letRun(cat)
cat.eat()

# 狗测试
dog = Dog()
letRun(dog)
dog.eat()
```

## 题目5 

### 题干

以下说法是否正确

a.一个子类是可以继承多个父类

b.类中的方法可以有return，也可以没有return

c.类方法和静态方法是一样的

d.删除对象时，默认调用__ init __方法

e.python3中object是所有类的父类

f.python中不支持多继承

g.父类中的所有方法和属性都会被继承

h.一个对象可以当做一个参数来传递

i.如果类属性和实例属性名字相同，那么实例对象调用时候使用的是实例属性

j.实例对象不可以访问类属性

k.类的私有属性，能够通过实例对象来访问

l.重写后，父类方法默认调用重写后的方法

m.子类重写父类方法时，方法名和参数都不变，只有实现方式不一样

n.类方法不可以通过实例对象来调用，只能通过类对象调用

o.一个类只能创建一个对象

### 训练目标

- 对类中的定义描述的理解

### 训练提示

### 参考方案

### 操作步骤

### 参考答案

```
a.一个子类是可以继承多个父类           正确

b.类中的方法可以有return，也可以没有return   正确

c.类方法和静态方法是一样的      不正确

d.删除对象时，默认调用__ init __方法  不正确 调用的是del魔法方法

e.python3中object是所有类的父类     正确 在python3中全都是新式类

f.python中不支持多继承				不正确 python支持多继承
	
g.父类中的所有方法和属性都会被继承		不正确 私有方法和属性不被继承

h.一个对象可以当做一个参数来传递		正确

i.如果类属性和实例属性名字相同，那么实例对象调用时候使用的是类属性  不正确 实例对象调用的是实例属性

j.实例对象不可以访问类属性  		不正确 可以访问类属性

k.类的私有属性，能够通过实例对象来访问	不正确 私有属性不被访问

l.重写方法后，父类方法默认调用重写后的方法 	不正确 父类调用的是自己的方法，子类是调用重写后的方法	

m.子类重写父类方法时，方法名和参数都不变，只有实现方式不一样	不正确  参数时可以改变的 只有方法名不变

n.类方法不可以通过实例对象来调用，只能通过类对象调用		不正确 类方法可以通过实例对象调用

o.一个类只能创建一个对象		不正确 一个类可以创建多个对象

```

