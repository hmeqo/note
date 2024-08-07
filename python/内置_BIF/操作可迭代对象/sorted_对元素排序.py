"""sorted()  内置_BIF"""


'''
1.返回排序后的值

可选参数：
    reverse=  排序顺序
    key=  指定规则排序
对可迭代对象排序后以列表返回

注意：传入的参数中的元素不能是不同类型
'''
print('1.')
print('——————————————————————————————————————————————————')

a = (2, 1, 3)
print('1.', sorted(a))
print('转换后并没有改变原序列', a)
a = {2: 3, 1: 4, 3: 5}
print('2.', sorted(a))
print('3.', sorted(a, reverse=True))
a = ('222', '11', '3')
print('4.', sorted(a, key=lambda x: len(x)))
a = ((1, 2), (2, 1), (3, 0))
print('5.', sorted(a, key=lambda x: x[1]))

print('——————————————————————————————————————————————————')
print('\n')
