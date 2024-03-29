"""= -= +=  赋值运算符"""


'''
1.赋值运算符

+  加，一个数加上一个数，数的开头加上加号表示一个数本身
-  减，一个数减一个数，数的开头加上减号表示一个数的相反数
*  乘，一个数乘以一个数
/  除，一个数除以一个数，计算结果是一个浮点数
//  整除，一个数整除一个数。需要注意是向下取整
%  取余，一个数整除以另一个数的余数。
    公式：被除数减除数 乘以 被除数整除除数的商，x - y * (x // y)
**  幂，一个数的几次幂

加号和乘号能作用于其他数据类型，加号将两个序列拼接，
乘号对于不可变序列，将其复制几遍，对于可变序列，只是对其多次引用，不产生新的序列
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.', 10 + 2)
print('2.', 10 - 2)
print('3.', 10 * 2)
print('4.', 10 / 2)
print('5.', 10 // 3)
print('6.', -10 // 3,
      '\n-3.333... 向下取整 -4')
print('7.', -10 // -3)
print('8.', 10 % 3, 10 - 3*(10//3))
print('9.', -10 % 3, -10 - 3*(-10//3))
print('10.', 10 % -3, 10 - -3*(10//-3))
print('11.', -10 % -3, -10 - -3*(-10//-3))
print('12.', 10 ** 3)

print('——————————————————————————————————————————————————')
print('\n')
