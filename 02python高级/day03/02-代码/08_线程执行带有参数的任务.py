import time
import threading


# 编写代码
def coding(num):
    for i in range(num):
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
    # 创建子线程
    coding_thread = threading.Thread(target=coding, args=(3,))
    music_thread = threading.Thread(target=music, kwargs={"count" : 1})

    # 启动子线程执行任务
    coding_thread.start()
    music_thread.start()