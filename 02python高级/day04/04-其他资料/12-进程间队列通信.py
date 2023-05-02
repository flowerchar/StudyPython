# -*- coding: utf-8 -*-
# @Author  : Chinesejun
# @Email   : flower@163.com
# @File    : 12-进程间队列通信.py
# @Software: PyCharm


import multiprocessing
def proc_func(queue):
    # print("子进程....")
    while True:
        print("子进程接受到的数据是:%s" % queue.get())
if __name__ == '__main__':

    queue = multiprocessing.Queue(3)
    pro = multiprocessing.Process(target=proc_func, args=(queue,))
    pro.start()

    while True:
        data = input("输入数据:")
        queue.put(data)
