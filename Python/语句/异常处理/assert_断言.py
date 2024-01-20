"""assert  断言"""


'''
1.当条件不满足时抛出异常

格式:
    assert condition [, except]
'''

print('1.')
print('——————————————————————————————————————————————————')

try:
    assert 1 == 2, '一不等于二'
except AssertionError as e:
    print('1.', e)

print('——————————————————————————————————————————————————')
print('\n')
