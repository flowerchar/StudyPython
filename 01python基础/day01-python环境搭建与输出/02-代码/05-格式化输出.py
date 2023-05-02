"""
1. 准备数据
2. 格式化符号输出数据
"""
age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
stu_id2 = 1000

# 1. 今年我的年龄是x岁 -- 整数 %d
print('今年我的年龄是%d岁' % age)
print(f"今年我是{age}")

# 2. 我的名字是x -- 字符串 %s
print('我的名字是%s' % name)
print(f"我的名字是{name}")

# 3. 我的体重是x公斤 -- 浮点数 %f
print('我的体重是%.3f公斤' % weight)
print(f"我的体重是{weight:0.3f}公斤")

# 4. 我的学号是x -- %d
print('我的学号是%d' % stu_id)
print(f"我的学号是{stu_id}")

# 4.1 我的学号是001
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)
print(f"我的学号是{stu_id:03d}")
print(f"我的学号是{stu_id2:03d}")

# 5. 我的名字是x，今年x岁了
print('我的名字是%s，今年%d岁了' % (name, age))
# 5.1 我的名字是x，明年x岁了
print('我的名字是%s，明年%d岁了' % (name, age + 1))
print(f"我的名字是{name}，今年{age}岁了")
print(f"我的名字是{name}，今年{age + 1}")

# 6. 我的名字是x，今年x岁了，体重x公斤，学号是x
print('我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%06d' % (name, age, weight, stu_id))
print(f"我的名字是{name}，今年{age}岁了，体重{weight:0.2f}公斤，学号是{stu_id:06d}")
