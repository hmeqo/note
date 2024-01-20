"""dict  字典"""


'''
1.{1: 2}  字典，可变序列

字典由一对对键-值对组成，其中键是不可重复且不可变的，一个字典中不能出现相同的键，值是可重复的
通过键获取字典中键的值
也可以通过键修改值和添加键值对
可将字典中键的值理解为键的属性，这个属性默认是被隐藏的，需要通过键得到它
'''

print('1.')
print('——————————————————————————————————————————————————')

dict1 = {'name': '张三', 'age': '18'}
print('1.', dict1)
print('2.', dict1['name'])
print('3.', dict1['age'])
print('4.', '值默认被隐藏，看似会拿出键值对其实只拿出键')
for i in dict1:
    print(i)
print('5.', '再通过键拿出值，就是键值对了')
for i in dict1:
    print(i, dict1[i])
print('6.', dict1, '修改值')
dict1['name'] = '李四'
print('修改后', dict1)
print('7.', dict1, '添加键值对')
dict1['job'] = '推销员'
print('添加后', dict1)

print('——————————————————————————————————————————————————')
print('\n')


'''
2.get() setdefault() keys() values() items()

获取字典元素
get()  传入键，如果字典中有，返回值，没有，返回默认值，默认值默认为 None
setdefault()  返回传入的键对应的值，如果没有这个键，则添加键和默认值，再返回值
keys()  返回字典中所有的键，以列表返回一个可迭代对象，不是列表类型
values()  返回字典中所有的值，以列表返回一个可迭代对象，不是列表类型
items()  返回字典中所有的键值对，以列表中嵌套的一个个元祖返回一个可迭代对象，不是列表类型
'''

print('2.')
print('——————————————————————————————————————————————————')

dict1 = {'name': '张三', 'age': '18'}
print('1.', dict1.get('name'))
print('2.', dict1.get('键', '默认值'))
print('3.', dict1.setdefault('name'))
print('4.', dict1.setdefault('键', '默认值'))
print('5.', dict1.keys())
print('6.', dict1.values())
print('7.', dict1.items())
print('8.', type(dict1.items()))
print('9.', list(dict1.items()))

print('——————————————————————————————————————————————————')
print('\n')


'''
3.update()

添加修改键值对
update()  以一个可迭代对象更新字典
'''

print('3.')
print('——————————————————————————————————————————————————')

dict1 = {'name': '张三', 'age': '18'}
print('1.', '更新前', dict1)
dict1.update((('更新字典', '值'), ('name', '李四')))
print('更新后', dict1)

print('——————————————————————————————————————————————————')
print('\n')


'''
4.pop() popitem() clear() del

删除键值对
pop()  弹出指定的键和对应的值，返回对应的值
popitem()  弹出末尾的一对键值对，以元组的形式返回键值对
clear()  清空字典
del  语句，指定删除键值对或删除整个字典
'''

print('4.')
print('——————————————————————————————————————————————————')

dict1 = {'name': '张三', 'age': '18', '多余': '请删掉我'}
print('1.', dict1.pop('多余'))
print(dict1)
dict1 = {'name': '张三', 'age': '18', '多余': '请删掉我'}
print('2.', dict1.popitem())
print(dict1)
dict1 = {'name': '张三', 'age': '18', '多余': '请删掉我'}
print('3.', dict1)
dict1.clear()
print(dict1)
dict1 = {'name': '张三', 'age': '18', '多余': '请删掉我'}
print('4.', dict1)
del dict1['多余']
print(dict1)
dict1 = {'name': '张三', 'age': '18', '多余': '请删掉我'}
print('5.', dict1)
del dict1
print('字典已被删除')

print('——————————————————————————————————————————————————')
print('\n')


'''
5.copy()

拷贝字典
copy()  拷贝一份字典，浅拷贝

使用其他方式也可以拷贝字典，不额外设计的情况下，这些都属于浅拷贝
（深拷贝详见模块 copy，这里不做介绍）
'''

print('5.')
print('——————————————————————————————————————————————————')

dict1 = {'name': '张三', 'age': '18', '多余': '请删掉我'}
dict2 = dict1.copy()
print('1.', dict1.pop('多余'))
print(dict1)
print(dict2)
dict1 = {'name': '张三', 'age': '18', '多余': '请删掉我'}
dict2 = {key: value for key, value in list(dict1.items())}
print('2.', dict1.pop('多余'))
print(dict1)
print(dict2)
dict1 = {'name': '张三', 'age': '18', '多余': '请删掉我'}
dict2 = dict(tuple(dict1.items()))
print('3.', dict1.pop('多余'))
print(dict1)
print(dict2)

print('——————————————————————————————————————————————————')
print('\n')


'''
6.fromkeys()

创建字典
fromkeys()  创建一个新的字典，其中键来自一个可迭代序列，值来自一个固定值

fromkeys() 是一个静态方法，可以不通过已创建的对象直接用类使用它
'''

print('6.')
print('——————————————————————————————————————————————————')

dict1 = {'name': '张三', 'age': '18', '多余': '请删掉我'}
print('1.', dict1.fromkeys('abc', '123'))
print(dict1)
print('2.', dict.fromkeys('abc'))

print('——————————————————————————————————————————————————')
print('\n')
