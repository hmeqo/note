"""set()  内置_BIF"""


'''
1.将括号里的可迭代对象转换成集合
'''

print('1.')
print('——————————————————————————————————————————————————')

a = '1234.1234'
print('1.', '转换前', a, '类型', type(a), '\n转换后', set(a), '类型', type(set(a)))
a = (10, '哈哈')
print('2.', '转换前', a, '类型', type(a), '\n转换后', set(a), '类型', type(set(a)))

print('——————————————————————————————————————————————————')
print('\n')
