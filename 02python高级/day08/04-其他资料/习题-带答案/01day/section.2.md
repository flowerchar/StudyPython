# 每日练习题

1. 实现add(item) 链表头部添加元素

   ```python
   def add(self, item):
           """头部添加元素"""
           # 先创建一个保存item值的节点
           node = SingleNode(item)
           # 将新节点的链接域next指向头节点，即_head指向的位置
           node.next = self.__head
           # 将链表的头_head指向新节点
           self.__head = node
   ```

   

2. 实现append(item) 链表尾部添加元素

   ```python
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

   

3. 实现insert(pos, item) 指定位置添加元素

   ```python
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

   

4. 实现remove(item) 删除节点

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

   

5. 实现search(item) 查找节点是否存在

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

   