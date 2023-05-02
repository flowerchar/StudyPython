# 每日练习题

1. 阐述选择排序的思想

   > 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

2. 代码实现选择排序算法

   ```python
   def selection_sort(alist):
       n = len(alist)
       # 需要进行n-1次选择操作
       for i in range(n-1):
           # 记录最小位置
           min_index = i
           # 从i+1位置到末尾选择出最小数据
           for j in range(i+1, n):
               if alist[j] < alist[min_index]:
                   min_index = j
           # 如果选择出的数据不在正确位置，进行交换
           if min_index != i:
               alist[i], alist[min_index] = alist[min_index], alist[i]
   
   alist = [54,226,93,17,77,31,44,55,20]
   selection_sort(alist)
   print(alist)
   ```

   

3. 阐述插入排序算法的思想

   > 通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入

4. 代码实现排序算法

   ```python
   def insert_sort(alist):
       # 从第二个位置，即下标为1的元素开始向前插入
       for i in range(1, len(alist)):
           # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
           for j in range(i, 0, -1):
               if alist[j] < alist[j-1]:
                   alist[j], alist[j-1] = alist[j-1], alist[j]
   
   alist = [54,26,93,17,77,31,44,55,20]
   insert_sort(alist)
   print(alist)
   ```

   

5. 阐述快速排序算法的思想

   > 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

6. 代码实现快速排序算法

   ```python
   
   def quick_sort(alist, start, end):
       """快速排序"""
   
       # 递归的退出条件
       if start >= end:
           return
   
       # 设定起始元素为要寻找位置的基准元素
       mid = alist[start]
   
       # low为序列左边的由左向右移动的游标
       low = start
   
       # high为序列右边的由右向左移动的游标
       high = end
   
       while low < high:
           # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
           while low < high and alist[high] >= mid:
               high -= 1
           # 将high指向的元素放到low的位置上
           alist[low] = alist[high]
   
           # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
           while low < high and alist[low] < mid:
               low += 1
           # 将low指向的元素放到high的位置上
           alist[high] = alist[low]
   
       # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
       # 将基准元素放到该位置
       alist[low] = mid
   
       # 对基准元素左边的子序列进行快速排序
       quick_sort(alist, start, low-1)
   
       # 对基准元素右边的子序列进行快速排序
       quick_sort(alist, low+1, end)
 
   alist = [54,26,93,17,77,31,44,55,20]
   quick_sort(alist,0,len(alist)-1)
   print(alist)
   ```

   