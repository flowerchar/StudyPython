# 每日练习题

1. 什么是闭包?

   ```
   在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
   ```

2. 闭包的特点是什么?

   ```
   1.外部函数中定义了一个内部函数
   2.外部函数总是返回内部函数的引用
   3.内部函数可以使用外部函数提供的环境变量
   ```

3. 定义装饰器的语法?

   ```
   1.基础是闭包语法
   2.外层函数只有一个参数就是被装饰的函数的引用
   ```

4. **装饰器的功能** 

   ```
   1.引入日志
   2.函数执行时间统计
   3.执行函数前预备处理
   4.执行函数后清理功能
   5.权限校验等场景
   6.缓存
   ```

5. 装饰器工厂函数的作用

   ```
   1.产生装饰器对象，对函数进行装饰
   2.接收参数传入装饰器内部，以控制装饰器函数内部的逻辑
   ```

6. 写一个能打印出程序运行耗时的装饰器

   ```python
   import time,random
   def get_run_time(func):
   	def inner():
         start = time.time()
         func()
         stop = time.time()
         run_time = stop-start
         print("执行程序花费时间为：%s"%run_time)
     return inner

   @get_run_time
   def waste_time():
     time.sleep(random.random())  # random()方法返回[0,1)之间的数字

   waste_time()  
    #   def random(self): # real signature unknown; restored from __doc__
    #      """ random() -> x in the interval [0, 1). """
    #      pass
   ```

   ​

