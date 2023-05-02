# 每日练习题

## 题目1

### 题干

- 使用os模块创建一个名为“Python”的文件夹
- 获取Python文件夹当前所在目录
- 获取当前的目录列表
- 改变文件的操作路径
- 将Python文件夹删除

### 训练目标

- os模块的使用

### 训练提示

os模块基础命令的使用

### 参考方案

创建文件mkdir

当前所在目录getcwd

当前的目录列表listdir

改变文件的操作路径chdir

删除文件夹rmdir

### 操作步骤

### 参考答案

```python
import os
# 01
os.mkdir("Python")
# 02
os.getcwd()
# 03
os.listdir("./")
# 04
os.chdir("../")
# 05
os.rmdir("Python")
```



## 题目2

### 题干

编写一段代码以完成两份文件之间的相互备份

- 提示用户输入文件名。例：gailun.txt

- 创建已用户输入的名字的文件

- 打开文件写入如下信息

  ​	功夫，周星驰

  ​	一出好戏，黄渤

  ​	我不是药神，徐峥

- 将输入的数据输出到终端上

- 在文件夹中创建gailun副本.txt文件

- 将gailun.txt文件中的数据写入gailun副本.txt文件中

- 打开文件，查看文件中内容

### 训练目标

- 文件的综合使用

### 训练提示

- 每次操作完文件需要关闭
- 在windows系统中注意编码格式问题
- 需要自己重新定义一个新的文件名

### 参考方案

### 操作步骤

- 操作步骤一
  - 提示用户输入文件名
  - 打开文件
  - 写入信息
  - 关闭文件
  - 打开文件
  - 读取文件中的信息
- 操作步骤二
  - 提取文件名的后缀
  - 组建新的文件名
- 操作步骤三
  - 打开新组建的文件名字的文件
  - 写入文步骤一中读取到的信息写入到新的文件中
  - 关闭文件
- 操作步骤四
  - 打开新的文件
  - 读取文件中的内容
  - 关闭文件

### 参考答案

```python
# 提示输入文件
oldFileName = input("请输入要创建的文件名:")
# 以写的方式打开文件
oldFile = open(oldFileName, 'w', encoding="utf8")
oldFile.write("功夫，周星驰\n一出好戏，黄渤\n我不是药神，徐峥")
oldFile.close()
#d打开文件
f = open(oldFileName, 'r', encoding="utf8")
#读取文件内容
context = f.readlines()
print(context)
f.close()

# 提取文件名的后缀
fileFlagNum = oldFileName.rfind('.')
if fileFlagNum > 0:
    fileFlag = oldFileName[fileFlagNum:]

# 组织新的文件名字
newFileName = oldFileName[:fileFlagNum] + '复本' + fileFlag

# 创建新的文件副本
newFile = open(newFileName, 'w',encoding="utf8")
for lineContent in context:
    print(lineContent)
    newFile.write(lineContent)
newFile.close()

# 打开写入的新文件
f = open(newFileName, "r", encoding="utf8")
# 读取内容
context = f.read()
# 输入到终端
print(context)
# 关闭文件
f.close()
```



## 题目3

### 题干

- 创建一个新项目中新创建一个名字py文件夹
- 进入py文件夹中创建5个文件，文件名分别为python基础班-1.txt，python基础班-2.txt，python基础班-3.txt，python基础班-4.txt，python基础班-5.txt
- 然后将py文件夹中的所有文件都改名为[Python]python基础班-1.txt，[Python]python基础班-2.txt，[Python]python基础班-3.txt，[Python]python基础班-4.txt，[Python]python基础班-5.txt

### 训练目标

- os模块的综合使用

### 训练提示

- 首先创建文件夹，创建文件
- 然后，获取当前文件夹下所有文件
- 最后进行重命名

### 参考方案

- 创建文件夹mkdir
- 进入文件夹中chdir
- 获取文件夹中所有的文件listdir
- 重命名rename

### 操作步骤

- 第一部分
  - 创建文件夹
  - 进入文件夹中
  - 循环遍历创建五个文件，每创建一个后关闭文件
- 第二部分
  - 获取文件夹中所有的文件
  - 遍历获取后的文件，并修改文件名称

### 参考答案

```python
# 第一部分
import os
# 创建文件夹
os.mkdir("py")
# 进入py文件夹中
os.chdir("py")
# 创建5个文件
for i in range(1, 6):
    f = open("python基础班-%d.txt" % i, "w")
    f.close()

# 第二部分
# 进入py文件夹中,由于上边代码中已经进入到“py”文件夹里面，这里就不用再次进入了
# os.chdir("py") 
# 获取py文件夹中所有的文件
filename_list = os.listdir()
# 遍历文件
for file_name in filename_list:
    # 进行修改
    new_file_name = "[Python]" + file_name
    os.rename(file_name, new_file_name)
```

