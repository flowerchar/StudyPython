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
