使用execjs库处理js代码

示例：

```python
import execjs
js_code = '''
    var a = 1;
    var b = 2;
    var c = a + b;
    var H = "hello world";    
    function add(a,b) {
        return a+b;
    }
'''
jsc_obj = execjs.compile(js_code)
return_value = jsc_obj.call('add',1,2)
print(f'value is {return_value} and type is {type(return_value)}')
a_value = jsc_obj.eval('a')
print(f'a is {a_value} and type is {type(a_value)}')
# value is 3 and type is <class 'int'>
# a is 1 and type is <class 'int'>
```

这个模块是先把js代码转换成一个字符串，再通过compile编译成为一个js对象

1.如果想要获得js对象里的一个变量，可以通过jsc_obj.eval('a')这样得到

2.如果想要执行js对象里的一个函数，可以通过jsc_obj.call('add',1,2)调用得到函数返回值，第一个参数为函数名，后面的参数为调用该函数的参数