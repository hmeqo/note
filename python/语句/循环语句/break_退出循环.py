"""break  退出循环语句"""


'''
1.用于打破，退出这一层循环的语句
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.'， end='')
print('循环一开始执行')
while True:
    print('循环一执行中')
    print('循环二开始执行')
    while True:
        print('循环二执行中')
        print('循环二遇到 break 语句')
        break
    print('循环二结束')
    print('循环一遇到 break 语句')
    break
print('循环一结束')

print('——————————————————————————————————————————————————')
print('\n')
