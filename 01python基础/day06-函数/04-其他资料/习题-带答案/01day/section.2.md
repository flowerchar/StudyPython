# 每日练习题

## 题目1

### 题干

手机上都有计算器的功能（两个数字的加减乘除）并且实现将结果输出，那么假如你是开发人员，你怎么用一个函数来实现这个功能？

例如：输入： 2+33

​	   输出：和为35

### 训练目标

1. 有返回值、有参数的函数练习
2. 字符串的分割处理
3. if的条件判断
4. 返回值的应用

### 训练提示

1. 输入的是字符串“2+33” ，那么我们是不是要对这个字符串进行处理
2. 在处理以上字符串的时候，因为可能出现“+-*/”任意一个字符，甚至是不期望的字符，那么怎么进行处理？
3. 对于字符串中的数字，是不是要将其从字符转变成数字？
4. 形式参数要怎么来设定?
5. 返回值要怎么接收？

### 参考方案

1.先判断符号，然后根据符号分割，之后将字符转换成数字，然后进行用函数计算

### 操作步骤

1. 先用in来判断四种符号在不在这个字符串里面
2. 如果符合第一步，那么就用这个符号来分割字符串
3. 将两个部分分别转换成整形
4. 将这两个整形传入函数之中，进行计算，然后接收返回值进行输出

### 参考答案

```python
def computet(a,b,c):
    if b =="+":
        return a+c
    elif b== "-":
        return a-c
    elif b=="*":
        return a*c
    elif b=="/":
        return a/c
jisuanstr = input("请输入一个表达式")
if '+'in jisuanstr:
    num = jisuanstr.split('+')
    num1 = int(num[0])
    num2 = int(num[1])
    print(computer(num1,'+',num2))
elif '-'in jisuanstr:
    num = jisuanstr.split('-')
    num1 = int(num[0])
    num2 = int(num[1])
    print(computer(num1,'-',num2))
elif '*'in jisuanstr:
    num = jisuanstr.split('*')
    num1 = int(num[0])
    num2 = int(num[1])
    print(computer(num1,'*',num2))
elif '/'in jisuanstr:
    num = jisuanstr.split('/')
    num1 = int(num[0])
    num2 = int(num[1])
    print(computer(num1,'/',num2))
elif 
	print("出现了不期望字符")
# 请运用你现在所学的东西，将代码简化一下。
# 以上代码仅供参考，有其他方法能实现也可
```

## 题目2

### 题干

有如下代码：

```python
num = 10
def anum():
    num = 20
print(num)
```

请问这段代码最终输出的值是多少？

### 训练目标

1. 分清全局变量与局部变量

### 训练提示

1. 全局变量与局部变量有什么区别

### 参考方案

对于在函数内部的变量，如果改变没有global声明的变量，那么相当于是重新定义了一个与全局变量同名的局部变量



## 题目3

### 题干

有如下代码：

```python
def abnum(big, small, middle):
    .....#此处省略一千行代码
```

现在要调用abnum函数，但是怕在调用的时候将参数的位置传错，如何避免这个情况？写一段代码示范下

### 训练目标

关键字参数的使用

### 训练提示

1. 题中已经给了现有的函数以及形参，但是要怎么才能保证实参能够一对一传入，不发生错误呢？

### 参考方案

1. 明确要用关键字参数，来指定参数位置

### 操作步骤

1. 在调用函数的时候，直接标明参数的值

### 参考答案

```python
abnum(big=5, small=1, middle=1)    
```