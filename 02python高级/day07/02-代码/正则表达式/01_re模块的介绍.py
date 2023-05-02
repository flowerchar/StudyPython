# 1 导入re模块 import re
import re

# 2 match匹配数据
#      match（正则表达式,要匹配的字符串）
#      result = re.match(正则表达式,要匹配的字符串)
result = re.match("itc", "flower")

# 3 group提取数据
#      result.group()
info = result.group()
print(info)
