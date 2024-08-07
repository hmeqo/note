# 内置BIF (Built In Function)

## 属性

| 函数 | 描述 |
| --- | --- |
| **输入输出** |  |
| [`print`](#print) | 输出 |
| [`input`](#input) | 输入 |
| **对象属性操作** |  |
| [`delattr`](#delattr) | 删除一个对象拥有的属性 |
| [`getattr`](#getattr) | 从一个对象中获取属性 |
| [`hasattr`](#hasattr) | 一个对象是否拥有这个属性 |
| [`setattr`](#setattr) | 给一个对象设置一个属性 |
| **查询对象** |  |
| [`dir`](#dir) | 返回对象的属性 |
| [`globals`](#globals) | 以字典的形式返回全局变量 |
| [`help`](#help) | 对象的帮助文档, 文本文档 |
| [`id`](#id) | 返回对象的标识 (id) |
| [`locals`](#locals) | 以字典的形式返回局部变量 |
| [`repr`](#repr) | 调用对象的 \_\_repr\_\_ 方法 |
| [`type`](#type) | 返回对象的类型 (type) |
| **判断对象** |  |
| [`callable`](#callable) | 对象是否是可调用的 |
| [`isinstance`](#isinstance) | 该对象是否是某个类的实例 |
| [`issubclass`](#issubclass) | 该对象是否是某个类的子类 |
| **类与对象** |  |
| [`property`](#property) | 属性 |
| [`super`](#super) | 父类 |

### print

输出一个对象, 内部实现通过 \_\_str\_\_ 方法将其转换为字符串

| 参数 | 描述 |
| --- | --- |
| values | 输出的元素, 调用其 \_\_str\_\_ 方法输出 |
| sep | 每个逗号之间的元素用什么分隔, 默认一个空格 |
| end | 结束时输出什么, 默认 '\n' |
| file | 输出到哪个文件 |
| flush | 结束调用 print 函数后立即输出, whether to forcibly flush the stream |

### input

接收用户输入的数据, 返回字符串  
括号中可以填写字符串，填写后在字符串后面提供用户输入空间

### delattr

删除类或实例的一个属性, 没有则报错, 相当于 del name.var

示例:

```python
class A:

    x = 2


print(getattr(A, 'x', "访问的属性 'x'不存在"))

delattr(A, 'x')

print(getattr(A, 'x', "访问的属性 'x'不存在"))
```

### getattr

获取类或实例的属性, 相当于 name.var  
如果填写了第三个参数, 当属性不存在时, 捕获异常, 返回第三个参数

示例:

```python
getattr(obj, "__name__")  # 获取obj对象的 __name__ 属性, 不存在则报错

getattr(obj, "__name__", None)  # 获取obj对象的 __name__ 属性, 不存在则返回 None
```

### hasattr

一个类或实例是否拥有这个属性

示例:

```python
print('1.', hasattr(str, 'isdecimal'))
print('2.', hasattr(str, '__init__'))
print('3.', hasattr(str, 'A'))
```

### setattr

给一个类或实例设置一个属性, 相当于 name.var = 'any'

示例:

```python
class A:

    pass


print(getattr(A, 'x', "访问的属性 'x'不存在"))

setattr(A, 'x', 2)

print(getattr(A, 'x', "访问的属性 'x'不存在"))
```

### dir

返回对象的属性

示例:

```python
print(dir(__builtins__))
```

### globals

以字典的形式返回全局变量

示例:

```python
print(globals())
```

### help

对象的帮助文档, 文本文档

示例:

```python
help(help)
```

### id

返回对象的标识 (id)

示例:

```python
a = [1, 2, 3, 4]
print('1.', id(a))
print('2.', id(a[0]))
```

### locals

以字典的形式返回局部变量

示例:

```python
print('1.', locals())


def a():
    
    x = '2'
    n = 1
    print(locals())

    def b():

        nonlocal x
        print(locals())
        return None
    
    return b()


print('2.')
a()
```

### repr

调用对象的 \_\_repr\_\_ 方法

示例:

```python
from decimal import Decimal

print('1.', 'hello', repr('hello'))
print('2.', Decimal('1'), repr(Decimal('1')))
```

### callable

对象是否是可调用的 (如果是实例那么就看它是否拥有 \_\_call\_\_ 方法)

示例:

```python
print('1.', callable(int))
print('2.', callable(1))
```

### type

返回对象的类型

示例:

```python
a = [1, 2, 3, 4]

print('1.', type(a))

print('2.', type(a[0]))
```

### isinstance

返回一个对象是一个类的实例还是它的子类的实例, 返回布尔值  
第二个参数可以填由类组成的元组, 例如: isinstance(a, (A, B, C))

示例:

```python
a = '123'
print('1.', isinstance(a, str))

a = 123
print('2.', isinstance(a, str))


class A:

    def __init__(self):

        pass


a = A()
print('3.', isinstance(a, A))
```

### issubclass

返回一个类是否是一个类的子类, 返回布尔值  
第二个参数可以填由类组成的元组, 例如: issubclass(a, (A, B, C))

示例:

```python
class A:

    def __init__(self):

        pass


print('1.', issubclass(A, object))
print('2.', issubclass(A, str))
```

### property

| 参数 | 描述 |
| --- | --- |
| fget | 获取 x 的值使用的callable对象 |
| fset | 设置 x 的值使用的callable对象 |
| fdel | 删除 x 的值使用的callable对象 |
| doc | 文档字符串 |

| 方法 | 描述 |
| --- | --- |
| getter | 设置 fget 函数 |
| setter | 设置 fset 函数 |
| deleter | 设置 fdel 函数 |

示例:

```python
class A:

    _month = 1
    _day = 1

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    def get_month(self):
        return self._month

    def set_month(self, value):
        self._month = value

    month = property(fget=get_month, fset=set_month)
```

### super

用于调用父类的方法和属性  
第一个参数为类, 指明了要从 mro 的哪个位置之后开始找  
第二个参数为类或实例, 决定了要查找的 mro 链

语法:

```python
super(类, 类或实例)
```

示例:

```python
class A:

    def __init__(self):
        print("A")

class B(A):

    def __init__(self):
        super().__init__()
        print("B")
```
