"""float()  内置_BIF"""


'''
1.将括号里的对象转换成浮点数类型

需要注意要转换的对象只能是数字不能是字符或者其他对象，例如：哈哈
整数转成浮点数时，会在末尾添上 .0
'''

print('1.')
print('——————————————————————————————————————————————————')

a = '1234.1234'
print('1.', '转换前', a, '类型', type(a), '\n转换后', float(a), '类型', type(float(a)))
a = 10
print('2.', '转换前', a, '类型', type(a), '\n转换后', float(a), '类型', type(float(a)))
a = '1E6'
print('3.', '转换前', a, '类型', type(a), '\n转换后', float(a), '类型', type(float(a)))

print('——————————————————————————————————————————————————')
print('\n')
