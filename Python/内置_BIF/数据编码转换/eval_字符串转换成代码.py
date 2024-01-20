"""eval()  内置_BIF"""


'''
1.去掉字符串引号转换成代码并执行

参数必须是字符串
一次只能转换一串代码
'''
print('1.')
print('——————————————————————————————————————————————————')

a = "['哈哈']"
print('1.', '转换前', a, type(a))
a = eval(a)
print('转换后', a, type(a))
a = '12357.44'
print('2.', '转换前', a, type(a))
a = eval(a)
print('转换后', a, type(a))
a = """print('我原本不是字符串吗？', [i for i in range(10)])"""
print('3.')
print(eval(a))
print('4.', eval(bin(ord('a'))))

print('——————————————————————————————————————————————————')
print('\n')
