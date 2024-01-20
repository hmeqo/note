"""raise  抛出异常"""


'''
1.手动抛出异常

格式:
    raise BaseException('异常')
    raise ValueError('异常')

手抛异常的基类需来自 BaseException 类
'''

print('1.')
print('——————————————————————————————————————————————————')

try:
    raise BaseException('异常')
except BaseException as e:
    print('1.', e)

print('——————————————————————————————————————————————————')
print('\n')
