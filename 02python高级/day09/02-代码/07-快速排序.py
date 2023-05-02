def quick_sort(alist, start, end):
    """快速排序"""

    # 递归的结束条件
    if start >= end:
        return

    # 界限值
    mid = alist[start]
    # 左右游标
    left = start
    right = end


    while left < right:
        # 从右边开始找寻小于mid的值 归类到左边
        while alist[right] >= mid and left < right:
            right -= 1
        alist[left] = alist[right]
        # 从左边开始找寻大于mid的值 归类到右边
        while alist[left] < mid and left < right:
            left += 1
        alist[right] = alist[left]

    # 循环一旦结束了 证明找到了mid应该在的位置
    alist[left] = mid

    # 递归操作
    quick_sort(alist, start, left-1)
    quick_sort(alist, right+1, end)

if __name__ == '__main__':
    alist = [1,2,100,50,1000,0,1,1]
    quick_sort(alist, 0, len(alist)-1)
    print(alist)




