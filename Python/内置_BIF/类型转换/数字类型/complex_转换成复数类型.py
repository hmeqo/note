"""complex()  内置_BIF"""


'''
1.将括号里的两个数转换成复数类型

两个参数必须是数字，或者传入一个字符串
'''

print('1.')
print('——————————————————————————————————————————————————')

a = 10
b = 20.5
print('1.', '转换前', a, b, '类型', type(a), type(b), '\n转换后', complex(a, b), '类型', type(complex(a, b)))
a = '10+20.5j'
print('2.', '转换前', a, '类型', type(a), '\n转换后', complex(a), '类型', type(complex(a)))

print('——————————————————————————————————————————————————')
print('\n')
