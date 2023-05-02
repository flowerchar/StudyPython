turtle绘图机制

> 有一个小海龟在坐标轴上移动，它的移动轨迹就是留在画布上的痕迹。海龟初始位置为画布正中心，面向x轴

![img](D:\markdown\python\教学\pictures\20200813113335400.png)

## 画布

- ###  设置宽高背景色

  turtle.screensize(canvwidth=None, canvheight=None, bg=None)

- ### 设置宽高以及距离电脑左上角的位置

  turtle.setup(width=800,height=800, startx=100, starty=100)



## 画笔

- ### 属性

  - 宽度：turtle.pensize()
  - 颜色：turtle.pencolor() 字符串或者RGB三元组
  - 速度：turtle.speed() 移动取值为[0,10]，越大越快

- ### 运动函数

  | 命令             | 说明 |
  | ---- | ---- |
  | turtle.forward(x) | 以当前方向移动x个像素的距离 |
  |turtle.backward(x)|以当前方向反方向移动x个像素距离|
  |turtle.right(x)|顺时针移动x度|
  |turtle.left(x)|逆时针移动x度|
  |turtle.pendown(x)|画笔落下|
  | turtle.goto(x,y)|移动到坐标x,y处|
  |turtle.circle()|画圆，半径为正，则圆心在画笔左边，反之右边|
  |turtle.penup()|提起画笔|
  |setx()|将当前x轴移到指定位置|
  |sety()|将当前y轴移到指定位置|
  |setheading(x)|设置当前朝向为x的角度|
  |home()|设置当前画笔位置为原点，朝向正东|
  |dot(r)|绘制一个指定直接的原点|

- ### 控制命令

  | 命令                          | 说明         |
  | ----------------------------- | ------------ |
  | turtle.fillcolor(colorstring) | 图形填充颜色 |
  |turtle.color(col1,col2)|col1为pencolor,col2为fillcolor|
  | turtle.begin_fill()|准备开始填充图形|
  |turtle.end_fill()|填充完成|
  |turtle.hideturtle()|隐藏画笔|
  |turtle.showturtle()|显示画笔|

  