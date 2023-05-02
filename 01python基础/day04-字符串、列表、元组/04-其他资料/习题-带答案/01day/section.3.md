# 企业面试题

## 1.元组元素求和b=(1,2,3,4,5,6,7,8,9)

```python
b = (1, 2, 3, 4, 5, 6, 7, 8, 9)
total = 0
for i in b:
    # print(i)
    total += i
print(total)

```

## 2. 输出元组内7的倍数及个位为7的数

```python
b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
for i in b:
    if i % 7 == 0 or i % 10 == 7:
        print(i)
```

##3. 列表倒数 a=[123,4567,12,3456] 输出 a = [321, 7654, 21, 6543]

```python
a = [123, 4567, 12, 3456]
b = []
for i in a:
    i = str(i)  # 将int值转换成字符串类型的值
    i = i[::-1]
    print(i)
    i = int(i)
    print(type(i))
    b.append(i)
print(b)
```

##4. 统计数字，字母，下划线个数 比如:a = '123456abcdaABCDEKO_'

```python
a = '123456abcdaABCDEKO_'

num = 0  # 记录数字的个数
char = 0  # 记录字符的个数
xhx = 0  # 记录下划线的个数

for i in a:
    if i >= '0' and i <= '9':
        '''判断是否是数字'''
        num += 1
    elif (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
        '''判断是否是字母'''
        char += 1
    else:
        '''判断是否是下划线'''
        xhx += 1

print(num, char, xhx)

或者是:
num = 0  # 记录数字的个数
char = 0  # 记录字符的个数
xhx = 0  # 记录下划线的个数
for i in a:
    if i.isdigit():
        '''判断是否是数字'''
        num += 1
    elif i.isalpha():
        '''判断是否是字母'''
        char += 1
    else:
        '''判断是否是下划线'''
        xhx += 1

print(num, char, xhx)
```

