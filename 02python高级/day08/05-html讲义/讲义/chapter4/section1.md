# 栈结构实现

栈可以用顺序表实现，也可以用链表实现。

### 栈的操作

* Stack() 创建一个新的空栈
* push(item) 添加一个新的元素item到栈顶
* pop() 弹出栈顶元素
* peek() 返回栈顶元素
* is_empty() 判断栈是否为空
* size() 返回栈的元素个数

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
    print stack.size()
    print stack.peek()
    print stack.pop()
    print stack.pop()
    print stack.pop()
```

执行过程如下：
![stack演示](/images/stack演示.gif)
