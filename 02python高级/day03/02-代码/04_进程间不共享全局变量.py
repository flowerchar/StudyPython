import multiprocessing
import time

# 全局变量
my_list = []


# 写入数据
def write_data():
    for i in range(3):
        my_list.append(i)
        print("add:", i)
    print("write_data", my_list)


# 读取数据
def read_data():
    print("read_data", my_list)


if __name__ == '__main__':
    # 创建写入数据进程
    write_process = multiprocessing.Process(target=write_data)
    # 创建读取数据进程
    read_process = multiprocessing.Process(target=read_data)

    # 启动进程执行相应任务
    write_process.start()
    time.sleep(1)
    read_process.start()