"""functools  模块"""
import functools


'''
1.函数工具

导入方式:
    import functools
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.reduce()

对数字元素的序列进行加减乘除等计算
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.', functools.reduce(lambda x, y: x * y, [i for i in range(1, 6)]))

print('——————————————————————————————————————————————————')
print('\n')
