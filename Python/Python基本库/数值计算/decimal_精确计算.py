"""deciaml  模块"""
import decimal


'''
1.用于精确计算小数的模块

导入方式:
    import decimal
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.Decimal()

保存数字（？）
因 Python 计算浮点数会产生误差，所以使用这个来避免误差
格式：decimal.Decimal('0.1')
注意：填入的是一个字符串
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.', '不使用模块计算 0.1 + 0.2=', 0.1 + 0.2,
      '\n使用该模块计算 0.1 + 0.2=', decimal.Decimal('0.1') + decimal.Decimal('0.2'))

print('——————————————————————————————————————————————————')
print('\n')


'''
3.decimal.getcontext().prec

调整精度
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.', decimal.Decimal('1') / decimal.Decimal('3'))
_ = decimal.getcontext().prec
decimal.getcontext().prec = 100
print(decimal.Decimal('1') / decimal.Decimal('3'))
decimal.getcontext().prec = _

print('——————————————————————————————————————————————————')
print('\n')
