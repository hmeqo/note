"""filter()  内置_BIF"""


'''
1.过滤元素

参数：
    function or None  函数
    iterable  可迭代对象
只保留函数返回值为 True 的值
'''
print('1.')
print('——————————————————————————————————————————————————')

a = filter(lambda x: x % 3, [4, 3, 7, 5])
print('1.', tuple(a))
a = filter(lambda x: x.isdecimal(), '2a3b中文c')
print('2.', tuple(a))

print('——————————————————————————————————————————————————')
print('\n')
