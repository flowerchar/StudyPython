# 外部函数
def config_name(name):
    # 内部函数
    def say_info(info):
        print(name + ":", info)

    return say_info

tom = config_name("tom")
tom("你好")
tom("你在么")

jerry = config_name("jerry")
jerry("你好")
jerry("我在呢")

