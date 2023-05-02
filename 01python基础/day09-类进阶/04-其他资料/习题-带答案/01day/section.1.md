# 每日必会题

### 题目1 

### 题干

 定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

### 训练目标

- 定义类
- 创建对象

### 训练提示

- 什么是类？
- 什么是对象？
- 定义类的命名规则是什么？
- 定义类的三大要素都有哪些？

### 参考方案

- 创建类关键字 class

### 操作步骤

- 使用class关键字创建类
- 实例化对象

### 参考答案

```python
class Star():
    pass

zhou_xing_chi = Star()
```



## 题目2 

### 题干 

定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

给对象添加属性 

​	明星姓名= “周星驰”

​	 明星的电影 = “功夫”

### 训练目标

- 添加属性

### 训练提示

- 如何给对象添加属性？

### 参考方案

- 添加属性方法1

  对象名.属性名 = 值

### 参考步骤

- 定义类
- 创建对象
- 添加属性

### 参考答案

```python
class Star():
    pass

zhou_xing_chi = Star()
zhou_xing_chi.name =  '周星驰'
zhou_xing_chi.movie = "功夫"
```



## 题目3 

### 题干

定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用init方法给对象添加属性 

### 训练目标

- init的使用
- 带有参数的init

### 训练提示

- init方法的作用？
- init方法在什么时候调用？
- init的参数都代表什么？

### 参考方案

- 使用init方法给对象添加属性

### 参考步骤

- 创建对象
- 定义init方法，并且重新赋值

### 参考答案

```python
class Star():
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie
zhou_xing_chi = Star('周星驰', "功夫")
```







