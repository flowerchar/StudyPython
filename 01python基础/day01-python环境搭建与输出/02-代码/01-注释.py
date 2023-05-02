# 单行：输出hello world
print('hello world')

print('hello Python')  # 简单注释内容

# 单行注释

"""
第一行注释
第二行注释
第三行注释
"""

'''
注释1
注释2
注释3
'''
import re
def formatNum(num):
    pattern=r'(\d+)(\d{4})((,\d{4})*)'
    while True:
        num,count=re.subn(pattern,r'\1,\2\3',num)
        if count==0:
            break
    return num

# dictionary = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
# def hex_char_decode(number:str='0x5abc')->int:
#     total = 0
#     length = len(number)-2
#     number_lower = number.lower()
#     for i, j in enumerate(number_lower[2:]):
#         if j in [str(k) for k in range(0,10)]:
#             total += int(j)*(16**(length-i-1))
#         else:
#             total += (16**(length-i-1))*dictionary[j]
#     return total
# print(hex_char_decode())
# def binary_string_decode(number:str='101101010111100')->int:
#     length = len(number)
#     total = 0
#     for i, j in enumerate(number):
#         total += int(j)*(2**(length-i-1))
#     return total
# print(binary_string_decode())

# def binary_to_hex(digit:str='101101010111100')->int:
#     numList = formatNum(digit).split(',')
#     total = 0
#     print(numList)
#     length = len(numList)
#     for i, j in enumerate(numList):
#         for in_i, k in enumerate(j):
#             length_j = len(j)
#             total+=int(k)*2**(((length_j-in_i-1))+(length-i-1)*4)
#         print(i, j)
# binary_to_hex()
dictionary = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
def hex_char_decode(digit:str="0x5")->int:
    if digit[-1] in [str(i) for i in range(0,10)]:
        return int(digit[-1])
    else:
        return dictionary[digit[-1]]
print(hex_char_decode())

input_str = input('请输入待转二进制数：')

input_list = []
list_cut = []
list_deal = []


def binary_hex()->str:
    for i in input_str:
        input_list.append(i)
    if len(input_list) % 4 == 0:
        pass
    elif len(input_list) % 4 == 1:
        input_list.insert(0, '0')
        input_list.insert(1, '0')
        input_list.insert(2, '0')
    elif len(input_list) % 4 == 2:
        input_list.insert(0, '0')
        input_list.insert(1, '0')
    elif len(input_list) % 4 == 3:
        input_list.insert(0, '0')
    y = 0
    while y < len(input_list):
        list_cut.append(input_list[y: (y + 4)])
        y += 4
    input_list.clear()
    num = 0
    t = 3
    for k in list_cut:
        for p in k:
            num += int(p) * 2 ** t
            t -= 1
        list_deal.append(num)
        num = 0
        t = 3
    list_cut.clear()
    list_str = [str(u) for u in list_deal]
    list_deal.clear()
    for r in list_str:
        if r == '10':
            o = list_str.index('10')
            list_str[o] = 'a'
        elif r == '11':
            o = list_str.index('11')
            list_str[o] = 'b'
        elif r == '12':
            o = list_str.index('12')
            list_str[o] = 'c'
        elif r == '13':
            o = list_str.index('13')
            list_str[o] = 'd'
        elif r == '14':
            o = list_str.index('14')
            list_str[o] = 'e'
        elif r == '15':
            o = list_str.index('15')
            list_str[o] = 'f'
    end_str = ''.join(list_str)
    list_str.clear()
    return '0x'+end_str


print(binary_hex())