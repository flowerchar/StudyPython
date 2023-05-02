import threading
import time


# 全局变量
my_list = []


# 写入数据
def write_data():
    for i in range(3):
        print("add:", i)
        my_list.append(i)
    print("write:", my_list)


# 读取数据
def read_data():
    print("read:", my_list)


if __name__ == '__main__':
    # 创建子线程
    write_thread = threading.Thread(target=write_data)
    read_thread = threading.Thread(target=read_data)

    # 启动线程
    write_thread.start()
    # 延时一秒
    time.sleep(1)
    read_thread.start()
