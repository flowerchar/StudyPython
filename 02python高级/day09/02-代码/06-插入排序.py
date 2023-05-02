def insert_sort(alist):
    """插入排序"""

    # 列表的长度
    n = len(alist)

    # 控制轮数
    for j in range(1, n):
        # [j,j-1,j-2, ..., 1]
        # 找到合适的位置安放我们的无序的数据
        for i in range(j, 0, -1):
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
            else:
                break

if __name__ == '__main__':
    alist = [1,100,99,20,5,1000]
    insert_sort(alist)
    print(alist)