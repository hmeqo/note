"""class  类"""


'''
1.定义一个类

格式:
    class ClassName:

        pass
    
    class ClassName(object):

        pass

    命名使用驼峰法，首字母大写，单词首字母大写，单词间不使用下划线隔开

在类中定义的变量叫类属性
在类中定义的函数叫方法
实例化类对象返回的对象叫这个类对象的实例对象

方法格式:
    一般的方法:
        def method_name(self, *args, **keywords):

            pass
    静态方法:
        @staticmethod
        def staticmethod_name(*args, **keywords):

            pass
    类方法:
        @classmethod
        def classmethod_name(cls, *args, **keywords):

            pass

类对象/未绑定类:
    刚定义好的类就是未绑定类

    和实例的关系类似于子类的父类，未绑定类是父类

实例:
    instance = ClassName()
    调用未绑定类，实例化该类，返回一个新的对象，继承未绑定类的属性方法

    和未绑定类的关系类似于父类的子类，实例就是子类
    初始的实例没有任何属性方法，其属性方法来自未绑定类
    使用实例调用方法时，自动将实例本身传入调用的方法的第一个参数

继承:
    在定义类旁边的括号中写上父类即可
    格式:
        class ClassName(object):

            pass
    定义的类是子类，括号中的类是父类
    子类中找不到属性方法时，会在父类中找，可以说子类继承了父类的属性方法
    一层中父类的父类不能是此层中的父类
    多重继承就在括号中填写多个父类，用逗号隔开

    object 是所有类的基类
    Python3 不写括号也默认继承 object 类

    关于查找父类方法的顺序:
        在 Python2 中，顶层基类不写括号就 从左到右，深度优先 搜索父类的方法
        (此处 顶层基类 指非 object 类的所有顶层基类)
        而继承 object 类，则用 广度优先 搜索父类的方法
        Python3 中不写括号默认继承 object 类，
        所以 Python3 中都是用 广度优先 搜索父类的方法

调用未绑定的类的普通函数:
    ClassName.method(self)
    如果是已实例化的对象，会将自身传入第一个参数，否则不会传入任何东西
    所以此处 self 参数为空，需要自行传入

动态绑定属性或方法:
    ClassOrInstance.attribute = 'any'
    类或实例对象.变量名 = 值
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')


class ClassName:
    
    print('类:', type(object), id(object))

    def method_name(self, *args, **keywords):

        pass

    @staticmethod
    def staticmethod_name(*args, **keywords):

        pass

    @classmethod
    def classmethod_name(cls, *args, **keywords):

        pass


print('2.')


class InheritanceClass(ClassName):

    pass


print('——————————————————————————————————————————————————')
print('\n')


'''
2.__dict__

特殊的类属性
__class__  返回实例或类的类对象
__name__  以字符串返回类对象的类名
__doc__  说明文档
__dict__  字典，存放这个类或实例对象所有的变量。当对象是实例时可以修改其中的键值
__slots__  列表，限定类的实例能够配置的变量(初始未定义)
'''

print('2.')
print('——————————————————————————————————————————————————')

obj = ClassName()
print('1.', ClassName.__class__, type(ClassName.__class__))
print(obj.__class__, type(obj.__class__))
print('2.', ClassName.__name__, type(ClassName.__name__))
print('3.', ClassName.__dict__, type(ClassName.__dict__))
print(obj.__dict__, type(obj.__dict__))

print('——————————————————————————————————————————————————')
print('\n')


'''
3.__init__ __new__

在创建实例对象时自动调用两个方法定义实例对象，括号中的参数自动传递
__new__(cls, *args, **kwargs): 返回一个实例对象
__init__(self, *args, **kwargs): 没有且不能有返回值

先调用 __new__ 方法，返回一个实例对象
并执行实例对象的 __init__ 方法
'''

print('3.')
print('——————————————————————————————————————————————————')


class Class:

    print('1.', '类属性')
    print('类:', type(object), id(object))
    
    def __new__(cls, *args, **keywords):

        self = object.__new__(cls)
        print('__new__:', type(cls), id(cls))
        print('__new__:', type(self), id(self))
        return self

    def __init__(self, *args, **keywords):

        self.args = args
        self.keywords = keywords
        print('__init__:', type(self), id(self))
        self.method_name()
    
    def method_name(self):
        
        print(self.args)
        print(self.keywords)


Class(1, 0, 3, a="'a'", b="'b'", c=2)

print('——————————————————————————————————————————————————')
print('\n')


'''
4.__repr__ __str__ __int__ __float__ __complex__ __bool__
__format__ __bin__ __oct__ __hex__ __hash__

重写一些方法
__repr__(self): repr()直接输出该对象后返回的字符串
__str__(self): str()该对象返回的字符串
__int__(self): int()该对象返回的整数
__float__(self): float()该对象返回的浮点数
__complex__(self): complex()该对象返回的复数
__bool__(self): bool()该对象返回的布尔值
__format__(self, format_spec): format()格式化该对象后返回的字符串
__bin__(self): bin()该对象返回的二进制数值
__oct__(self): oct()该对象返回的八进制数值
__hex__(self): hex()该对象返回的十六进制数值
__hash__(self): hash()该对象返回的哈希值
'''

print('4.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
5.__len__ __iter__ __next__
__getitem__ __setitem__ __delitem__
__reversed__ __contains__

序列类型相关的方法
__len__(self): len()该对象返回的长度
__iter__(self): iter()该对象返回的可迭代对象
__next__(self): 重写循环，使用 raise StopIteration() 跳出循环
__getitem__(self, item): 重写下标
__setitem__(self, key, value): 下标加赋值运算符的形式
__delitem__(self, key): del 语句尝试使用下标删除元素
__reversed__(self): 被 reversed() 函数调用时的行为
__contains__(self, item): 使用成员测试符（in, not in）时的行为

当把实例作为可迭代对象时，__next__ 方法才有作用
'''

print('5.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
6.__getattribute__ __getattr__ __setattr__ __delattr__

属性的访问赋值和删除相关的方法
__getattribute__(self, name): 当被引用存在的属性时返回的值
__getattr__(self, name): 当被引用的属性不存在时的行为
__setattr__(self, name, value): 当设置一个属性时的行为
__delattr__(self, name): 当删除一个属性时的行为
'''

print('6.')
print('——————————————————————————————————————————————————')

print('1.', '__getattribute__ __getattr__ 方法示例')


class A:

    x = True

    def __getattribute__(self, name):

        print('__getattribute__ 被调用了', '查找属性 %r' % name)
        return super().__getattribute__(name)

    def __getattr__(self, name):

        print('__getattr__ 被调用了', '不存在的属性 %r' % name)
        e = AttributeError("'A' object has no attribute %r" % name)
        raise e


a = A()
print(a.x)
print(getattr(a, 'b', None))
try:
    print(a.b)
except AttributeError as e:
    print(e)

print('——————————————————————————————————————————————————')
print('\n')


'''
7.__get__ __set__ __delete__

作为类属性时
__get__(self, instance, owner): 当该类实例是另一个类的类属性并被访问获取值时
__set__(self, instance, value): 当该类实例是另一个类的类属性并被尝试赋值时
__delete__(self, instance): 当该类实例是另一个类的类属性并被尝试删除时
'''

print('7.')
print('——————————————————————————————————————————————————')

print('1.', '__get__ __set__ __delete__ 方法示例')


class B:

    def __get__(self, instance, owner):

        print('__get__', self, instance, owner)

    def __set__(self, instance, value):

        print('__set__', self, instance, value)

    def __delete__(self, instance):

        print('__delete__', self, instance)


class C:
    x = B()

    def __init__(self):

        self.n = self.x


c = C()
print(c, ~1)
c.x
c.x = 2
del c.x
print('实例属性没有效果:', c.n)

print('——————————————————————————————————————————————————')
print('\n')


'''
8.__round__ __divmod__ __abs__ __pos__ __neg__
__add__ __sub__ __mul__ __truediv__
__floordiv__ __mod__ __pow__
__radd__ __rsub__ __rmul__ __rtruediv__
__rfloordiv__ __rmod__ __rpow__
__iadd__ __isub__ __imul__ __itruediv__
__ifloordiv__ __imod__ __ipow__

重写关于数值计算的方法
__round__(self, n=None): round()该对象舍去小数后返回的浮点数（或整数？）
__divmod__(self, other): divmod()该对象整数和取余另一个对象的结果（返回元组）
__abs__(self): abs()该对象返回的绝对值
__pos__(self): +instance 正号
__neg__(self): -instance 负号，取相反数

当 self 在左侧，other 在右侧
__add__(self, other): 加
__sub__(self, other): 减
__mul__(self, other): 乘
__truediv__(self, other): 除
__floordiv__(self, other): 地板除
__mod__(self, other): 取余
__pow__(self, power, modulo=None): 幂。pow() 函数有第三个参数，对结果取余

当 other 在左侧，self 在右侧
__radd__(self, other):
__rsub__(self, other):
__rmul__(self, other):
__rtruediv__(self, other):
__rfloordiv__(self, other):
__rmod__(self, other):
__rpow__(self, other):

与赋值运算符一起使用（加等于乘等于...）
__iadd__(self, other):
__isub__(self, other):
__imul__(self, other):
__itruediv__(self, other):
__ifloordiv__(self, other):
__imod__(self, other):
__ipow__(self, other):
'''

print('8.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
9.__lshift__ __rshift__
__and__ __or__ __xor__
__rlshift__ __rrshift__
__rand__ __ror__ __rxor__
__ilshift__ __irshift__
__iand__ __ior__ __ixor__
__invert__

二进制左移右移，按位与，按位或，按位异或，按位取反
当 self 在左侧，other 在右侧
__lshift__(self, other): 左移位
__rshift__(self, other): 右移位
__and__(self, other): 按位与
__or__(self, other): 按位或
__xor__(self, other): 按位异或

当 other 在左侧，self 在右侧
__rlshift__(self, other):
__rrshift__(self, other):
__rand__(self, other):
__ror__(self, other):
__rxor__(self, other):

与赋值运算符一起使用
__ilshift__(self, other):
__irshift__(self, other):
__iand__(self, other):
__ior__(self, other):
__ixor__(self, other):

__invert__(self): 按位取反
'''

print('9.')
print('——————————————————————————————————————————————————')

print('1.', 1 or 2)

print('——————————————————————————————————————————————————')
print('\n')


'''
10.__eq__ __ne__ __gt__ __ge__ __lt__ __le__

比较运算符
__eq__(self, other): 等于
__ne__(self, other): 不等于，如已重写 __eq__ 方法则可以不写
__gt__(self, other): 大于
__ge__(self, other): 大于等于
__lt__(self, other): 小于
__le__(self, other): 小于等于
'''

print('10.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
11.__enter__ __exit__

with 语句 上下文管理器调用的方法
__enter__(self): 上下文管理器开始
__exit__(self, exc_type, exc_value, traceback): 上下文管理器结束
'''

print('11.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
12.__del__

最后的倔强
__del__(self): 被 del 语句释放掉内存后的行为
'''

print('12.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')
