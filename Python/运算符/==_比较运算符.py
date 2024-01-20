"""== != <= >= < > is is not  比较运算符"""


'''
1.比较运算符有 == != <= >= < > is is not

==  判断左边是否等于右边
!=  判断左边是否不等于右边
<=  判断左边是否小于等于右边
>=  判断左边是否大于等于右边
<  判断左边是否小于右边
>  判断左边是否大于右边
is  判断两个对象的 id 是否相等
is not  判断两个对象的 id 是否不相等
以上，成立返回值 True，不成立返回值 False

因驻留机制，部分（列表不是，其他还不清楚）元素相同的变量共用同一个id对象，以节省内存空间
'''

print('1.')
print('——————————————————————————————————————————————————')

a = 10
b = 20
c = 10
print('1.', 'a等于b吗', a == b, 'a等于c吗', a == c)
print('2.', 'a不等于b吗', a != b, 'a不等于c吗', a != c)
print('3.', 'a小于等于b吗', a <= b, 'a小于等于c吗', a <= c)
print('4.', 'a大于等于b吗', a >= b, 'a大于等于c吗', a >= c)
print('5.', 'a小于b吗', a < b, 'a小于c吗', a < c)
print('6.', 'a大于b吗', a > b, 'a大于c吗', a > c)
print('7.', 'a是b吗', a is b, 'a是c吗', a is c)
print('8.', 'a不是b吗', a is not b, 'a不是c吗', a is not c)
lst = [10]
t = [10]
print('9.', 'lst是t吗', lst is t , 'lst不是t吗', lst is not t)

print('——————————————————————————————————————————————————')
print('\n')
