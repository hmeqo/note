"""int()  内置_BIF"""


'''
1.将括号里的对象转换成整数类型

需要注意要转换的对象只能是数字，不能是字符或其他对象，例如：哈哈
浮点类型转换整数类型时，会去掉小数
'''

print('1.')
print('——————————————————————————————————————————————————')

a = '1234'
print('1.', '转换前', a, '类型', type(a), '\n转换后', int(a), '类型', type(int(a)))
a = 10.9
print('2.', '转换前', a, '类型', type(a), '\n转换后', int(a), '类型', type(int(a)))

print('——————————————————————————————————————————————————')
print('\n')
