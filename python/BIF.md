# 内置BIF (Built In Function)

## 属性

| 函数                        | 描述                         |
| --------------------------- | ---------------------------- |
| **输入输出**                |                              |
| [`print`](#print)           | 输出                         |
| [`input`](#input)           | 输入                         |
| **对象属性操作**            |                              |
| [`delattr`](#delattr)       | 删除一个对象拥有的属性       |
| [`getattr`](#getattr)       | 从一个对象中获取属性         |
| [`hasattr`](#hasattr)       | 一个对象是否拥有这个属性     |
| [`setattr`](#setattr)       | 给一个对象设置一个属性       |
| **查询对象**                |                              |
| [`dir`](#dir)               | 返回对象的属性               |
| [`globals`](#globals)       | 以字典的形式返回全局变量     |
| [`help`](#help)             | 对象的帮助文档, 文本文档     |
| [`id`](#id)                 | 返回对象的标识 (id)          |
| [`locals`](#locals)         | 以字典的形式返回局部变量     |
| [`repr`](#repr)             | 调用对象的 \_\_repr\_\_ 方法 |
| [`type`](#type)             | 返回对象的类型 (type)        |
| **判断对象**                |                              |
| [`callable`](#callable)     | 对象是否是可调用的           |
| [`isinstance`](#isinstance) | 该对象是否是某个类的实例     |
| [`issubclass`](#issubclass) | 该对象是否是某个类的子类     |
| **类与对象**                |                              |
| [`property`](#property)     | 属性                         |
| [`super`](#super)           | 父类                         |
| **操作可迭代对象**          |                              |
| [`all`](#all)               | 元素都为真                   |
| [`max`](#max)               | 最大值                       |
| [`min`](#min)               | 最小值                       |
| [`sorted`](#sorted)         | 对元素排序                   |
| [`sum`](#sum)               | 数值总和                     |
| [`enumerate`](#enumerate)   | 次数和元素                   |
| [`filter`](#filter)         | 过滤元素                     |
| [`map`](#map)               | 加工元素                     |
| [`range`](#range)           | 产生整数序列                 |
| [`reversed`](#reversed)     | 翻转元素排序                 |
| [`iter`](#iter)             | 迭代器                       |
| [`next`](#next)             | 循环                         |
| **文件操作**                |                              |
| [`open`](#open)             | 读写文件                     |
| **数值计算**                |                              |
| [`abs`](#abs)               | 参数的绝对值                 |
| [`divmod`](#divmod)         | 整除和取余的结果             |
| [`pow`](#pow)               | 幂运算                       |
| [`round`](#round)           | 保留小数位                   |
| **数据编码转换**            |                              |
| [`bin`](#bin)               | 转换二进制                   |
| [`chr`](#chr)               | 编码转换字符                 |
| [`hex`](#hex)               | 转换十六进制                 |
| [`oct`](#oct)               | 转换八进制                   |
| [`ord`](#ord)               | 转换十进制编码               |
| **代码执行**                |                              |
| [`exec`](#exec)             | 解释并执行给定的字符串代码   |
| [`eval`](#eval)             | 获取给定的字符串代码执行结果 |
| **类型转换**                |                              |
| [`bool`](#bool)             | 转换成布尔类型               |
| [`bytes`](#bytes)           | 转换成字节类型               |
| [`complex`](#complex)       | 转换成复数类型               |
| [`dict`](#dict)             | 转换成字典                   |
| [`float`](#float)           | 转换成浮点数类型             |
| [`int`](#int)               | 转换成整数类型               |
| [`list`](#list)             | 转换成列表                   |
| [`set`](#set)               | 转换成集合                   |
| [`str`](#str)               | 转换成字符串                 |
| [`tuple`](#tuple)           | 转换成元组                   |

### print

输出一个对象, 内部实现通过 \_\_str\_\_ 方法将其转换为字符串

| 参数   | 描述                                                                |
| ------ | ------------------------------------------------------------------- |
| values | 输出的元素, 调用其 \_\_str\_\_ 方法输出                             |
| sep    | 每个逗号之间的元素用什么分隔, 默认一个空格                          |
| end    | 结束时输出什么, 默认 '\n'                                           |
| file   | 输出到哪个文件                                                      |
| flush  | 结束调用 print 函数后立即输出, whether to forcibly flush the stream |

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

| 参数 | 描述                          |
| ---- | ----------------------------- |
| fget | 获取 x 的值使用的callable对象 |
| fset | 设置 x 的值使用的callable对象 |
| fdel | 删除 x 的值使用的callable对象 |
| doc  | 文档字符串                    |

| 方法    | 描述           |
| ------- | -------------- |
| getter  | 设置 fget 函数 |
| setter  | 设置 fset 函数 |
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

### all

用于判断可迭代对象中所有元素是否都为真。
当可迭代对象中所有元素都为真（非零、非空、非False）时返回True，否则返回False。
空的可迭代对象始终返回True。

示例:

```python
a = [2, 1]
print(all(a))
a = [2, '2', '1']
print(all(a))
a = [12, 0]
print(all(a))
a = []
print(all(a))
```

### max

用于返回序列中的最大值。参数必须是可迭代对象，元素应该是可比较的类型。

示例:

```python
a = [2, 1]
print(max(a))
a = ['2', '1']
print(max(a))
a = '21'
print(max(a))
a = {'2': 3, '1': 0}
print(max(a))
```

### min

用于返回序列中的最小值。参数必须是可迭代对象，元素应该是可比较的类型。

示例:

```python
a = [2, 1]
print(min(a))
a = ['2', '1']
print(min(a))
a = '21'
print(min(a))
a = {'2': 3, '1': 0}
print(min(a))
```

### sorted

用于对可迭代对象进行排序，返回排序后的列表。不会改变原始可迭代对象。

可选参数：

- `reverse`: 排序顺序，默认为 False（升序），设置为 True 为降序
- `key`: 指定排序规则的函数，例如按长度或特定元素排序

注意：传入的可迭代对象中的元素应该是可比较的类型，否则可能报错。

示例:

```python
a = (2, 1, 3)
print(sorted(a))
a = {2: 3, 1: 4, 3: 5}
print(sorted(a))
print(sorted(a, reverse=True))
a = ('222', '11', '3')
print(sorted(a, key=lambda x: len(x)))
a = ((1, 2), (2, 1), (3, 0))
print(sorted(a, key=lambda x: x[1]))
```

### sum

用于返回序列中数值的总和。参数必须是可迭代对象，且元素必须是数字类型（整数、浮点数、复数等）或可加法运算的对象。

示例:

```python
a = [2, 1]
print(sum(a))
a = [2, 1.5]
print(sum(a))
a = [0.1, 0.2]
print(sum(a))
a = [(1+2j), (2+3j)]
print(sum(a))
```

### enumerate

用于返回一个枚举对象，生成索引和元素的元组。索引从0开始，通常用于循环中获取元素及其索引。

示例:

```python
a = ['a', 'b', 'c', 'd']
print(list(enumerate(a)))
a = {'a': 'b', 'c': 'd'}
print(list(enumerate(a)))
```

### filter

用于过滤可迭代对象中的元素，只保留使函数返回 True 的元素。返回一个迭代器。

参数：

- `function`: 过滤函数，接收一个参数并返回布尔值。如果为 None，则过滤掉假值（False, None, 0, 空字符串等）。
- `iterable`: 要过滤的可迭代对象。

示例:

```python
print(list(filter(lambda x: x % 3, [4, 3, 7, 5])))
print(list(filter(lambda x: x.isdecimal(), '2a3b中文c')))
```

### map

用于对可迭代对象中的每个元素应用一个函数，返回一个迭代器。当最短的可迭代对象耗尽时停止。

参数：

- `func`: 要应用的函数
- `iter1`: 可迭代对象（可以传入多个可迭代对象）

对可迭代对象中每个元素都使用函数加工，返回一个可迭代对象。

示例:

```python
print(list(map(lambda x: x*3, [4, 3, 7, 5])))
print(list(map(lambda x: x.title(), 'abc')))
print(list(map(lambda x: x.swapcase(), ['map', 'English', 'Python'])))
```

### range

用于生成一个整数序列，返回一个不可变的序列类型，通常用于循环中。

参数：

- `start`: 序列的起始值，默认为 0
- `stop`: 序列的结束值（不包含）
- `step`: 步长，默认为 1

示例:

```python
print(range(10))
print(list(range(10)))
print(range(0, 10, 1))
print(list(range(0, 10, 1)))
print(range(9, -1, -1))
print(list(range(9, -1, -1)))
print(range(0, -10, -1))
print(list(range(0, -10, -1)))
```

### reversed

用于返回一个反转序列的迭代器。不会改变原始序列。

示例:

```python
a = (2, 1, 3)
print(reversed(a))
print(tuple(reversed(a)))
a = {2: 3, 1: 4, 3: 5}
print(tuple(reversed(a)))
a = (2, 1, '3')
print(tuple(reversed(a)))
```

### iter

用于调用对象的 `__iter__` 方法返回一个可迭代对象。如果对象没有 `__iter__` 方法则会抛出异常。

示例:

```python
# 基本用法
a = [1, 2, 3]
print(iter(a))
print(list(iter(a)))

# 字符串迭代
b = "hello"
print(iter(b))
print(list(iter(b)))

# 字典迭代（键）
c = {'a': 1, 'b': 2}
print(iter(c))
print(list(iter(c)))
```

### next

用于调用对象的 `__next__` 方法返回一个值。如果对象没有 `__next__` 方法则会抛出异常。通常在对象的 `__next__` 方法中定义了循环规则，当循环结束时通过抛出 `StopIteration` 异常来结束循环。

示例:

```python
# 基本用法
a = iter([1, 2, 3])
print(next(a))
print(next(a))
print(next(a))
# print(next(a))  # 这里会抛出 StopIteration

# 使用默认值避免异常
b = iter([])
print(next(b, 'default'))

# 文件迭代示例（假设有文件对象）
# with open('file.txt') as f:
#     print(next(f))
```

### open

用于读写文件，返回文件对象。可以与 `with` 语句配合使用，确保文件正确关闭。

参数：

- `file`: 文件名及其扩展名
- `mode`: 文件打开模式
  - `'r'`: 以读模式打开，文件必须存在
  - `'w'`: 以写模式打开，文件不存在则创建，存在则覆盖
  - `'x'`: 创建新文件并以写模式打开，文件必须不存在
  - `'a'`: 以末尾追加模式打开，文件不存在则创建
  - 可选后缀（可多选）:
    - `'+'`: 可读可写
    - `'b'`: 以二进制模式打开
    - `'t'`: 以文本模式打开（默认）
    - `'U'`: 通用换行符（文本模式生效）
- `encoding`: 文件编码格式，例如 `encoding='UTF-8'`，二进制模式不可用

文件对象方法：

- `close()`: 关闭文件
- `read(size)`: 按字符读取，返回字符串
- `readline(size)`: 按单行读取，返回字符串
- `readlines(size)`: 按多行读取，返回列表
- `write(string)`: 写入字符串
- `writelines(iterable)`: 写入可迭代对象
- `tell()`: 返回当前指针位置
- `seek(offset, whence)`: 设置指针位置
  - `whence`: 0 表示从开头，1 从当前位置，2 从末尾

示例:

```python
# 基本文件读取
file = open('open_读写文件.py', 'r', encoding='UTF-8')
print('1.', file.readline())
file.close()

# 使用 with 语句自动关闭文件
with open('open_读写文件.py', 'r', encoding='UTF-8') as file:
    print('2.', file.readline())

# 读取方法示例
with open('open_读写文件.py', 'r', encoding='UTF-8') as file:
    print('1.', file.read(100))
    file.seek(0, 0)
    print('2.', file.readline(100))
    file.seek(0, 0)
    print('3.', file.readlines(100))

# 写入方法示例
with open('open_读写文件.txt', 'w', encoding='UTF-8') as file:
    file.write('hello world')
    file.seek(0, 0)
    file.write('NiHao')

# 文件指针操作
with open('open_读写文件.txt', 'w', encoding='UTF-8') as file:
    print('1.', file.tell())
    file.seek(5)
    print('2.', file.tell())
```

### abs

返回参数的绝对值。参数必须是数字。

示例:

```python
a = 10
print(abs(a))
a = -10.5
print(abs(a))
a = 10+20j
print(abs(a))
```

### divmod

返回两个参数整除和取余的结果。参数必须是数字。

示例:

```python
a = 20.5
b = 10.5
print(divmod(a, b))
a = 20.5
b = -10.5
print(divmod(a, b))
```

### pow

返回第一个参数的第二个参数次幂。参数必须是数字。当第一个参数是整数时，可以再加上第三个参数，返回取余的结果。

示例:

```python
a = 2
print(pow(a, 3))
a = -2.5
print(pow(a, 3))
a = 2
print(pow(a, 3, 3))
```

### round

保留小数位。参数必须是数字。

示例:

```python
a = 2.131
print(round(a, 1))
```

### ord

把一位字符转换成十进制unicode编码。

示例:

```python
print(ord('a'), ord('b'))
```

### chr

将整数按unicode编码表转换成字符。

示例:

```python
print(ord('a'), ord('b'))
print(chr(ord('a')), chr(ord('b')))
```

### bin

将整数转换成二进制编码，返回0b开头的字符串。

示例:

```python
print(bin(ord('a')), bin(ord('b')))
```

### oct

将整数转换成八进制编码，返回0o开头的字符串。

示例:

```python
print(oct(ord('a')), oct(ord('b')))
```

### hex

将整数转换成十六进制编码，返回0x开头的字符串。

示例:

```python
print(hex(ord('a')), hex(ord('b')))
```

### exec

解释并执行给定的字符串代码。

示例:

```python
def f():
    print('hello world')

exec('f()')
```

### eval

获取给定的字符串代码执行结果。

示例:

```python
a = "['哈哈']"
print('转换前', a, type(a))
a = eval(a)
print('转换后', a, type(a))
a = '12357.44'
print('转换前', a, type(a))
a = eval(a)
print('转换后', a, type(a))
a = """print('我原本不是字符串吗？', [i for i in range(10)])"""
print(eval(a))
print(eval(bin(ord('a'))))
```

### bool

将括号里的对象转换成布尔类型。任何对象都有一个布尔值。

示例:

```python
a = [10.5, '哈哈']
print('转换前', a, '类型', type(a))
print('转换后', bool(a), '类型', type(bool(a)))
a = []
print('转换前', a, '类型', type(a))
print('转换后', bool(a), '类型', type(bool(a)))
```

### bytes

转换成字节类型。转换数字直接填写参数即可，转换字符串需要填写编码格式。

示例:

```python
print(bytes(1))
```

### complex

将括号里的两个数转换成复数类型。两个参数必须是数字，或者传入一个字符串。

示例:

```python
a = 10
b = 20.5
print('转换前', a, b, '类型', type(a), type(b))
print('转换后', complex(a, b), '类型', type(complex(a, b)))
a = '10+20.5j'
print('转换前', a, '类型', type(a))
print('转换后', complex(a), '类型', type(complex(a)))
```

### dict

将括号里的可迭代对象转换成字典。

示例:

```python
a = [('123', 1+2j)]
print('转换前', a, '类型', type(a))
print('转换后', dict(a), '类型', type(dict(a)))
a = [('10', '哈哈'), ('233', '滑稽')]
print('转换前', a, '类型', type(a))
print('转换后', dict(a), '类型', type(dict(a)))
```

### float

将括号里的对象转换成浮点数类型。需要注意要转换的对象只能是数字不能是字符或者其他对象。整数转成浮点数时，会在末尾添上 .0。

示例:

```python
a = '1234.1234'
print('转换前', a, '类型', type(a))
print('转换后', float(a), '类型', type(float(a)))
a = 10
print('转换前', a, '类型', type(a))
print('转换后', float(a), '类型', type(float(a)))
a = '1E6'
print('转换前', a, '类型', type(a))
print('转换后', float(a), '类型', type(float(a)))
```

### int

将括号里的对象转换成整数类型。需要注意要转换的对象只能是数字，不能是字符或其他对象。浮点类型转换整数类型时，会去掉小数。

示例:

```python
a = '1234'
print('转换前', a, '类型', type(a))
print('转换后', int(a), '类型', type(int(a)))
a = 10.9
print('转换前', a, '类型', type(a))
print('转换后', int(a), '类型', type(int(a)))
```

### list

将括号里的可迭代对象转换成列表。

示例:

```python
a = '1234.1234'
print('转换前', a, '类型', type(a))
print('转换后', list(a), '类型', type(list(a)))
a = (10, '哈哈')
print('转换前', a, '类型', type(a))
print('转换后', list(a), '类型', type(list(a)))
```

### set

将括号里的可迭代对象转换成集合。

示例:

```python
a = '1234.1234'
print('转换前', a, '类型', type(a))
print('转换后', set(a), '类型', type(set(a)))
a = (10, '哈哈')
print('转换前', a, '类型', type(a))
print('转换后', set(a), '类型', type(set(a)))
```

### str

将括号里的对象转换成字符串。似乎任何对象都能转换成字符串。

示例:

```python
a = 1234.1234
print('转换前', a, '类型', type(a))
print('转换后', str(a), '类型', type(str(a)))
a = [10, '哈哈']
print('转换前', a, '类型', type(a))
print('转换后', str(a), '类型', type(str(a)))
```

### tuple

将括号里的可迭代对象转换成元组。

示例:

```python
a = '1234.1234'
print('转换前', a, '类型', type(a))
print('转换后', tuple(a), '类型', type(tuple(a)))
a = [10, '哈哈']
print('转换前', a, '类型', type(a))
print('转换后', tuple(a), '类型', type(tuple(a)))
```
