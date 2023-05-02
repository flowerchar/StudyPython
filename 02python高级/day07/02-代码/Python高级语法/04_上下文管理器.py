# 1定义一个File类
class File(object):
    def __init__(self, file_name, file_model):
        self.file_name = file_name
        self.file_model = file_model

# 2实现 __enter__() 和 __exit__()方法
    def __enter__(self):
        print("这是上文")
        self.file = open(self.file_name, self.file_model)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("这是下文")
        self.file.close()

# 3然后使用 with 语句来完成操作文件
with File("1.txt","r") as f:
    file_data = f.read()
    print(file_data)

