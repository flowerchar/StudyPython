# Python中的顺序表

Python中的list和tuple两种类型采用了顺序表的实现技术，具有前面讨论的顺序表的所有性质。

tuple是不可变类型，即不变的顺序表，因此不支持改变其内部状态的任何操作，而其他方面，则与list的性质类似。

### list的基本实现技术

Python标准类型list就是一种元素个数可变的线性表，可以加入和删除元素，并在各种操作中维持已有元素的顺序（即保序），而且还具有以下行为特征：

+ 基于下标（位置）的高效元素访问和更新，时间复杂度应该是O(1)；

    为满足该特征，应该采用顺序表技术，表中元素保存在一块连续的存储区中。

+ 允许任意加入元素，而且在不断加入元素的过程中，表对象的标识（函数id得到的值）不变。

    为满足该特征，就必须能更换元素存储区，并且为保证更换存储区时list对象的标识id不变，只能采用分离式实现技术。

在Python的官方实现中，**list就是一种采用分离式技术实现的动态顺序表**。这就是为什么用list.append(x) （或 list.insert(len(list), x)，即尾部插入）比在指定位置插入元素效率高的原因。

> 《数据结构与算法 Python语言描述》 裘宗燕 著

> ~~在Python的官方实现中，list实现采用了如下的策略：在建立空表（或者很小的表）时，系统分配一块能容纳8个元素的存储区；在执行插入操作（insert或append）时，如果元素存储区满就换一块4倍大的存储区。但如果此时的表已经很大（目前的阀值为50000），则改变策略，采用加一倍的方法。引入这种改变策略的方式，是为了避免出现过多空闲的存储位置。~~

在Python的官方实现中，list实现采用了如下的策略：
```c
    /* This over-allocates proportional to the list size, making room
     * for additional growth.  The over-allocation is mild, but is
     * enough to give linear-time amortized behavior over a long
     * sequence of appends() in the presence of a poorly-performing
     * system realloc().
     * The growth pattern is:  0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...
     */
    new_allocated = (newsize >> 3) + (newsize < 9 ? 3 : 6);

    /* check for integer overflow */
    if (new_allocated > PY_SIZE_MAX - newsize) {
        PyErr_NoMemory();
        return -1;
    } else {
        new_allocated += newsize;
    }
```
