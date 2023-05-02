# 企业面试题

##1. 生成如下列表 [[0,0,0,0,0,],[0,1,2,3,4,],[0,2,4,6,8,],[0,3,6,9,12,]]

###方案一:

```python
list1 = []
for in range(4):
    temp = []
    for j in range(5):
        temp.append(j*i)
    list1.append(temp)

print(list1)
```

### 方案二:

```python
list1 =[[ i*j for j in range(5)] for i in range(4)]
print(list1)
```

## 2. 把列表`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`中的每个元素都加100，生成一个新列表

### 方案一:

```python
list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = []
for i in list1:
    list2.append(i+100)
print(list2)
```

### 方案二:

```python
list2 = list(map(lambda x:x+100,list1))
print(list2)
```

### 方案三:

```python
list2 = [i+100 for i in list1]
print(list2)
```

##3. 根据提供的两个列表, 生成指定的列表

```python
已知:list1 = ["A","B","C"], list2 = ["X","Y","Z"]使用列表推导式生成['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

### 参考代码:

```python
print([x+y for x in list1 for y in list2])
```

