# 企业面试题

## 题干1

介绍一下except的作用和用法?

**参考答案**

```python
try:
pass
except Exception as e:
print(e)
finally:
pass
```

捕获try except中间代码发生的异常，如果发生异常执行except的代码，不管是否发生异常都执行finally中的代码

except可以有0个或多个，如果有多个从上到下依次根据异常类型匹配，匹配某个Exception这执行对应的except中代码

## 题干2

IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常?

**参考答案**

IOError：输入输出异常

AttributeError：试图访问一个对象没有的属性

ImportError：无法引入模块或包，基本是路径问题

IndentationError：语法错误，代码没有正确的对齐

IndexError：下标索引超出序列边界

KeyError:试图访问你字典里不存在的键

SyntaxError:Python代码逻辑语法出错，不能执行

NameError:使用一个还未赋予对象的变量