# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
import time

start_time = time.time()

# ①列举a, b, c的所有可能的数值
for a in range(0 , 1001):
    for b in range(0 , 1001):
        for c in range(0 , 1001):
# ②判断是否满足条件
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                print("a b c:",a, b, c)

end_time = time.time()
cost_time = end_time - start_time
print(cost_time)