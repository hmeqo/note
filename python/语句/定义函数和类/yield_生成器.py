"""yield  生成器"""


'''
1.在函数或方法中使用，使其变成生成器，可暂停挂起，是特殊的迭代器
格式:
    yield 'return value'
    到 yield 语句暂停，并返回其附带的值
    函数结束时或结束之后调用将报出 StopIteration
'''

print('1.')
print('——————————————————————————————————————————————————')


def a():

    print('one')
    yield '暂停'
    print('tow')
    return None


b = a()
print('1.', type(b))
for i in b:
    print(i)

print('2.')
b = a()
print(next(b))
try:
    print(next(b))
except StopIteration:
    print('StopIteration')


def a():

    print('one')
    return None
    yield '暂停'
    print('tow')


print('3.')
b = a()
try:
    next(b)
except StopIteration:
    print('StopIteration')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.send()

对生成器传值，并执行
相当于调用 next() 时传入值
第一次调用生成器，函数是从头开始，无处接收传入的值，所以必须传入 None
'''

print('2.')
print('——————————————————————————————————————————————————')


def a():

    for i in range(3):
        temp = yield i
        print(temp)
    return None


print('1.')
b = a()
print(b.send(None))
print(b.send('    -3'))
print(b.send('    -2'))
try:
    print(b.send('    -1'))
except StopIteration:
    print('StopIteration')

print('——————————————————————————————————————————————————')
print('\n')


'''
3.()
简化生成器

和列表推导式相似，外围括号换成小括号
调用处只有一个参数时括号可以省略
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.', sum((i for i in range(10))))
print('2.', end=' ')
print(sum(i for i in range(10)))
print('3.', sum(map(lambda x: x ** 2, (i for i in range(10)))))

print('——————————————————————————————————————————————————')
print('\n')
