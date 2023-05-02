# 每日必会题

1. 实现栈的结构及以下方法:

   > - Stack() 创建一个新的空栈
   > - push(item) 添加一个新的元素item到栈顶
   > - pop() 弹出栈顶元素
   > - peek() 返回栈顶元素
   > - is_empty() 判断栈是否为空
   > - size() 返回栈的元素个数

   ```python
   class Stack(object):
       """栈"""
       def __init__(self):
            self.items = []
   
       def is_empty(self):
           """判断是否为空"""
           return self.items == []
   
       def push(self, item):
           """加入元素"""
           self.items.append(item)
   
       def pop(self):
           """弹出元素"""
           return self.items.pop()
   
       def peek(self):
           """返回栈顶元素"""
           return self.items[len(self.items)-1]
   
       def size(self):
           """返回栈的大小"""
           return len(self.items)
   
   if __name__ == "__main__":
       stack = Stack()
       stack.push("hello")
       stack.push("world")
       stack.push("flower")
       print(stack.size())
       print(stack.peek())
       print(stack.pop())
       print(stack.pop())
       print(stack.pop())
   ```

2. 实现队列结构及以下方法:

   > - Queue() 创建一个空的队列
   > - enqueue(item) 往队列中添加一个item元素
   > - dequeue() 从队列头部删除一个元素
   > - is_empty() 判断一个队列是否为空
   > - size() 返回队列的大小

   ```python
   class Queue(object):
       """队列"""
       def __init__(self):
           self.items = []
   
       def is_empty(self):
           return self.items == []
   
       def enqueue(self, item):
           """进队列"""
           self.items.insert(0,item)
   
       def dequeue(self):
           """出队列"""
           return self.items.pop()
   
       def size(self):
           """返回大小"""
           return len(self.items)
   
   if __name__ == "__main__":
       q = Queue()
       q.enqueue("hello")
       q.enqueue("world")
       q.enqueue("flower")
       print(q.size())
       print(q.dequeue())
       print(q.dequeue())
       print(q.dequeue())
   ```

   

3. 阐述冒泡排序的思想

   > - 比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
   > - 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
   > - 针对所有的元素重复以上的步骤，除了最后一个。
   > - 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

4. 代码实现冒泡排序

   ```python
   def bubble_sort(alist):
       for j in range(len(alist)-1,0,-1):
           # j表示每次遍历需要比较的次数，是逐渐减小的
           for i in range(j):
               if alist[i] > alist[i+1]:
                   alist[i], alist[i+1] = alist[i+1], alist[i]
   
   li = [54,26,93,17,77,31,44,55,20]
   bubble_sort(li)
   print(li)
   ```

   