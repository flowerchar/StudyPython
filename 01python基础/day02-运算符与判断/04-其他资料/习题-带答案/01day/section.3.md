# 企业面试题

## 1. a=1,b=2,不用中间变量交换a和b的值？
```python
方法一：

1. a = a+b

2. b = a-b

3. a = a-b

方法二：

1. a = a^b

2. b =b^a

3. a = a^b

方法三：

1. a,b = b,a
```

##2. 简述你对input()函数的理解?

​		在Python3中，input()获取用户输入，不论用户输入的是什么，获取到的都是字符串类型的。

​		在Python2中有 raw_input()和input(), raw_input()和Python3中的input()作用是一样的，input()输入的是什么数据类型的，获取到的就是什么数据类型的。

