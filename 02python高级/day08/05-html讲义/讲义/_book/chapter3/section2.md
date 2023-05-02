# 单向循环链表

单链表的一个变形是单向循环链表，链表中最后一个节点的next域不再为None，而是指向链表的头节点。

![单向循环链表](/images/单向循环链表.png)

### 操作

+ is_empty() 判断链表是否为空
+ length()  返回链表的长度
+ travel() 遍历
+ add(item) 在头部添加一个节点
+ append(item) 在尾部添加一个节点
+ insert(pos, item) 在指定位置pos添加节点
+ remove(item)  删除一个节点
+ search(item)  查找节点是否存在

### 实现

```python
class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkedlist(object):
    """单向循环链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        count = 1
        cur = self.__head
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        print cur.item,
        while cur.next != self.__head:
            cur = cur.next
            print cur.item,
        print ""


    def add(self, item):
        """头部添加节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            #添加的节点指向_head
            node.next = self.__head
            # 移到链表尾部，将尾部节点的next指向node
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            #_head指向添加node的
            self.__head = node

    def append(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 移到链表尾部
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 将尾节点指向node
            cur.next = node
            # 将node指向头节点_head
            node.next = self.__head

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.item == item:
                # 先判断此结点是否是头节点
                if cur == self.__head:
                    # 头节点的情况
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.item == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                # pre.next = cur.next
                pre.next = self.__head

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        if cur.item == item:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return False

if __name__ == "__main__":
    ll = SinCycLinkedlist()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print "length:",ll.length()
    ll.travel()
    print ll.search(3)
    print ll.search(7)
    ll.remove(1)
    print "length:",ll.length()
    ll.travel()
```
