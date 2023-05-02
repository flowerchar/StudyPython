# 尾部插入删除数据
# append(item), pop()

class Stack(object):
    """栈:先进后出"""
    def __init__(self):
        self.__items = []

    def push(self, item):
        """进栈"""
        self.__items.append(item)

    def pop(self):
        """出栈"""
        self.__items.pop()

    def travel(self):
        """遍历"""
        for i in self.__items:
            print(i)

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.travel()

# 出栈 3 先出去
my_stack.pop()
my_stack.travel()


