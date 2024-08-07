"""copy  模块"""
import copy


'''
1.拷贝

导入方式:
    import copy
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.copy() deepcopy()

copy()  和一般的拷贝一样，都是浅拷贝
deepcopy()  深拷贝
'''

print('2.')
print('——————————————————————————————————————————————————')

lst = [1, 2, 3]
print('1.', '原列表', lst)
lst2 = copy.copy(lst)
print('拷贝的列表', lst2)
lst = [[1], [2], [3]]
print('2.', '原列表', lst)
lst2 = copy.deepcopy(lst)
print('拷贝的列表', lst2)

print('——————————————————————————————————————————————————')
print('\n')
