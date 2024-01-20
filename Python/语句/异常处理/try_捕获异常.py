"""try  捕获异常"""


'''
1.捕获异常

格式:
    try:
        ...
    except[ ...]:
        ...
    else:
        ...
    finally:
        ...
    当出现异常时执行 except 包含的代码块并捕获异常
    当没有出现异常时执行 else 包含的代码块
    无论是否出现异常都将执行 finally 包含的代码块
    同时存在 else 和 finally 时，finally 在下方
'''

print('1.')
print('——————————————————————————————————————————————————')

try:
    int('abc')
except ValueError as e:
    print('1.', e)
else:
    print('1.', '无异常')
finally:
    print('Finally')

try:
    int('1')
except ValueError as e:
    print('2.', e)
else:
    print('2.', '无异常')

print('——————————————————————————————————————————————————')
print('\n')
