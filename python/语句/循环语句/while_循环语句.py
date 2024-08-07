"""while  循环语句"""


'''
1.循环语句

当右侧条件判断成立时执行其包含的代码块，执行完毕后继续条件判断
当条件不成立时，退出循环
（使用 break 语句也可以退出）

在循环后面加上 else 语句，表示当 while 循环正常结束时，执行 else 包含的代码块
当遇到 break 退出时，不执行 else
'''

print('1.')
print('——————————————————————————————————————————————————')

counts = 3
print('1.', end='')
while counts:
    print('循环语句while', counts)
    counts -= 1
print('循环结束')
print('2.', end='')
while not counts:
    print('循环语句while', counts)
    counts -= 1
else:
    print('else 语句被执行了')
print('循环结束')
print('3.', end='')
while True:
    print('循环语句while')
    break
else:
    print('else 语句被执行了')
print('循环结束')

print('——————————————————————————————————————————————————')
print('\n')
