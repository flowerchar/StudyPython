# 每日必会题

1. 用面向对象的方法实现链表节点 

   ```python
   class SingleNode(object):
       """单链表的结点"""
       def __init__(self,item):
           # item存放数据元素
           self.item = item
           # next是下一个节点的标识
           self.next = None
   ```

2. 用面向对象的方法初始化单链表

   ```python
   class SingleLinkList(object):
       """单链表"""
       def __init__(self):
           self.__head = None
   ```

3. 实现单链表中判断链表是否为空的方法is_empty()

   ```python
   def is_empty(self):
           """判断链表是否为空"""
           return self.__head == None
   ```

4. 实现单链表中判断链表长度的方法length()

   ```python
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
         
   ```

5. 实现单链表中遍历链表的功能travel()

   ```python
   def travel(self):
           """遍历链表"""
           cur = self.__head
           while cur != None:
               print cur.item,
               cur = cur.next
           print("")
   ```

   