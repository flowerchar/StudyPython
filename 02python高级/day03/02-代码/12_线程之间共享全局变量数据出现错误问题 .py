import threading


# 全局变量
g_num = 0


# 对g_num进行加操作
def sum_num1():
    for i in range(1000000):
        global g_num
        g_num += 1

    print("g_num1:", g_num)


# 对g_num进行加操作
def sum_num2():
    for i in range(1000000):
        global g_num
        g_num += 1

    print("g_num2:", g_num)


if __name__ == '__main__':
    # 创建子线程
    sum1_thread = threading.Thread(target=sum_num1)
    sum2_thread = threading.Thread(target=sum_num2)

    # 启动线程
    sum1_thread.start()
    sum2_thread.start()