"""sys  模块"""
import sys


'''
1.与系统相关的模块

导入方式:
    import sys
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.path version argv
一些变量

path  Python 的搜索路径，一个列表
version  版本
argv  执行时附带的参数
    例如在 windows cmd 中 C:\> test.py 10 a b
    将 test.py 10 a b 按空格分隔以字符串加入此列表
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.', *sys.path, sep='\n')
print('2.', sys.version)
print('3.', *sys.argv, sep='\n')

print('——————————————————————————————————————————————————')
print('\n')


'''
3.exit()
退出 python 解释器
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.', "sys.exit()")

print('——————————————————————————————————————————————————')
print('\n')


'''
4.stdout
stdout: 标准输入输出
'''

print('4.')
print('——————————————————————————————————————————————————')

sys.stdout.write("1. Print string to terminal.\n")

print('——————————————————————————————————————————————————')
print('\n')
