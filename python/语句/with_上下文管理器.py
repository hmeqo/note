"""with  上下文管理器"""


'''
1.上下文管理器

调用对象的 __enter__ 和 __exit__ 方法
开始时调用 __enter__
结束时调用 __exit__，无论是否出现异常都会执行
'''

print('1.')
print('——————————————————————————————————————————————————')


class A:

    def __init__(self, **kwargs):

        pass

    def __enter__(self):

        print('__enter__ 方法被执行了！')
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print('__eixt__ 方法被执行了！')
        return None


print('1.')
with A() as a:
    print('...', a)

print('——————————————————————————————————————————————————')
print('\n')
