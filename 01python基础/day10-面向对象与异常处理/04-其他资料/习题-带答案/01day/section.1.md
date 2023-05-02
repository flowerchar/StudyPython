# 每日必会题

## 题目1

### 题干

创建一个Animal（动物）基类,其中有一个run方法

创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法

### 训练目标

- 单继承的使用

### 训练提示

- 继承的格式是什么？
- 继承可以继承那些属性和方法？
- 子类中增加方法

### 参考方案

- 子类在继承的时候，在定义类时，小括号()中为父类的名字
- 父类的属性、方法，会被继承给子类

### 操作步骤

- 定义一个Animal（动物）类，实现run方法
- 定义子类Horse(马)继承父类，实现eat方法

### 参考答案

```python
class Animal():
    def run(self):
        print("跑起来")

class Horse(Animal):
    def eat(self):
        print("吃东西")
```



## 题目2

### 题干

创建一个动物的基类,其中有一个run方法

创建一个Horse（马）类继承于动物类，Horse类中重写run方法，增加打印"迈着矫健的步伐跑起来"，同时实现eat方法

### 训练目标

- super方法的使用
- 重写父类方法

### 训练提示

- 如何重写父类方法？
- 如何在子类中调用父类的方法？
- super的作用是什么？

### 参考方案

- 继承父类
- 重写父类方法
- 使用super方法调用父类方法

### 操作步骤

- 创建父类
- 创建子类
- 重写父类方法
- 使用super方法调用父类方法

### 参考答案

```python
class Horse(Animal):
    def run(self):
        super(Cat, self).run()
        print("迈着矫健的步伐跑起来")
        
    def eat(self):
        print("吃东西")

c = Cat()
c.run()
c.eat()
```



## 题目3 

### 题干

创建一个动物的基类,其中有一个run方法

创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法

创建一个SwiftHorse（千里马）类继承与Horse类，初始化init方法name为千里马

### 训练目标

- 多层继承

### 训练提示

- 多层继承父类

### 参考方案

- SwiftHorse类都拥有那些属性和方法？

### 操作步骤

- 定义Animal类
- 定义Horse类继承Animal类
- 定义SwiftHorse类继承Cat类

### 参考答案

```python
class Animal():
    def run(self):
        print("跑起来")

class Horse(Animal):
    def eat(self):
        print("吃东西")
        
class SwiftHorse(Cat):
    def __init__(self):
        self.name = "千里马"

```



## 题目4

### 题干

创建一个动物的基类,其中有一个run方法

创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法

创建一个Donkey（驴）类继承于动物类，Donkey类中不仅有run方法还有eat方法

创建一个Mule（骡子）类继承于Horse，Donkey，初始化name为驴。定义eat方法，调用父类eat方法使用的是哪个父类的方法？

### 训练目标

- 多继承

### 训练提示

- 多继承，当使用super时调用的是哪个父类的方法？
- 使用super() 是否调用所有的父类方法？只执行多少次。调用顺序遵循什么顺序。 

### 参考方案

- 如果继承了多个父类，且父类都有同名方法，则默认只执行第一个父类的(同名方法只执行一次，目前super()不支持执行多个父类的同名方法)
- 使用super() 可以逐一调用所有的父类方法，并且只执行一次。调用顺序遵循 **mro** 类属性的顺序。 

### 操作步骤

- 定义Horse类
- 定义Donkey类
- 定义Mule类，继承Horse、Donkey。

### 参考答案

```
class Animal():
    def run(self):
        print("跑起来")

class Horse(Animal):
    def eat(self):
        print("猫吃东西")

class Donkey(Animal):
    def eat(self):
        print("狗吃东西")

class Mule(Horse, Donkey):
    def __init__(self):
        self.name = "驴"
    def eat(self):
        super(CatDog, self).eat()
```



## 题目5

### 题干

- 创建一个Car类（车类），初始化name和油耗
- 创建一个 GasolineCat（汽车）类继承于Car类，有一个run方法，打印消耗了多少升汽油
- 创建一个 ElectricityCat类（电车）继承于Car类，有一个run方法，打印“我是电车不耗油”
- 创建一个HybridCar（混动汽车）类继承GasolineCat，ElectricityCat类。

### 训练目标

- 类继承的使用

### 训练提示

- 子类可以继承父类的属性和方法

### 参考方案

- GasolineCat和ElectricityCat是单继承Car类
- hybridCar继承GasolineCat、ElectricityCat

### 操作步骤

- 定义car类，初始化属性name和loss
- 定义GasolineCat类，实现run方法
- 定义ElectricityCat类，实现run方法
- 定义HybridCar类，继承GasolineCat、ElectricityCat，实现run方法。

### 参考答案

```python
class Car():
    def __init__(self,name,loss):
        self.name = name
        self.loss = loss

class GasolineCat(Car):
    def run(self, num):
        lo = self.loss/100 * num
        print("消耗了%s升汽油"%lo)

class ElectricityCat(Car):
    def run(self):
        print('我是电车不耗油')

class HybridCar(GasolineCat,ElectricityCat):
    def run(self):
        print('我是混动车')
```







