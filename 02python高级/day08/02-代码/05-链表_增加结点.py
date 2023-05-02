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

# 判断链表是否为空
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

# 获取链表长度
    def length(self):
        # 游标记录当前所在的位置
        cur = self.head
        # 记录链表的长度
        count = 0

        while cur is not None:
            cur = cur.next
            count += 1

        return count

# 遍历链表
    def travel(self):
        # 游标记录当前所在的位置
        cur = self.head

        while cur is not None:
            print(cur.item)
            cur = cur.next

# 头部增加结点
    def add(self, item):
        # 新结点存储新数据
        node = SingleNode(item)
        node.next = self.head
        self.head = node

# 尾部增加结点
    def append(self, item):
        # 新结点存储新数据
        node = SingleNode(item)

        # 判断是否是空链表
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            # 找到尾结点
            while cur.next is not None:
                cur = cur.next

            cur.next = node

# 指定位置增加结点
# insert(pos, item)
    def insert(self, pos, item):
        # 头部增加新结点
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            # 游标
            cur = self.head
            # 计数
            count = 0
            # 新结点
            node = SingleNode(item)

            # 1找到插入位置的前一个结点
            while count < pos - 1:
                cur = cur.next
                count += 1

            # 2完成插入新结点
            node.next = cur.next
            cur.next = node



if __name__ == '__main__':
    # 结点
    node1 = SingleNode(10)
    print(node1.item)
    print(node1.next)
    # 链表
    link1 = SingleLinkList()
    print(link1.head)
    link2 = SingleLinkList(node1)
    print(link2.head.item)
    # 判空
    print(link1.is_empty())
    print(link2.is_empty())
    # 长度
    print(link1.length())
    print(link2.length())
    # 遍历
    link2.travel()
    # 头部增加结点
    link2.add(9)
    link2.travel()
    # 尾部增加结点
    link2.append(11)
    link2.travel()
    # 指定位置增加结点
    link2.insert(100,0)
    link2.travel()


