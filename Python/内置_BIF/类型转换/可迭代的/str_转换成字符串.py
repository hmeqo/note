"""str()  内置_BIF"""


'''
1.将括号里的对象转换成字符串

似乎任何对象都能转换成字符串
'''

print('1.')
print('——————————————————————————————————————————————————')

a = 1234.1234
print('1.', '转换前', a, '类型', type(a), '\n转换后', str(a), '类型', type(str(a)))
a = [10, '哈哈']
print('2.', '转换前', a, '类型', type(a), '\n转换后', str(a), '类型', type(str(a)))

print('——————————————————————————————————————————————————')
print('\n')
