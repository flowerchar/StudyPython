def select_sort(alist):
    """选择排序"""

    # 列表的长度
    n = len(alist)

    # 控制比较轮数
    for j in range(0,n-1):
        # 假定的最小值的下标
        min_index = j

        # 控制比较次数
        for i in range(j+1, n):
            # 进行比较获得最小值
            if alist[i] < alist[min_index]:
                min_index = i

        # 如果假定的最小值下标发生变化了,那么我们就进行交换
        if min_index != j:
            alist[j],alist[min_index] = alist[min_index],alist[j]

if __name__ == '__main__':
    alist = [1,3,4,10,0,1000,88]
    select_sort(alist)
    print(alist)