# 7 常见时间复杂度

|执行次数函数举例	|阶	|非正式术语|
|-----------|:--------:|:-------|
|12	|O(1)|	常数阶|
|2n+3	|O(n)	|线性阶|
|3n<sup>2</sup>+2n+1|	O(n<sup>2</sup>)|	平方阶|
|5log<sub>2</sub>n+20	|O(logn)	|对数阶|
|2n+3nlog<sub>2</sub>n+19	|O(nlogn)	|nlogn阶|
|6n<sup>3</sup>+2n<sup>2</sup>+3n+4	|O(n<sup>3</sup>)	|立方阶|
|2<sup>n</sup>	|O(2<sup>n</sup>)	|指数阶|

**注意，经常将log<sub>2</sub>n（以2为底的对数）简写成logn**

## 常见时间复杂度之间的关系  
![算法效率关系](/images/算法效率关系.bmp)

所消耗的时间从小到大

 **O(1) < O(logn) < O(n) < O(nlogn) < O(n<sup>2</sup>) < O(n<sup>3</sup>) < O(2<sup>n</sup>) < O(n!) < O(n<sup>n</sup>)**

> 练习：
时间复杂度练习( 参考算法的效率规则判断 )  
O(5)  
O(2n + 1)  
O(n²+ n + 1)  
O(3n³+1)  
