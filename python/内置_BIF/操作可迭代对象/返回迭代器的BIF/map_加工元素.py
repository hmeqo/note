"""map()  内置_BIF"""


'''
1.加工元素

参数：
    func  函数
    iter1  可迭代对象
创建一个迭代器，使用每个可迭代对象的实参计算函数。当最短的可迭代对象耗尽时停止。
对可迭代对象中每个元素都使用一遍函数加工
返回一个可迭代对象，每次迭代从此对象弹出一个元素
'''

print('1.')
print('——————————————————————————————————————————————————')

a = map(lambda x: x*3, [4, 3, 7, 5])
print('1.', tuple(a))
a = map(lambda x: x.title(), 'abc')
print('2.', tuple(a))
a = map(lambda x: x.swapcase(), ['map', 'English', 'Python'])
print('3.', tuple(a))

print('——————————————————————————————————————————————————')
print('\n')
