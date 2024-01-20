"""set  集合"""


'''
1.{1, 2}  集合，可变序列

集合就像没有值的字典，其中的元素也是不可重复且不可变的，元素无序排列
对其中元素进行哈希值计算存储位置和排列顺序
集合和字典一样使用外括号，空字典是 {}，所以空集合用 set() 表示
'''

print('1.')
print('——————————————————————————————————————————————————')

set1 = {1, 2, 3, 4, 5, '集合'}
print('1.', set1)

print('——————————————————————————————————————————————————')
print('\n')


'''
2.add() update()

添加元素
add()  添加一个元素
update()  更新一个可迭代对象中的元素
'''

print('2.')
print('——————————————————————————————————————————————————')

set1 = {1, 2, 3, 4, 5, '集合'}
print('1.', set1)
set1.add('set')
print(set1)
set1 = {1, 2, 3, 4, 5, '集合'}
print('2.', set1)
set1.update('set')
print(set1)

print('——————————————————————————————————————————————————')
print('\n')


'''
3.pop() discard() remove() clear() del

删除元素
pop()  弹出开头的一个元素
discard()  指定删除一个元素，如果元素不存在，则什么都不做
remove()  指定删除一个元素
clear()  清空集合
del  语句，只能用来删除整个集合
'''

print('3.')
print('——————————————————————————————————————————————————')

set1 = {1, 2, 3, 4, 5, '集合'}
print('1.', set1.pop())
print(set1)
set1 = {1, 2, 3, 4, 5, '集合'}
set1.discard(3)
print('2.', set1)
set1 = {1, 2, 3, 4, 5, '集合'}
set1.discard('0')
print('3.', set1)
set1 = {1, 2, 3, 4, 5, '集合'}
set1.remove(3)
print('4.', set1)
set1 = {1, 2, 3, 4, 5, '集合'}
set1.clear()
print('5.', set1)
set1 = {1, 2, 3, 4, 5, '集合'}
print('6.', set1)
del set1
print('已删除集合')

print('——————————————————————————————————————————————————')
print('\n')


'''
4.intersection() intersection_update() union()
difference() difference_update()
symmetric_difference() symmetric_difference_update()

操作集合
intersection()  返回自身和另一个集合交集的部分作为一个新的集合
intersection_update()  用自身与另一个集合的交集更新自身
union()  返回自身和另一个集合合并后的集合
difference()  返回自身和另一个集合差集的部分作为一个新的集合
difference_update()  用自身和另一个集合的差集更新自身
symmetric_difference()  返回自身和另一个集合差集的部分再合并作为一个新的集合
symmetric_difference_update()  用自身和另一个集合差集在合并更新自身
'''

print('4.')
print('——————————————————————————————————————————————————')

set1 = {1, 2, 3, 4, 5, '集合'}
set2 = {1, 2, 5, '233', 'abc'}
print('1.', set1.intersection(set2))
set1.intersection_update(set2)
print('2.', set1)
set1 = {1, 2, 3, 4, 5, '集合'}
print('3.', set1.union(set2))
print('4.', set1.difference(set2))
set1.difference_update(set2)
print('5.', set1)
set1 = {1, 2, 3, 4, 5, '集合'}
print('6.', set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print('7.', set1)

print('——————————————————————————————————————————————————')
print('\n')


'''
5.issuperset() issubset() isdisjoint()

判断集合
issuperset()  自身是否是另一个集合的超集
issubset()  自身是否是另一个集合的子集
isdisjoint()  自身是否与另一个集合没有交集

两个集合元素相同时，互为超集和子集
'''

print('5.')
print('——————————————————————————————————————————————————')

set1 = {1, 2, 3, 4, 5, '集合'}
set2 = {1, 2, 3, 4, 5}
print('1.', set1.issuperset(set2))
print('2.', set1.issubset(set2))
print('3.', set1.isdisjoint(set2))
set2 = {1, 2, 3, 4, '5'}
print('4.', set1.issuperset(set2))
print('5.', set1.issubset(set2))
print('6.', set1.isdisjoint(set2))

print('——————————————————————————————————————————————————')
print('\n')
