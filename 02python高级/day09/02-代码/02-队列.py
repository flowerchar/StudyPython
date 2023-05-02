# Queue()
# 创建一个空的队列
class Queue(object):
    def __init__(self):
        # 存储数据 线性表
        self.items = []

    # enqueue(item)
    # 队列尾部添加元素item
    def enqueue(self, item):
        self.items.append(item)

    # dequeue():
    # 队列头部删除元素
    def dequeue(self):
        self.items.pop(0)

    # is_empty()
    # 判断队列是否为空
    def is_enpty(self):
        return self.items == []

    # size()
    # 返回队列的大小
    def size(self):
        return len(self.items)

q = Queue()
# 添加数据
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

for i in q.items:
    print(i)

# 删除数据
q.dequeue()
for i in q.items:
    print(i)

print(q.is_enpty())
print(q.size())

