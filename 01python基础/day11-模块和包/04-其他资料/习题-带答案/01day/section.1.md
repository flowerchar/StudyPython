# 每日必会题

## 题干1

使用面向对象编程思想完成学员管理系统的开发, 编写系统启动的入口文件main.py和学生类文件student.py

```python
main.py文件内容如下
# 导入模块student_manager
from student_manager import *

if __name__ == "__main__":
    # 启动 学生管理系统
    sm = StudentManager()
    sm.startup()
```

```python
student.py文件内容如下
class Student:
    """
    定义一个学生类,用来封装学生的4个信息
    """

    def __init__(self, id, name, score):
        """
        给对象添加3个属性
        :param id: 学号
        :param name: 姓名
        :param score: 分数
        """
        self.id = id
        self.name = name
        self.score = score

    def __str__(self):
        return "%s,%s,%s" % (self.id, self.name, self.score)
```

## 题干2

使用面向对象编程思想完成学员管理系统的开发, 编写管理系统文件student_manager.py, 首先完成功能展示界面show_menu()

```python
# 导入Student类
from student import Student


class StudentManager:
    """
    定义一个学生管理类,在这个类中定义显示菜单和对学生进行增删改查的方法
    """

    def __init__(self):
        # 定义一个类属性, 用来存储系统中的Student对象
        self.students_dict = {}

    @staticmethod
    def show_menu():
        """
        显示菜单:
        ******************************
        欢迎使用【学生管理系统】 V1.0
        1.添加学生
        2.显示全部
        3.查询学生
        4.修改学生
        5.删除学生
        0.退出系统
        ******************************
        """
        print("*" * 30)
        print("欢迎使用【学生管理系统】 V1.0")
        print("1.添加学生")
        print("2.显示全部")
        print("3.查询学生")
        print("4.修改学生")
        print("5.删除学生")
        print()
        print("0.退出系统")
        print("*" * 30)

```

## 题干3

完成管理系统的启动控制功能startup()和添加学生的功能接口add_student()

```python
# 导入Student类
from student import Student


class StudentManager:
    """
    定义一个学生管理类,在这个类中定义显示菜单和对学生进行增删改查的方法
    """

    def __init__(self):
        # 定义一个类属性, 用来存储系统中的Student对象
        self.students_dict = {}

    def startup(self):
        """
        学生管理系统的入口,系统一启动的时候就应该调用这个方法
        """

        # 在系统一启动的时候就从文件中读取数据,把数据保存到students_dict中
        self.load_from_file("data.txt")

        # 循环1,2,3步骤
        while True:
            # 1.调用StudentManager类中显示菜单的功能
            self.show_menu()

            # 2.提示录入菜单编号
            menu_code = int(input("请录入您选择的功能:"))

            # 3.根据菜单编号调用对应的功能
            if menu_code == 1:
                self.add_student()
            elif menu_code == 2:
                pass
            elif menu_code == 3:
         				pass
            elif menu_code == 4:
                pass
            elif menu_code == 5:
                pass
            elif menu_code == 0:
                print("退出系统")
                # 在退出系统时,把学生列表中的数据都保存到文件中        self.save_to_file("data.txt")
                break
            else:
                print("录入的菜单编号有误,请重新录入!!!\n")

    @staticmethod
    def show_menu():
        """
        显示菜单:
        ******************************
        欢迎使用【学生管理系统】 V1.0
        1.添加学生
        2.显示全部
        3.查询学生
        4.修改学生
        5.删除学生

        0.退出系统
        ******************************
        """
        print("*" * 30)
        print("欢迎使用【学生管理系统】 V1.0")
        print("1.添加学生")
        print("2.显示全部")
        print("3.查询学生")
        print("4.修改学生")
        print("5.删除学生")
        print()
        print("0.退出系统")
        print("*" * 30)
    def add_student(self):
        """
        添加一个学生
        """
        # 提示并录入学生的3个信息
        id = input("请录入学号:")
        name = input("请录入姓名:")
        score = input("请录入考试分数:")

        # 把字典添加到列表中
        if id in self.students_dict.keys():
            print("学生已存在!!!")
            return

        else:
            # 把3个信息封装到一个Student对象中
            student = Student(id, name, score)
            self.students_dict[id] = student

            # 提示"添加成功!"
            print("添加学生" + id + "成功!\n")

        print(self.students_dict)
		def add_student(self):
        """
        添加一个学生
        """
        # 提示并录入学生的3个信息
        id = input("请录入学号:")
        name = input("请录入姓名:")
        score = input("请录入考试分数:")

        # 把字典添加到列表中
        if id in self.students_dict.keys():
            print("学生已存在!!!")
            return

        else:
            # 把3个信息封装到一个Student对象中
            student = Student(id, name, score)
            self.students_dict[id] = student

            # 提示"添加成功!"
            print("添加学生" + id + "成功!\n")

        print(self.students_dict)
```

## 题干4

完成管理系统的显示全部学生的功能接口

```python
def show_all(self):

        # 判断系统中是否有学生信息
        if len(self.students_dict) <= 0:
            # 如果没有,就提示"系统中还没有学生信息!!!"
            print("系统中还没有学生信息!!!\n")
        else:
            # 如果有
            # 先打印表头,一条线
            print("学号".ljust(14) + "姓名".ljust(15) + "分数".ljust(15))
            print("-" * 45)
            # 4.2 遍历列表,打印每个学生,一个学生打印成干一行
            for student in self.students_dict.values():
                id = student.id
                name = student.name
                score = student.score
                print(id.ljust(15) + name.ljust(15) + score.ljust(15))
            # 4.3 打印一条线
            print("-" * 45)
```





