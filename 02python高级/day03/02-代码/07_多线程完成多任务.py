import time
import threading


# 编写代码
def coding():
    for i in range(3):
        print("coding...")
        time.sleep(0.2)


# 听音乐
def music():
    for i in range(3):
        print("music...")
        time.sleep(0.2)


if __name__ == '__main__':
    # coding()
    # music()
    # 创建子线程
    coding_thread = threading.Thread(target=coding)
    music_thread = threading.Thread(target=music)

    # 启动子线程执行任务
    coding_thread.start()
    music_thread.start()