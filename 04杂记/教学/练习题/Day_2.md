### 1. 给定一个英语句子，删除重复单词并且按照字典序排序打印出来，例如获得英语句子：

> ```
> hello world and practice makes perfect and hello world again
> ```

经过程序运行后得到：

> ```
> again and hello makes perfect practice world
> ```

**提示：善于利用Python里的数据结构，set是Python里的集合，特点是没有重复元素，list是列表，内嵌有大量预定义的函数可以调用，有一个sorted函数可以进行排序**

```python
s = input()
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))
```



### 2.编写一个程序，它接受一系列逗号分隔的 4 位二进制数作为输入，然后检查它们是否可以被 5 整除。 可被 5 整除的数字将以逗号分隔的顺序打印，例如输入：

> ```
> 0100,0011,1010,1001
> ```

经过程序运行后得到：

> ```
> 1010
> ```

**提示：int()只有一个参数时可以把一个浮点数或者字符串转为整型，两个参数时，第二个位置可以指定进制，例如int('1010', 2)结果为十进制下的10**

```python
value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p,2)
    if not intp % 5:
        value.append(p)
print (','.join(value))
```





### 3. 编写一个程序，它将找出 1000 到 3000 之间的所有数字（都包括在内），使得该数字的每个数字都是偶数。获得的数字应以逗号分隔的顺序打印在一行上，例如运行后输出：

> 2000,2002,2004,2006.....,2884,2886,2888     ...是中间省略了一部分

**遍历[1000, 3000]得到每一个元素，再取每一个元素里的个十百千位，看对2取余是否全为零，是则该数字的每个数字都是偶数，反之不是**

```python
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2 == 0) and (int(s[1])%2 == 0) and (int(s[2])%2 == 0) and (int(s[3])%2 == 0):
        values.append(s)
print (",".join(values))
```

