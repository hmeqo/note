"""continue  退出循环语句"""


'''
1.退出本轮循环
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.', end='')
i = 0
while i < 10:
    i += 1
    if not i % 2:
        print('偶数', i)
        continue
    print('奇数', i)

print('——————————————————————————————————————————————————')
print('\n')
