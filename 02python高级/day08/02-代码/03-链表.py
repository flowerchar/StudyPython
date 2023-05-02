# 链表结点实现
class SingleNode(object):
    def __init__(self, item):
        # item: 存放元素
        self.item = item
        # next: 标识下一个结点
        self.next = None

# 单链表的实现
class SingleLinkList(object):
    def __init__(self, node=None):
        # head: 首节点
        self.head = node

# 结点
node1 = SingleNode(10)
print(node1.item)
print(node1.next)
# 链表
link1 = SingleLinkList()
print(link1.head)
link2 = SingleLinkList(node1)
print(link2.head.item)
