"""for  循环语句"""


r'''
1.循环语句

循环通过 __next__ 方法获取可迭代对象的元素
直到抛出异常 StopIteration 结束循环
（使用 break 语句也可以退出）
比较容易理解的说法:
    逐一获取序列中的每个元素，直到获取完所有的元素，循环正常结束

for 循环中经常使用的内置函数:
    range()  产生一个整数序列
    （详见: 内置_BIF\操作可迭代对象\返回类对象的BIF\range_产生整数序列.py）

在循环后面加上 else 语句，表示当 for 循环正常结束时，执行 else 包含的代码块
当遇到 break 退出时，不执行 else
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.', end='')
print('循环开始')
for i in '循环语句 for':
    print(i)
print('循环结束')
print('2.', end='')
print('循环开始')
print('0到10的整数，不包含10')
for i in range(10):
    print('整数', i)
else:
    print('else 被执行了')
print('循环结束')
print('3.', end='')
print('循环开始')
for i in '循环语句 for':
    print(i)
    break
else:
    print('else 被执行了')
print('循环结束')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.推导式

能创建列表等可变序列，列表，字典，集合
格式：[i for i in range(10)] {key: value for key, value in an1}
'''

print('1.')
print('——————————————————————————————————————————————————')

lst = [i for i in range(10)]
print('1.', lst)
lst = [[0] * 3 for i in range(3)]
print('2.', lst)
an1 = (('键', '值'), ('我是谁', '我是字典'))
dict1 = {key: value for key, value in an1}
print('3.', dict1)
set1 = {i for i in range(10)}
print('4.', set1)

print('——————————————————————————————————————————————————')
print('\n')
