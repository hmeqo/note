"""bool  布尔类型"""


'''
1.布尔值

任何对象都有布尔值（调用对象的 __bool__ 方法）
有就是 True
没有就是 False。空的字符串，列表，字典，False 本身，None，等……，都是False
布尔值也能用来表示数，True 表示 1，False 表示 0
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.', bool(1))
print('2.', bool(0))
print('3.', bool(''))
print('4.', bool([]))
print('5.', bool({1: 1}))
print('6.', bool(None))
print('7.', bool(True))
print('8.', bool(False))
print('9.', 'True 和 Fale 表示的数', int(True), int(False),
      '\nTrue 加上 10 和 10 加上 False', 10 + True, 10 + False)

print('——————————————————————————————————————————————————')
print('\n')
