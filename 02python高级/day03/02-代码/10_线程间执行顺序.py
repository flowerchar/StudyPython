import threading
import time


# 获取线程信息函数
def get_info():
    time.sleep(0.5)
    # 获取线程信息
    current_thread = threading.current_thread()
    print(current_thread)


if __name__ == '__main__':
    # 创建子线程
    for i in range(10):
        sub_thread = threading.Thread(target=get_info)
        sub_thread.start()