def binary_search(alist, item):
    """二分查找"""

    # 设置起始位置 获取中间值
    start = 0
    end = len(alist) - 1

    while start <= end:
        # 获取中间值
        mid = (start + end)//2

        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            end = mid - 1
        elif item > alist[mid]:
            start = mid + 1

    # 没有找到想要找的数字
    return False

if __name__ == '__main__':
    alist = [1,2,3,4,5]
    print(binary_search(alist, 1))
    print(binary_search(alist, 100))