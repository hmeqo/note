"""tuple  元组"""


'''
1.(1, 2)  元组，不可变序列

和列表一样支持下标索引和切片，但不能增删改元素
虽然不能改变元祖中的元素，但如果元组中的元素指向的是一个可变序列，如列表，是可以修改列表中的元素的
可以对引用元组的对象重新赋值一个新的元组以达到修改元组元素的目的
只有一个元素的元组需要一个逗号
括号是可以省略的，但写上括号会比较直观，易读
'''

print('1.')
print('——————————————————————————————————————————————————')

tuple1 = (1, 2, 3, 4, 5, '元组')
print('1.', tuple1)
print('2.', tuple1[0])
print('3.', tuple1[-1])
print('4.', tuple1[2:])
tuple2 = ('拼接',)
print('5.', tuple1 + tuple2)
print('6.', tuple1 + tuple2 * 3)
tuple1 = ([1, 2, 3], [4, 5, 6])
print('7.', '原元组', tuple1)
tuple1[0][1] = -2
print('新元组', tuple1)

print('——————————————————————————————————————————————————')
print('\n')


'''
2.count() index()

元组元素的查找
count()  某个对象出现的次数
index()  某个对象的索引，只返回第一次查找到的索引
（在列表的介绍中也写了相关用法，想了解更多可以移步至列表的相关文件）
'''

print('2.')
print('——————————————————————————————————————————————————')

tuple1 = (1, 2, 3, 4, 1, 3, 1)
print('1.', tuple1.count(1))
print('2.', tuple1.index(1))

print('——————————————————————————————————————————————————')
print('\n')


'''
3.(for in)

生成器
使用小括号作为列表推导式的外壳得到的是一个生成器
在括号中可以省略括号
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.', (i for i in range(10)))
for i in (i for i in range(10)):
    print(i, end=' ')
print()
print('2.', sum(i for i in range(10)))

print('——————————————————————————————————————————————————')
print('\n')
