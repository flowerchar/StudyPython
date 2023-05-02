# 企业面试题

##1. 阅读下面的代码，写出A0，A1至An的最终值。
```python

\1.    A0 = dict(zip(('a'，'b'，'c'，'d'，'e')，(1，2，3，4，5)))

\2.    A1 = range(10)

\3.    A2 = [i for i in A1 if i in A0]

\4.    A3 = [A0[s] for s in A0]

\5.    A4 = [i for i in A1 if i in A3]

\6.    A5 = {i:i*i for i in A1}

\7.    A6 = [[i，i*i] for i in A1]
```

##2.  range和xrange的区别？

## 3. 考虑以下Python代码，如果运行结束，命令行中的运行结果是什么？

```python

\1.  l = []

\2.   for  i  in  xrange(10):

\3.       l.append({‘num’:i})

\4.   print l
```
载考虑以下代码，运行结束后的结果是什么？

```python
\1.   l = []

\2.   a = {‘num’:0}

\3.   for i in xrange(10):

\4.       a[‘num’] = i

\5.       l.append(a)

\6.   print l
```
以上两段代码的运行结果是否相同，如果不相同，原因是什么？

##4. 以下Python程序的输出？

```python
\1. for i in range(5，0，-1):

\2.       print(i)

```
