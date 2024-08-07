"""and or not  逻辑运算符"""


'''
1.逻辑运算符，也叫布尔运算符

and  如果两侧布尔值都为 True
or  左右两侧任意一方的布尔值为 True
not  取相反的布尔值

and or 从左往右判断布尔值，并拿出最后一次判断的对象。如 and 判断对象布尔值
为 False 时，与 and 的属性不符，终止判断并拿出这个值。
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.', '1 < 2 and 3 < 4=', 1 < 2 and 3 < 4)
print('2.', '1 > 2 and 3 < 4=', 1 > 2 and 3 < 4)
print('3.', '1 < 2 and 3 > 4=', 1 < 2 and 3 > 4)
print('4.', '1 > 2 and 3 > 4=', 1 > 2 and 3 > 4)
print('5.', '1 < 2 or 3 < 4=', 1 < 2 or 3 < 4)
print('6.', '1 > 2 or 3 < 4=', 1 > 2 or 3 < 4)
print('7.', '1 < 2 or 3 > 4=', 1 < 2 or 3 > 4)
print('8.', '1 > 2 or 3 > 4=', 1 > 2 or 3 > 4)
print('9.', 'not True=', not True)
print('10.', 'not False=', not False)
print('11.', 1 and 2 and 3)
print('12.', () and {} and [])
print('13.', 'a' or 'b' or 'c')
print('14.', () or {} or [])

print('——————————————————————————————————————————————————')
print('\n')
