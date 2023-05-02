# -*- coding: utf-8 -*-
# @Author  : Chinesejun
# @Email   : flower@163.com
# @File    : 14-进程间队列通信.py
# @Software: PyCharm


import multiprocessing

def write_queue(queue):
    for i in range(10):
        queue.put(i)

def read_queue(queue):
    for i in range(10):
        print("获取的数据：", queue.get())


if __name__ == '__main__':

    queue = multiprocessing.Queue(5)

    sub_process1 = multiprocessing.Process(target=write_queue, args=(queue,))
    sub_process2 = multiprocessing.Process(target=read_queue, args=(queue,))

    sub_process1.start()
    sub_process2.start()

