"""open()  内置_BIF"""


'''
1.读写文件

参数:
    file: 填文件名以及它的拓展名
    mode: 文件打开模式
        'r': 以读的模式打开，文件必须存在
        'w': 以写的模式打开，文件不纯在则创建，存在则覆盖
        'x': 创建新的文件并以写的模式打开，文件必须不存在
        'a': 以末尾追加的模式打开，文件不纯在则创建
        可选后缀（可多选）:
            '+': 可读可写
            'b': 以二进制模式打开
            't': 以文本模式打开（默认）
            'U': 通用换行符（文本模式生效）
    encoding: 文件格式，例如 encoding='UTF-8'，二进制模式不可用

close()  关闭文件
非 with 打开的文件没用时一定要关闭文件，可以使用 close() 关闭

可以和 with 语句配合使用
可以被 iter
'''

print('1.')
print('——————————————————————————————————————————————————')

file = open('open_读写文件.py', 'r', encoding='UTF-8')
print('1.', file.readline())
file.close()

with open('open_读写文件.py', 'r', encoding='UTF-8') as file:
    print('2.', file.readline())

print('——————————————————————————————————————————————————')
print('\n')


'''
2.read() readline() readlines()

以读的模式打开文件后的可选方法
read()  按字符读取，一个可选参数，参数填字符，返回字符串
readline()  按单行读取，一个可选参数，参数填字节，返回字符串
readlines()  按多行读取，参数同上，返回列表，元素是字符串
'''

print('2.')
print('——————————————————————————————————————————————————')

with open('open_读写文件.py', 'r', encoding='UTF-8') as file:
    print('1.', file.read(100))
    file.seek(0, 0)
    print('2.', file.readline(100))
    file.seek(0, 0)
    print('3.', file.readlines(100))

print('——————————————————————————————————————————————————')
print('\n')


'''
3.write() writelines()

以写的模式打开文件后的可选方法
write()  在当前指针位置写入字符串参数，覆盖掉原来的内容，相同字节长度的部分
writelines()  在当前指针位置向文件写入一个返回字符串的可迭代对象
'''

print('3.')
print('——————————————————————————————————————————————————')

with open('open_读写文件.txt', 'w', encoding='UTF-8') as file:
    file.write('hello world')
    file.seek(0, 0)
    file.write('NiHao')

print('——————————————————————————————————————————————————')
print('\n')


'''
4.tell() seek()

文件指针
tell()  返回当前指针位置
seek()  设置指针
    参数:
        offset: 移动几个字符
        whence: 填 0 表示从开头开始，1 从当前位置起算，2 从末尾
'''

print('4.')
print('——————————————————————————————————————————————————')

with open('open_读写文件.txt', 'w', encoding='UTF-8') as file:
    print('1.', file.tell())
    file.seek(5)
    print('2.', file.tell())

print('——————————————————————————————————————————————————')
print('\n')
