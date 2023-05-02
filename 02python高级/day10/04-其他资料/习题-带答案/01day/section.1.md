# 每日必会题

1. 阐述二分查找的原理

   > 首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，如果两者相等，则查找成功；
   >
   > 否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。
   >
   > 重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。

2. 递归代码实现二分查找算法

   ```python
   def binary_search(alist, item):
       if len(alist) == 0:
           return False
       else:
           midpoint = len(alist)//2
           if alist[midpoint]==item:
             return True
           else:
             if item<alist[midpoint]:
               return binary_search(alist[:midpoint],item)
             else:
               return binary_search(alist[midpoint+1:],item)
   
   testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
   print(binary_search(testlist, 3))
   print(binary_search(testlist, 13))
   ```

   

3. 非递归的方式实现二分查找算法

   ```python
   def binary_search(alist, item):
         first = 0
         last = len(alist)-1
         while first<=last:
             midpoint = (first + last)/2
             if alist[midpoint] == item:
                 return True
             elif item < alist[midpoint]:
                 last = midpoint-1
             else:
                 first = midpoint+1
       return False
   testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
   print(binary_search(testlist, 3))
   print(binary_search(testlist, 13))
   ```

4. 请阐述树的特点  

   ```python
   每个节点有零个或多个子节点；
   没有父节点的节点称为根节点；
   每一个非根节点有且只有一个父节点；
   除了根节点外，每个子节点可以分为多个不相交的子树；
   ```

