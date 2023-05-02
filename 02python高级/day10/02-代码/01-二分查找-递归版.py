def binary_search(alist, item):
    """二分查找"""

    # 数列的长度
    n = len(alist)
    # 递归的结束条件
    if n == 0:
        return False

    # 中间值
    mid = n//2

    if item == alist[mid]:
        return True
    elif item < alist[mid]:
        return binary_search(alist[0:mid], item)
    elif item > alist[mid]:
        return binary_search(alist[mid+1:], item)

if __name__ == '__main__':
    alist = [1,2,3,4,5]
    print(binary_search(alist, 1))
    print(binary_search(alist, 100))

