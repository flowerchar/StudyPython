# -*- coding: utf-8 -*-
# @Author  : Chinesejun
# @Email   : flower@163.com
# @File    : 13-队列的基本操作demo.py
# @Software: PyCharm

import multiprocessing

if __name__ == '__main__':
    queue = multiprocessing.Queue(5)

    queue.put(1)
    queue.put(2)
    queue.put(3)
    # print(queue.full())
    queue.put(4)
    queue.put(5)

    # 当存入的数据量大于规定的数据量时，此时处于阻塞状态，只有当数据被取出后，有空间之后
    # 才能继续放入

    # queue.put(6)
    # 当队列数据量为满时会直接报错
    # queue.put_nowait(6)

    # 取出数据
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.empty())
    # print(queue.get())
    # print(queue.get())
    # print(queue.get_nowait())










