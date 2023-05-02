# 每日练习题

## 题目1

### 题干

定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用init方法给对象添加属性 

定义方法playing()，打印“xxx出演了yyy，非常好看”

### 训练目标

self的使用

### 训练提示

- 如何在类中定义方法？
- 方法的参数都有哪些？
- self指的是什么？
- 如何调用方法？

### 参考方案

- 使用self保存私有属性
- 调用方法打印结果

### 参考步骤

- 创建对象
- 初始化
- 定义方法
- 创建对象
- 打印结果

### 参考答案

```python 
class Star():
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie
    def playing(self):
        print("%s出演了%s，非常好看"%(self.name,self.movie))
        
zhou_xing_chi = Star('周星驰', "功夫")
zhou_xing_chi.playing()
```



## 题目2

### 题干

定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用init方法给对象添加属性 

print输出对象时打印"xxx是我的偶像，我非常喜欢他的电影yyy"

xxx为明星姓名，yyy是电影的名字

### 训练目标

- str方法的使用

### 训练提示

- str方法的作用是什么？
- str方法的参数有哪些？
- str是否有返回值？

### 参考方案

- 使用str方法用来显示信息
- 该方法需要 return 一个数据，并且只有self一个参数，当在类的外部 print(对象) 则打印这个数据

### 参考步骤

- 定义类
- 初始化属性
- 定义str方法
- 创建对象
- 打印对象

### 参考答案

```python
class Star():
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie
        
    def __str__(self):
        return "%s是我的偶像，我非常喜欢他的电影%s"%(self.name,self.movie)
    
zhou_xing_chi = Star('周星驰', "功夫")
print(zhou_xing_chi)
```



## 题目3

### 题干

定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用init方法给对象添加属性 

删除创建的对象，打印“我不喜欢xxx了”

### 训练目标

- del方法的使用

### 训练提示

- del方法的作用是什么？
- del方法什么时候调用？

### 参考方案

- 当删除对象时，python解释器也会默认调用一个方法，这个方法为`__del__()`方法 
- 当有变量保存了一个对象的引用时，此对象的引用计数就会加1； 
- 当使用del() 删除变量指向的对象时，则会减少对象的引用计数。如果对象的引用计数不为1，那么会让这个对象的引用计数减1，当对象的引用计数为0的时候，则对象才会被真正删除（内存被回收）。 

### 参考步骤

- 创建类
- 初始化
- 定义del方法
- 创建对象
- 调用del方法

### 参考答案

```
class Star():
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie
        
    def __del__(self):
        print("我不喜欢%s了"%self.name)
        
zhou_xing_chi = Star('周星驰', "功夫")
print(zhou_xing_chi)
del(zhou_xing_chi)
```



## 题目4

### 题干

 a.定义一个Star类(明星类)，包含初始化init方法：

 成员属性：明星姓名

​		    明星的电影

成员方法：playing()

​	打印：“xxx出演了yyy，非常好看”

打印对象时显示“xxx是我的偶像，我非常喜欢他的电影yyy”

删除对象提示“xxx我不再喜欢了”

xxx为明星姓名，yyy是电影的名字

b.键盘循环输入五个Star对象的姓名和电影名。

c.分别调用输入Star对象的playing方法和打印对象

```
请输入你喜欢的明星:周星驰
请输入电影名功夫
请输入你喜欢的明星:刘德华
请输入电影名狄仁杰
请输入你喜欢的明星:周润发
请输入电影名赌神
周星驰出演了功夫，非常好看
周星驰是我的偶像，我非常喜欢他的电影功夫
刘德华出演了狄仁杰，非常好看
刘德华是我的偶像，我非常喜欢他的电影狄仁杰
周润发出演了赌神，非常好看
周润发是我的偶像，我非常喜欢他的电影赌神
我不喜欢周星驰了
我不喜欢刘德华了
我不喜欢周润发了
```



### 训练目标

- 类的基本使用

### 训练提示

- 创建类
- init初始化
- str打印对象
- del删除对象
- 使用列表保存创建的类对象

### 参考方案

- 循环保存对象到一个列表中
- 每次循环创建对象
- 遍历列表，取出每次保存的对象，调用对象方法

### 参考步骤

- 创建类
- 初始化
- 定义方法
- 重写str方法
- 重写del方法
- 创建一个空列表
- 循环创建类对象，并将对象保存到列表中
- 遍历列表，调用方法

### 参考答案

```python
class Star():
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie

    def playing(self):
        print("%s出演了%s，非常好看"%(self.name,self.movie))

    def __str__(self):
        return "%s是我的偶像，我非常喜欢他的电影%s"%(self.name,self.movie)

    def __del__(self):
        print("我不喜欢%s了"%self.name)

mov_l = []
for i in range(3):
    name = input("请输入你喜欢的明星:")
    movie = input("请输入电影名")
    s = Star(name,movie)
    mov_l.append(s)

for i in mov_l:
    i.playing()
    print(i)
```

