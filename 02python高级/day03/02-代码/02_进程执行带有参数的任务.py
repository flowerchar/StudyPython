# 导入进程模块
import multiprocessing
import time


# 编写代码
def coding(num, name):
    for i in range(num):
        print(name)
        print("coding...")
        time.sleep(0.2)


# 听音乐
def music(count):
    for i in range(count):
        print("music...")
        time.sleep(0.2)


if __name__ == '__main__':
    # coding()
    # music()
    # 通过进程类创建进程对象
    coding_process = multiprocessing.Process(target=coding, args=(3, "传智"))
    # 通过进程类创建进程对象
    music_process = multiprocessing.Process(target=music, kwargs={"count": 2})
    # 启动进程
    coding_process.start()
    music_process.start()


