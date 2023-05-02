# 单向链表

单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。   

![单向链表图示](/images/单链表的节点和单链表.png)

+ 表元素域elem用来存放具体的数据。
+ 链接域next用来存放下一个节点的位置（python中的标识）
+ 变量p指向链表的头节点（首节点）的位置，从p出发能找到表中的任意节点。

### 节点实现

```Python
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None
```

### 单链表的操作

+ is_empty() 链表是否为空  
+ length() 链表长度  
+ travel() 遍历整个链表
+ add(item) 链表头部添加元素
+ append(item)  链表尾部添加元素
+ insert(pos, item) 指定位置添加元素
+ remove(item) 删除节点   
+ search(item) 查找节点是否存在  

### 单链表的实现

```Python
class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self.__head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print cur.item,
            cur = cur.next
        print ""
```

** 头部添加元素 **

![单链表表头插入元素](/images/单链表表头插入元素.png)

```Python
    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self.__head
        # 将链表的头_head指向新节点
        self.__head = node
```

** 尾部添加元素 **

```Python
    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self.__head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
```

** 指定位置添加元素 **

![单链表指定位置添加元素](/images/单链表指定位置添加元素.png)

```Python
    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node
```

** 删除节点 **

![单链表删除节点](/images/单链表删除节点.png)

```python
    def remove(self,item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
```

** 查找节点是否存在 **

```python
    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
```

** 测试 **

```python
if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print "length:",ll.length()
    ll.travel()
    print ll.search(3)
    print ll.search(5)
    ll.remove(1)
    print "length:",ll.length()
    ll.travel()
```

### 链表与顺序表的对比

链表失去了顺序表随机读取的优点，同时链表由于增加了结点的指针域，空间开销比较大，但对存储空间的使用要相对灵活。

链表与顺序表的各种操作复杂度如下所示：  

|操作 |链表|顺序表|
|-------|:-------:|-------|
|访问元素|O(n)|  O(1)|
|在头部插入/删除|O(1)|O(n)|
|在尾部插入/删除 | O(n)| O(1)|
|在中间插入/删除 | O(n) | O(n)|

注意虽然表面看起来复杂度都是 O(n)，但是链表和顺序表在插入和删除时进行的是完全不同的操作。链表的主要耗时操作是遍历查找，删除和插入操作本身的复杂度是O(1)。顺序表查找很快，主要耗时的操作是拷贝覆盖。因为除了目标元素在尾部的特殊情况，顺序表进行插入和删除时需要对操作点之后的所有元素进行前后移位操作，只能通过拷贝和覆盖的方法进行。
