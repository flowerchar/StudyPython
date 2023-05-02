import time
import threading


# 工作函数
def work():
    for i in range(10):
        print("work...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程
    # 方式1 参数方式设置守护主线程
    # work_thread = threading.Thread(target=work, daemon=True)
    work_thread = threading.Thread(target=work)
    # 启动线程
    # 方式2
    work_thread.setDaemon(True)
    work_thread.start()

    # 延时一秒
    time.sleep(1)
    print("主线程执行完毕")