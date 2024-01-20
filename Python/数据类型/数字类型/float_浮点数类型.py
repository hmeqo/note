"""float  浮点数类型"""
import decimal


'''
1.浮点数

浮点数相加时计算有误差，可以导入模块 decimal 使用 Decimal 解决
对于极端数字，Python 使用科学计数法 e 表示
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.', 1.3)
print('2.', 50.800901)
print('3.', -10.5555)
print('4.', 0.1 + 0.2)
print('5.', decimal.Decimal('0.1') + decimal.Decimal('0.2'))
print('6.', 0.00005)

print('——————————————————————————————————————————————————')
print('\n')
