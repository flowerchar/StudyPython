## 方法一

可以使用QuickTime来合并一系列的ts文件

---

## 方法二

1. | 型号 | 操作 |
   | :---- | :---- |
   |   mac | cat 1.ts 2.ts 3.ts > xxx.mp4|
   |  windows | copy /b 1.ts+2.ts+3.ts xxx.mp4 |
2.操作实例：
```python
import os
# 假设lst是一个含有所有ts文件的列表
lst = ["1.ts","2.ts","3.ts"]
s = " ".join(lst)
# 这句话可以在命令行执行 合并ts
os.system(f"cat {s} > movie.mp4")   


```