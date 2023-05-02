# 每日练习题

## 题干1

使用面向对象编程思想完成学员管理系统的开发, 编写管理系统文件student_manager.py, 完成查询一个学生的接口find_student()

```python
		def find_student(self):
        """
        查询一个学生
        """

        # 提示录入一个姓名
        input_id = input("请录入一个学号:")
        # 遍历列表
        if input_id not in self.students_dict.keys():
            # 如果比较了一遍没有发现有姓名一样的学生,就提示在系统中没有找到此学生
            print("在系统中没有找到此学生!!!\n")
            return
        else:
            # 在系统中得到该学生对象
            student = self.students_dict[input_id]
            # 如果一样就打印
            print("学号".ljust(14) + "姓名".ljust(15) + "分数".ljust(15))
            print("-" * 45)
            id = student.id
            name = student.name
            score = student.score
            print(id.ljust(15) + name.ljust(15) + score.ljust(15))
            print("-" * 45)    def find_student(self):
        """
        查询一个学生
        """

        # 提示录入一个姓名
        input_id = input("请录入一个学号:")
        # 遍历列表
        if input_id not in self.students_dict.keys():
            # 如果比较了一遍没有发现有姓名一样的学生,就提示在系统中没有找到此学生
            print("在系统中没有找到此学生!!!\n")
            return
        else:
            # 在系统中得到该学生对象
            student = self.students_dict[input_id]
            # 如果一样就打印
            print("学号".ljust(14) + "姓名".ljust(15) + "分数".ljust(15))
            print("-" * 45)
            id = student.id
            name = student.name
            score = student.score
            print(id.ljust(15) + name.ljust(15) + score.ljust(15))
            print("-" * 45)
```

## 题干2

使用面向对象编程思想完成学员管理系统的开发, 编写管理系统文件student_manager.py, 完成修改学生的接口update_student()

```python
def update_student(self):
        """
        修改一个学生
        """

        # 1.提示录入一个学号
        input_id = input("请录入一个学号:")

        # 判断系统中是否有该学号对应的学生
        if input_id not in self.students_dict.keys():
            # 如果没有找到该学生
            print("在系统中没有找到此学生!!!\n")
            return
        else:
            # 如果找到了就打印该学生
            # 在系统中得到该学生对象
            student = self.students_dict[input_id]

            # 获得要修改的信息
            new_name = input('请输入新名字:')
            new_score = input('请输入新分数:')

            # 修改学生的姓名和分数
            student.name = new_name
            student.score = new_score

            # 提示修改变成功
            print("修改%s成功" % input_id)
```

## 题干3

使用面向对象编程思想完成学员管理系统的开发, 编写管理系统文件student_manager.py, 完成删除学生的接口delete_student()

```python
def delete_student(self):
        """
        删除一个学生
        """

        # 提示录入一个学号
        input_id = input("请录入一个学号:")

        # 判断系统中是否有该学号对应的学生
        if input_id not in self.students_dict.keys():
            # 如果没有找到
            print("在系统中没有找到此学生!!!\n")
            return
        else:
            # 如果找到了
            # 删除学生
            del self.students_dict[input_id]
            print("删除成功!!!\n")
```

## 题干4

使用面向对象编程思想完成学员管理系统的开发, 编写管理系统文件student_manager.py, 完成学生的信息保存到文件中的接口save_to_file()

```python
def save_to_file(self, file):
        """
        把列表中的数据写到指定的文件中
        :param file: 文件
        """

        # 得到字典中的所有学生
        student_list = self.students_dict.values()

        # 把所有学生 都写到一个文件中,一个学生写一行
        f = open(file, "w", encoding="UTF-8")

        for student in student_list:

            # 一个学生写一行
            f.write(str(student)+"\n")

        # 关闭文件
        f.close()
```

## 题干5

使用面向对象编程思想完成学员管理系统的开发, 编写管理系统文件student_manager.py, 完成学生的信息从文件中加载的接口load_from_file()

```python
def load_from_file(self, file):
        """
        从指定的文件中读取,并返回数据
        :param file:
        :return: 返回从文件中读出来的数据
        """
        f = open(file, "r", encoding="UTF-8")
        for line in f.readlines():
            # 得到一行的字符串,去掉最后的换行符"\n"
            student_info = line[:-1].split(",")
            # 得到学生的3个信息
            id = student_info[0]
            name = student_info[1]
            score = student_info[2]
            # 创建一个学生对象
            student = Student(id, name, score)
            # 在字典中保存学生对象
            self.students_dict[id] = student

        # 关闭文件
        f.close()
```

