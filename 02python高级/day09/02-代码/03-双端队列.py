class Deque(object):
    """双端队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def size(self):
        """返回队列大小"""
        return len(self.items)

    def add_front(self, item):
        """头部添加数据"""
        self.items.insert(0, item)

    def add_rear(self, item):
        """尾部添加数据"""
        self.items.append(item)

    def remove_front(self):
        """头部删除数据"""
        self.items.pop(0)

    def remove_rear(self):
        """尾部删除数据"""
        self.items.pop()

deque = Deque()

print(deque.is_empty())
print(deque.size())

# 添加数据
deque.add_front(1)
deque.add_front(2)
deque.add_rear(3)
deque.add_rear(4)
for i in deque.items:
    print(i)

# 删除数据
deque.remove_front()
deque.remove_rear()
for i in deque.items:
    print(i)






