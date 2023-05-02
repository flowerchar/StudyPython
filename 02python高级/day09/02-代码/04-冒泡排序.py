def bubble_sort(alist):
    """冒泡排序"""

    # 数列的长度
    n = len(alist)

    # 控制比较轮数
    for j in range(0,n-1):
        # 计数
        count = 0
        # 控制每一轮的比较次数
        for i in range(0,n-j-1):
            # 比较相邻的两个数字 , 不符合要求交换位置
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count+=1
        # 如果遍历一遍发现没有数字交换,退出循环,证明数列是有序的
        if count == 0:
            break

if __name__ == '__main__':
    alist = [5,3,4,7,2]
    bubble_sort(alist)
    print(alist)



def select_sort(alist):

    n = len(alist)
    for j in range(0, n-1):
        min_index = j
        # 假设第一个值为最小值min_index, 从alist第二个值开始和它比较
        for i in range(j+1, n):
            if alist[i] < alist[min_index]:
                # 发现比min_index值小的数字,就记录下他的下标
                min_index = i
        # 如果最小值不是我们假设的值min_index,那么把min_index和最小值交换
        if min_index != j:
            alist[j], alist[min_index] = alist[min_index], alist[j]

if __name__ == '__main__':
    alist = [3,4,1,6,79,10]
    select_sort(alist)
    print(alist)