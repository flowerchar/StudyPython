# 企业面试题

## 题干1

4G内存怎么读取一个5G的数据？

**参考答案**

方法一：

可以通过生成器，分多次读取，每次读取数量相对少的数据（比如500MB）进行处理，处理结束后在读取后面的 500MB的数据。

方法二：

可以通过linux命令split切割成小文件，然后再对数据进行处理，此方法效率比较高。可以按照行数切割，可以按照文件大小切割。

## 题干2

有一个jsonline格式的文件file.txt大小约为10K

```python
def get_lines():
    with open('file.txt','rb') as f:
        return f.readlines()

if __name__ == '__main__':
    for e in get_lines():
        process(e) # 处理每一行数据
```

现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不变的情况下，应该如何实现？需要考虑的问题都有那些？

**参考答案**

```python
def get_lines():
    with open('file.txt', 'r') as f:
        for i in f:
            yield i
g = get_lines()
```

## 题干3

**补充缺失的代码**

```python
def print_directory_contents(sPath):
"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""
```

**参考代码**

```python
def print_directory_contents(sPath):
"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""
    import os
    for s_child in os.listdir(sPath):
        s_child_path = os.path.join(sPath, s_child)
        if os.path.isdir(s_child_path)
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)
```

## 题干4

一个大小为100G的文件log.txt,要读取文件中的内容，写出具体过程代码

**参考代码**

方案一:

```python
with open("xx/log.txt",encoding='utf8') as f:
    for line in f:
        print(line)
# 注意:for line in f 这种用法是把文件对象f当作迭代对象， 系统将自动处理IO缓冲和内存管理
```

方案二:

```python
def read_in_block(file_path):
    BLOCK_SIZE = 1024
    with open(file_path, "r",encoding='utf8') as f:
        while True:
            block = f.read(BLOCK_SIZE)  # 每次读取固定长度到内存缓冲区
            if block:
                yield block
            else:
                return  # 如果读取到文件末尾，则退出
file_path = "xxx/log.txt"
for block in read_in_block(file_path):
    print(block)
```

