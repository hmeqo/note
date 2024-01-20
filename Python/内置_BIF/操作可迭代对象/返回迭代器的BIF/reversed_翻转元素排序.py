""""reversed()  内置_BIF"""


'''
1.返回翻转排序后的值

对可迭代对象翻转排序后以列表返回
'''
print('1.')
print('——————————————————————————————————————————————————')

a = (2, 1, 3)
print('1.', reversed(a))
print('2.', tuple(reversed(a)))
a = {2: 3, 1: 4, 3: 5}
print('3.', tuple(reversed(a)))
a = (2, 1, '3')
print('4.', tuple(reversed(a)))

print('——————————————————————————————————————————————————')
print('\n')
