# 每日练习题

## 题干1

书写学生管理系统中的修改学生信息的接口modify_info(), 并在循环控制模块中添加器修改信息的接口

```python
def modify_info():
    """修改学生信息"""
    global info_list

    modify_num = int(input("请输入要修改的序号:"))
    if 0 <= modify_num < len(info_list):
        print("你要修改的信息是:")
        print("name:%s, tel:%s, QQ:%s" % (info_list[modify_num]['name'],
            info_list[modify_num]['tel'],info_list[modify_num]['qq']))
        info_list[modify_num]['name'] = input("请输入新的姓名:")
        info_list[modify_num]['tel'] = input("请输入新的手机号:")
        info_list[modify_num]['qq'] = input("请输入新QQ:")
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
            modify_info()
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

## 题干2

书写学生管理系统中的查询学生信息的接口search_info(), 并在循环控制模块中添加查询信息的接口

```python
def search_info():
    """查询学生信息"""
    search_name = input("请输入要查询的学生姓名:")
    for temp_info in info_list:
        if temp_info['name'] == search_name:
            print("查询到的信息如下:")
            print("name:%s, tel:%s, QQ:%s" % (temp_info['name'],
                temp_info['tel'], temp_info['qq']))
            break
    else:
        print("没有您要找的信息....")
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
            modify_info()
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

### 题干3

书写学生管理系统中的遍历学生信息的接口print_all_info(), 并在循环控制模块中添加遍历学生信息的接口及退出功能

```python
def print_all_info():
    """遍历学生信息"""
    print("序号\t姓名\t\t手机号\t\tQQ")
    i = 0
    for temp in info_list:
        # temp是一个字典
        print("%d\t%s\t\t%s\t\t%s" % (i, temp['name'], temp['tel'], temp['qq']))
        i += 1
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
            modify_info()
        elif num == "4":
            # 查询学生
            search_info()
        elif num == "5":
            # 遍历所有的信息
            print_all_info()
        elif num == "6":
            # 退出系统
            exit_flag = input("亲,你确定要退出么?~~~~(>_<)~~~~(yes or no) ")
            if exit_flag == "yes":
                break
        else:
            print("输入有误,请重新输入......")


        input("\n\n\n按回车键继续....")
        os.system("clear")  # 调用Linux命令clear完成清屏

# 程序的开始
main()       
```

