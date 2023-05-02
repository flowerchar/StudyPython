# 企业面试题

1. 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型

   ```python
   class Solution:
       def __init__(self):
           self.stack1 = []
           self.stack2 = []
       def push(self,node):
           self.stack1.append(node)
       def pop(self):
           if self.stack2 == []:
               while self.stack1:
                   self.stack2.append(self.stack1.pop())
               return self.stack2.pop()
           return self.stack2.pop()
   ```

   

2. 两个队列实现一个栈

   > 思路: 
   >
   > 进栈：元素入队列A
   >
   > 出栈：判断如果队列A只有一个元素，则直接出队。否则，把队A中的元素出队并入队B，直到队A中只有一个元素，再直接出队。为了下一次继续操作，互换队A和队B。

   ```python
   class Solution:
       def __init__(self):
           self.queue1 = []
           self.queue2 = []
       def add(self, node):
           # write code here
           self.queue1.append(node)
    
       def dele(self):
           # return xx
           if self.queue1 == []:
              return None
           while len(self.queue1) != 1:
               self.queue2.append(self.queue1.pop(0))
           self.queue1,self.queue2 = self.queue2,self.queue1##交换是为了下一次的pop
           return self.queue2.pop()
   ```

   