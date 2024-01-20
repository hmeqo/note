"""打包和解包"""


'''
1.

生成一个元组有时也称为元组的打包
解包就是把元组中的元组分别提取出来，需要注意的是，左侧的变量数量必须和右侧的对象长度相等
此操作同样适用其他序列，如字符串，列表，字典，集合

单纯解包字典，不添加其他代码时，只会拿出键
'''

print('1.')
print('——————————————————————————————————————————————————')

t1 = ('t', 2, 3)
a, b, c = t1
print('1.', t1)
print(a, b, c)
a, b, c = 'str'
print('2.', a, b, c)
a, b, c = ['l', 1, 6]
print('3.', a, b, c)
a, b = {'我是谁？': '我是字典！', '键': '值'}
print('4.', a, b)
a, b = {'我是集合', 123}
print('5.', a, b)

print('——————————————————————————————————————————————————')
print('\n')
