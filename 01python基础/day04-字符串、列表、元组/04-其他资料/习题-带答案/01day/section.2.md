# 每日练习题

## 题目1

### 题干

james有一个关于爬虫的项目，他需要在一个字符串中查找python这个关键字，
当前他通过index()函数进行查找，虽然可以实现查找的需求，但是总会在
没有查找到关键字的时候报错，为什么会报错，如何优化？

### 训练目标

1. 理解find函数和index函数的区别

### 训练提示

1. find函数如果查找到则返回索引值，如果查不到，则返回-1
2. index函数如果查找到则返回索引值，如果查不到，则报错

### 参考方案

1. 通过使用find函数的方式替换掉index

### 操作步骤

1. 通过使用find函数的方式替换掉index

### 参考答案

```python
只需要使用find函数替换掉index函数即可，在功能上, find函数index函数完全一致,不同的是index函数在没有查找到关键字的情况下会报ValueError的异常,因此在一般开发环境下通常都会使用find函数
```



## 题目2

### 题干

1，判断单词great是否在这个字符串中，如果在，则将每一个great后面加一个s， 如果不在则输出 great不在该字符串中
2，将整个字符串的每一个单词都变成小写，并使每一个单词的首字母变成大写
3，去除首尾的空白，并输出处理过后的字符串

### 训练目标

1. 字符串的相关操作

### 训练提示

1. 字符串的相关操作来解决上述问题
2. 使用判断语句来判断语句成立的条件

### 参考方案

1. 使用in判断某一个子字符串是否在母字符串中
2. 使用replace函数替换子字符串
3. 使用lower函数将字符串变为小写
4. 使用title函数将单词的首字母大写
5. 使用strip函数去除字符串首尾的空白

### 操作步骤

1. 使用in判断某一个子字符串是否在母字符串中
2. 使用replace函数替换子字符串
3. 使用lower函数将字符串变为小写
4. 使用title函数将单词的首字母大写
5. 使用strip函数去除字符串首尾的空白

### 参考答案

``` python
words = " great craTes Create great craters, But great craters Create great craters "

# 判断单词great是否在这个字符串中
if 'great' in words:
	# 将每一个great替换成greats
    words = words.replace("great", "greats")

    # 将单词变成小写
    words = words.lower()

    # 将每一个单词的首字母都大写
    words = words.title()

    # 去除首尾的空白
    words = words.strip()

    # 最后进行输出
    print(words)

else:
    print("great不在该字符串中")
```

## 题目3 

### 题干

将下列两个列表合并，将合并后的列表去重，之后降序并输出

list1 = [11, 45, 34, 51, 90]
list2 = [4, 16, 23, 0]

### 训练目标

列表操作方法的使用

### 训练提示

1， 列表直接可以直接拼接，元素会合并到同一个列表中
2， 可以使用sort对列表进行排序

### 参考方案

1，使用 +  对列表进行拼接
2，使用set方法将列表转变成集合，以便于去重，
3，使用sort函数，参数reverse=True对列表进行倒序排序

### 操作步骤

1，使用 +  对列表进行拼接
2，使用set方法将列表转变成集合，以便于去重，
3，使用sort函数，参数reverse=True对列表进行倒序排序

### 参考答案

``` python
list1 = [11, 45, 34, 51, 90]
list2 = [4, 16, 23, 0]

# 列表拼接
list3 = list1 + list2

# 列表去重
list4 = set(list3)
list5 = list(list4)

# 列表降序输出
list5.sort(reverse=True)

print(list5)
```

## 题目4 

### 题干

现有列表：
namelist =["tom","kaisa","alisi",["xiaoming","songshu"]]
现在有个要求，将最外层的列表转换成元组存储，里面的小列表不变；
并且向小列表中添加一个元素“python”

### 训练目标

1. 元组的强制转换
2. 元组虽然是不可变类型，但是元组中的列表是可变的

### 训练提示

1. 元组可以直接完成强制转换
2. 什么是不可变类型？
3. 元组作为不可变类型，那么元组中的元素如果是可变类型，那么可以在那个可变类型中添加吗?

### 参考方案

1. 用tuple（）这个方法
2. 在元组的可变元组中，进行添加元素操作，如果报错那么就可以证明：如果不可变类型中的的元素是可变类型，那么可变类型以是可以完成增加元素的

### 操作步骤

1. tuple(namelist)即可直接完成元组对列表的强制转换
2. 对可变类型的某一元素进行直接增加，看是否会报错

### 参考答案

```python
namelist =["tom","kaisa","alisi",["xiaoming","songshu"]]
nametuple = tuplenamelist)
print(nametuple)

#y 以下是往可变元素中添加元素
nametuple[3].append("python")


```

