"""@  装饰器"""


'''
1.装饰器
使用类或函数定义装饰器，可以装饰类和函数
'''

print('1.')
print('——————————————————————————————————————————————————')


def decorator(function):

    def wrapper(*args, **kwargs):

        print('-' * 50)
        result = function(*args, **kwargs)
        print('-' * 50)
        return result
    
    return wrapper


class Decorator:

    def __new__(cls, f):

        self = object.__new__(cls)
        self.f = f
        return self.wrapper

    def wrapper(self, *args, **kwargs):

        print('-' * 50)
        result = self.f(*args, **kwargs)
        print('-' * 50)
        return result


print('1.')


@decorator
def func(*args, **kwargs):

    print(args, kwargs)


func(1, 2, 3)
print('2.')


@Decorator
def func(*args, **kwargs):

    print(args, kwargs)


func(1, 2, 3, 4, 5)
print('3.')


@Decorator
class Class:

    def __init__(self, *args, **kwargs):

        print(args, kwargs)


Class(2, 3, 4, 5)

print('——————————————————————————————————————————————————')
print('\n')


'''
2.staticmethod classmethod property
可用于装饰的类

staticmethod  修饰为静态方法，不会自动传入实例
classmethod  修饰为类方法，传入类
property  property()
'''
