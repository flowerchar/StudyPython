# 企业面试题

## 题干1

4G内存怎么读取一个5G的数据？



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

## 题干4

一个大小为100G的文件log.txt,要读取文件中的内容，写出具体过程代码



