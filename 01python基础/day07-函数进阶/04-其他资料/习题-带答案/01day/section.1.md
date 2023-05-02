# 每日必会题

## 题干1

 书写学生管理系统中的界面展示部分

```python
def print_menu():
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("---------------------------")
def main():
  print_menu()
#程序开始
main()
```

## 题干2

书写学生管理系统中的添加学生信息接口add_new_info()并添加循环控制逻辑

```python
def add_new_info():
    """添加学生信息"""
    global info_list

    new_name = input("请输入姓名:")
    new_tel = input("请输入手机号:")
    new_qq = input("请输入QQ:")

    for temp_info in info_list:
        if temp_info['name'] == new_name:
            print("此用户名已经被占用,请重新输入")
            return  # 如果一个函数只有return就相当于让函数结束，没有返回值

    # 定义一个字典，用来存储用户的学生信息(这是一个字典)
    info = {}

    # 向字典中添加数据
    info["name"] = new_name
    info["tel"] = new_tel
    info["qq"] = new_qq

    # 向列表中添加这个字典
    info_list.append(info)
def main():
    """用来控制整个流程"""
    while True:
        # 1. 打印功能
        print_menu()

        # 2. 获取用户的选择
        num = input("请输入要进行的操作(数字)")

        # 3. 根据用户选择,做相应的事情
        if num == "1":
            # 添加学生
            add_new_info()
        elif num == "2":
            # 删除学生
            pass
        elif num == "3":
            # 修改学生
            pass
        elif num == "4":
            # 查询学生
            pass
        elif num == "5":
            # 遍历所有的信息
            pass
        elif num == "6":
            # 退出系统
            pass
        input("\n\n\n按回车键继续....")
        os.system("clear")  # 调用Linux命令clear完成清屏
main()
```

## 题干3

书写学生管理系统中的删除信息的接口del_info()并补充循环控制逻辑

```python
def del_info():
    """删除学生信息"""
    global info_list

    del_num = int(input("请输入要删除的序号:"))
    if 0 <= del_num < len(info_list):
        del_flag = input("你确定要删除么?yes or no")
        if del_flag == "yes":
            del info_list[del_num]
    else:
        print("输入序号有误,请重新输入")
        
def main():
    """用来控制整个流程"""
    while True:
        # 1. 打印功能
        print_menu()

        # 2. 获取用户的选择
        num = input("请输入要进行的操作(数字)")

        # 3. 根据用户选择,做相应的事情
        if num == "1":
            # 添加学生
            add_new_info()
        elif num == "2":
            # 删除学生
            del_info()
        elif num == "3":
            # 修改学生
            pass
        elif num == "4":
            # 查询学生
            pass
        elif num == "5":
            # 遍历所有的信息
            pass
        elif num == "6":
            # 退出系统
            pass
        input("\n\n\n按回车键继续....")
        os.system("clear")  # 调用Linux命令clear完成清屏
main()
```









