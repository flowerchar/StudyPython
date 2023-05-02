# 每日必会题

## 题目1 

### 题干

在当前目录先，创建movie.txt文件，文件内容是：

​	功夫，周星驰

​	一出好戏，黄渤

​	我不是药神，徐峥

### 训练目标

- 文件的写操作

### 训练提示

- 如何往一个文件里面写入数据
- 写入的数据换行使用什么方法

### 参考方案

- 打开文件open，打开方式为“w”
- 写入文件write
- 换行使用“\n”
- 也可以使用""" """三个引号的形式，可以直接在代码里书写换行

### 操作步骤

- 打开文件，创建对象
- 写入信息
- 关闭文件

### 参考答案

- 第一种方式

```python
# 因为编码格式的问题，我们为了防止出现乱码，需要在这里设置encoding="utf8"
f = open("movie.txt","w",encoding="utf8")
f.write("功夫，周星驰\n一出好戏，黄渤\n我不是药神，徐峥")
f.close()
```

- 第二种方式

```python
f = open("movie.txt","w",encoding="utf8")
f.write("""功夫，周星驰
一出好戏，黄渤
我不是药神，徐峥""")
f.close()
```

## 题目2 

### 题干

将第一题创建好的文件打开，并读取内容

- 一次全部读取
- 每次读取一行

### 训练目标

- 文件的读操作

### 训练提示

- 如何读取文件内容？
- 全部读取的方法？
- 每次读取一行的方法？
- 什么时候采用读取行的形式读取文件？

### 参考方案

- 打开文件open，打开方式为“r”
- 读取文件read
- 读取一行readline
- 读取所有行readlines

### 操作步骤

- 打开文件（使用r方式打开，如果不写那么默认是只读方式打开）
- 读取信息
- 关闭文件（每次操作完文件后要关闭文件）

### 参考答案

- 第一种方式

  ```python
  # 注意编码格式问题
  f = open("movie.txt",'r',encoding="utf8")
  content = f.read()
  f.close()
  print(content)
  ```

- 第二种方式

  ```python
  f = open("movie.txt",'r',encoding="utf8")
  content = f.readlines()
  f.close()
  # 读取后的内容是一个列表，注意列表中的数据中有一个"\n"。如果使用需要处理
  print(content)
  ```

- 第三种方式

  ```python
  f = open("movie.txt",'r',encoding="utf8")
  # 因为readline 每次读取一行，需要我们使用循环读取
  while True:
      content = f.readline()
      # 当我们读取的内容是空字符的时候跳出循环
      if content == "":
          break
      print(content)
  f.close()
  ```

  





