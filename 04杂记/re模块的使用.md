正则表达式在信息提取上有着很大威力，下面是一些基础知识点

# 正则基础知识

## 元字符

| 元字符 | 匹配内容 |
| :- | :-------- |
| .| 除开换行符以外的任意字符        |
| \w| 匹配（字母，数字，下划线|
| \s|匹配任意空白符|
| \d|匹配数字|
| \W| 匹配非（字母，数字，下划线）但是不能匹配汉字 |
| \S|匹配非空白符，可以匹配到汉字|
| \D|匹配非数字，可以匹配到汉字|
| \n|匹配换行符|
| \t|匹配一个制表符|
| \b|匹配一个单词的边界|
|^|匹配一个字符串的起始|
|$|匹配一个字符串的结尾|
|a \| b|匹配a或者b|
|[123456]|[]表示一个集合，可以匹配1-6其中一个|
|[^123456]|匹配除开1-6的所有字符|
|()|()里面的为一个组别|



## 量词
|量词|说明|
| :- | :-------- |
| * |重复零次或者更多次|
| +|重复一次或者更多次|
|  ?|重复零次或者一次|
|{n}|精确重复n次|
|{n,}|重复至少n次|
|{n,m}|重复至少n次，至多m次|



---

# re模块的基本使用

Python内置有处理正则表达式的re库

## 常用方法

- re.match(pattern,string,flags) 
  
  > Try to apply the pattern at the start of the string, returning a Match object, or None if no match was found.

- re.search(pattern,string,flags=0)
  
  > Scan through string looking for a match to the pattern, returning a Match object, or None if no match was found
  
- re.findall(pattern,string,flags=0)
  > Return a list of all non-overlapping matches in the string.If one or more capturing groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group.Empty matches are included in the result.
  

## 初试牛刀

1. ```python
   import re
   
   s1 = '中国香港日本大阪中国台湾中国江苏'
   r1 = re.search(r'中国(香港|台湾|江苏)', s1)
   print(r1.group())# 中国香港
   print(r1.group(0))# 中国香港
   print(r1.group(1))# 香港
   print(r1.group(2)) # 报错
   print(r1.groups()) # ('香港',)
   ```
   
   search会从字符串中搜索第一个匹配的值，成功则返回match对象，否则None
   
   
   
2. 

   ```python
   s1 = 'man are advanced animals'
   s2 = 'woman are advanced animals'
   r1 = re.search(r'(wo)?man',s1)
   r2 = re.search(r'(wo)?man',s2)
   print(r1.group())# man
   print(r2.group())# woman
   
   ```

   ？在圆括号后面表明模式是可选的，甚至可以理解成？的原意，“匹配？之前的分组零次或者一次”



  3. 

     ```python
     s1 = 'hahahahaha'
     r1 = re.search(r'(ha){1,5}',s1)
     r2 = re.search(r'(ha){1,5}?',s1)
     print(r1.group())# hahahahaha
     print(r2.group())# ha
     ```

     python的正则模块默认是贪心匹配，非贪婪模式可以在量词后面加上？



   4. 

      ```python
      s1 = 'Cell: 415-555-9999 Work:212-555-0000'
      r1 = re.findall(r'\d{3}-\d{3}-\d{4}',s1)
      r2 = re.findall(r'(\d{3})-(\d{3})-(\d{4})',s1)
      print(r1)# ['415-555-9999', '212-555-0000']
      print(r2)# [('415', '555', '9999'), ('212', '555', '0000')]
      ```

      findall()返回一个列表，而不是Match对象：

      1. 如果作用在一个没有分组的模式上，返回一个匹配字符串的列表
      2. 如果作用在有分组的模式上，返回一个元组列表，列表里的每一个元组对应一个匹配到的字符串，元组里的每一个元素又对应匹配到字符串里的分组

   5.

   ```python
s1 = '123...456'
r1 = re.findall(r'[1-9.]',s1)
print(r1)
# ['1', '2', '3', '.', '.', '.', '4', '5', '6']
   ```

   在[]内部的字符如.之类的，不会再被解释为特殊字符，即不需\转义


​      

   6.
   ```python
s1 = '123456789'
s2 = '123 456798'
r1 = re.search(r'^\d+$',s1)
r2 = re.search(r'^\d+$',s2)
print(r1 == None)# False
print(r2 == None)# True
   ```

   ^.*?$就要求字符串从头到尾都要匹配上，而不是匹配到一个子串
	
   7.

   ```python
s1 = '''I wanna be the knight
	  who guards you,
	  my princess'''
r1 = re.search(r'.*',s1)
r2 = re.search(r'.*',s1,re.DOTALL)
print(r1.group())# I wanna be the knight
print(r2.group())# s1原文
   ```
   re.DOTALL(re.S)表示.可以匹配换行符，即.能匹配所有字符。同理常用的还有re.IGNORE(re.I)表示忽略字母大小写匹配


## 高级用法

1. re.sub(pattern,repl,string,count=0,flags=0) 

   >pattern:采用的什么模式
   >
   >repl:把匹配上的字符串匹配成什么字符串
   >
   >string:作用在哪一个字符串上面
   >
   >count:表示替换的次数，为1就只能替换1次
   >
   >flags：忽略大小写之类
   >
   >return: 返回值为替换后的新字符串,没匹配上则返回string

   ```python
   s1 = '糖果超咸呜啦啦呜啦啦糖果超甜'
   s2 = re.sub(r'糖果超[酸甜苦辣咸]','鼻屎超黏',s1)
   print(s2)# 鼻屎超黏呜啦啦呜啦啦鼻屎超黏
   ```

   subn的作用跟sub一样，只是subn返回值为元组，第一个元素为替换后的字符串，第二个元素为替换的次数

2. 

   ```python
   s1 = re.search(r'''
   (\s|-|\.)?
   (\d{4})  # 配4个数字
   ''','asdasdasdas5453',re.VERBOSE|re.IGNORE
   ```

   如果模式太长并且有注释时还想忽略大小写，可以如上写

3. 

   ```python
   s1 = '杨千嬅的专辑电光幻影很好听'
   s2 = re.sub(r'(杨)(.{2})(.*)(电.{3})(.*)',r'\1小姐\3\2盛放也\5',s1)
   print(s2)
   ```
   比如一些公开的中奖数据，需要对中奖人的名以及电话号码的中间四位打码，那么可以使用分组替换，把中奖人的名保留下来，后面的以及电话改为***这样

4. re.split(pattern,string,maxsplit=0,flags=0)   
  > patttern:匹配的模式
  >
  > string:需要切割的源字符串
  >
  > maxsplit:切割的最大次数，默认为0
  >
  > flags:标识

  ```python
  s1 = 'this0is12a321string4of56numbers789and letters'
  r1 = re.split(r'\d+| ',s1)
  print(r1)
  # ['this', 'is', 'a', 'string', 'of', 'numbers', 'and', 'letters']
  ```

5. re.finditer(pattern,string,flags=0)

   > 该方法的返回值是一个迭代器对象，每一个迭代器生成的元素都是一个Match对象，这个方法既有findall全局搜索的特点，又整合了match,search所返回的Match对象特点，如果没有匹配到，也不会报错，而是返回一个空的迭代器

   ```python
   s1 = '[{"hero_id":001,"hero_name":"森林之女"},{"hero_id":002,"hero_name":"时空猎手"}]'
   pat = r'"hero_id":(?P<ID>\d+).*?name":"(?P<NAME>.*?)"'
   r1 = re.finditer(pat,s1)
   for i in r1:
       print(f'ID:{i.group("ID")} NAME:{i.group("NAME")}')
   # ID:001 NAME:森林之女
   # ID:002 NAME:时空猎手
   ```

6. 如果需要对一段字符串多次提炼，可以先把匹配模式先编译成为一个正则表达式对象，这样可以加快后面的速度

   ```python
   s1 = r'C:\Users\DELL\AppData\Local\Programs\Python\Python39\python.exe'
   pat1 = re.compile(r'.*?\\Users\\(?P<type>.*?)\\')
   r1 = pat1.search(s1)
   print(r1.group('type'))# DELL
   ```

   注意如果是使用的类似re.search()之类的方法，flags放在函数形参位置即可，但是一个正则表达式如pat1.search()这里不能加入flags，只有在编译的时候pat1=re.compile(flags)这里传入标识。

7. 总结一下Match对象的常用方法

   | 属性或方法 | 说明 |
   | :--  | :--- |
   | pos|搜索的开始位置|
   | endpos|搜索的结束位置|
   | string|匹配的原字符串|
   |re|返回对应的正则表达式对象|
   |lastindex|返回最后一个分组的索引，没有则返回None|
   |lastgroup|返回最后一个分组的别名，没有则返回None|
   |group(index=0)|传入某个分组索引(或者传入别名也行)，0是返回整个表达式|
   |groups()|返回所有分组，结构为元组|
   |groupdict()|返回key为组名,value为值的字典|
   |start([group])|返回一个组的开始位置|
   |end([group])|返回一个组的结束位置|
   |span([group])|获得一个组的开始和结束位置|
   

# re冷知识

1. 提取一段文本里的所有汉字,utf-8:[\u4e00-\u9fa5]
2. re里match对象的span把中文字符看成一个单位
3. 使用.*?可以屏蔽无用的字符
















