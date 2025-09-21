# Python 基本库

## 目录

| 模块                               | 描述               |
| ---------------------------------- | ------------------ |
| **日期时间相关**                   |                    |
| [datetime](#datetime-模块)         | 日期和时间处理     |
| [time](#time-模块)                 | 时间相关功能       |
| **函数工具**                       |                    |
| [functools](#functools-模块)       | 函数工具和高阶函数 |
| [keyword](#keyword-模块)           | Python关键字操作   |
| **GUI界面**                        |                    |
| [tkinter](#tkinter-模块)           | GUI界面开发        |
| **数据处理**                       |                    |
| [configparser](#configparser-模块) | 配置文件处理       |
| [copy](#copy-模块)                 | 对象拷贝操作       |
| [hashlib](#hashlib-模块)           | 加密算法           |
| [json](#json-模块)                 | JSON数据交换格式   |
| [pickle](#pickle-模块)             | 二进制序列化       |
| **数值计算**                       |                    |
| [decimal](#decimal-模块)           | 精确小数计算       |
| [fractions](#fractions-模块)       | 分数运算           |
| [random](#random-模块)             | 随机数生成         |

## datetime 模块

和时间有关。

导入方式:

```python
import datetime
```

示例:

```python
import datetime
print(datetime.datetime.now().timestamp())
```

## functools 模块

函数工具。

导入方式:

```python
import functools
```

### reduce()

对数字元素的序列进行加减乘除等计算。

示例:

```python
import functools
print(functools.reduce(lambda x, y: x * y, [i for i in range(1, 6)]))
```

## keyword 模块

与 Python 标识符有关。

导入方式:

```python
import keyword
```

### iskeyword()

判断是否是保留标识符。

示例:

```python
import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('print'))
print(keyword.iskeyword('is'))
```

### kwlist

变量，所有的保留标识符。

示例:

```python
import keyword
print(keyword.kwlist)
```

## time 模块

和时间有关。

导入方式:

```python
import time
```

### sleep()

休眠一段时间。

示例:

```python
import time
time1 = time.perf_counter()
print(time.perf_counter() - time1)
```

### time() time_ns() perf_counter()

计时:

- time(): 返回当前浮点数秒数时间
- time_ns(): 返回当前时间，整数，精度0.000000100，单位纳秒
- perf_counter(): CPU运行时间，浮点数秒数，高精度

示例:

```python
import time
time1 = time.perf_counter()
print(time.time())
print(time.time_ns())
print(time.perf_counter() - time1)
```

### gmtime() localtime() ctime() mktime() strftime() strptime()

浮点数秒数转换:

- gmtime(): 返回格林时间，或把浮点数秒数转换成格林时间
- localtime(): 返回本地时间，或把浮点数秒数转换成本地时间
- ctime(): 将浮点数秒数转换成字符串的本地时间
- mktime(): 把元组转换成无精度的浮点数秒数
- strftime(): 格式化浮点数秒数时间
- strptime(): 按照格式把字符串时间转换成 time.struct_time

转换后返回的对象的可使用方法（以下返回值都是整数）:

- tm_year: 年: 正常值
- tm_mon: 月: 取值区间 [1 - 31]
- tm_mday: 日: 取值区间 [1 - 31]
- tm_hour: 时: 取值区间 [0 - 23]
- tm_min: 分: 取值区间 [0 - 59]
- tm_sec: 秒: 取值区间 [0 - 61]
- tm_wday: 星期: 取值区间 [0 - 6]
- tm_yday: 从一月一日起算过了几天: 取值区间 [1 - 366]
- tm_isdst: 夏令时标识符，实行为正，不实行为 0，不清楚为负

示例:

```python
import time
import os

a = time.localtime(os.path.getctime(os.curdir))
print(os.path.abspath(os.curdir) + '\n' + str(a))
print(a.tm_year, '年', a.tm_mon, '月', a.tm_mday, '日', '星期', a.tm_wday + 1)
print(a.tm_hour, ':', a.tm_min, ':', a.tm_sec, sep='')
print(time.ctime(time.time()))
print(time.mktime(time.localtime()))
a = time.strftime('%Y/%m/%d %H:%M:%S')
print(a)
print(time.strptime(a, '%Y/%m/%d %H:%M:%S'))
```

## tkinter 模块

制作GUI窗口的模块。

导入方式:

```python
import tkinter
```

### Tk()

创建一个窗口。注: 必须先创建一个根窗口，才能进行其它操作。

- Tk(): 实例化一个根窗口
- Toplevel(): 实例化根窗口的顶层窗口，子窗口

以上实例都可使用的方法属性:

- mainloop(): 窗口循环显示（一个大的 while 循环）
- quit(): 离开 TCL 解释器，所有控件将被销毁
- destroy(): 销毁窗口及其所有控件，将终止应用于它的 TCL 解释器
- title() wm_title(): 窗口标题，括号中填入字符串
- geometry() wm_geometry(): 窗口初始大小和位置（O点在左上角，箭头往右下）
  - 参数: newGeometry: 传入字符串，格式: `<width>x<height>+<x>+<y>`（长乘宽注意是小写 x）
- minsize() wm_minsize(): 最小尺寸，参数: x, y
- maxsize() wm_maxsize(): 最大尺寸，参数: x, y
- resizable() wm_resizable(): 可调整窗口大小
  - 参数: width: 可调整长度，填 0 为不可调整；height: 可调整高度，填 0 为不可调整
- iconbitmap() wm_iconbitmap(): 设置图标，字符串参数填路径
- register(): 新创建一个 TCL 函数，参数填入 Python 函数

如果使用 destroy() 窗口无法退出，那么就先调用 quit()

### Frame() LabelFrame()

框架。提供一个框架，可在里面添加控件。

- Frame(): 普通的框架
- LabelFrame(): 标签框架
  - 参数: text: 文本；foreground: 可简写成 fg，前景颜色，填入字符串

以上实例都可用的方法属性:

- master: 上级
- image: 图片，传入 tkinter.PhotoImage() 实例对象
- background: 可简写成 bg，背景颜色
- width: 控件长
- height: 控件宽
- padx: x 轴间距
- pady: y 轴间距
- config: 配置参数

### pack() grid() place()

放置控件。

- pack(): 上下左右自动放置
  - 参数: side: 位置（'top' 'bottom' 'left' 'right'）；anchor: 锚，对齐（'e' 's' 'w' 'n' 'ne' 'nw' 'se' 'sw'）；fill: 填充空白（'x' 'y'）
- grid(): 网格布局放置
  - 参数: row: 行；column: 列；sticky: 粘性，和 pack() 的 anchor 类似
- place(): 放置至指定位置
  - 参数: x: 横坐标；y: 纵坐标；anchor: 锚点

以上实例都可用的方法属性:

- padx: 外部 x 轴间距
- pady: 外部 y 轴间距

### pack_forget() place_forget() grid_forget() forget()

拿起控件。注: 只能对创建好的控件对象使用。

- pack_forget(): 拿起被 pack() 放置的控件
- place_forget(): 拿起被 place() 放置的控件
- grid_forget(): 拿起被 grid() 放置的控件
- forget(): 看文档好像是只能拿起被 pack() 放置的控件

想重新放置使用放置控件的方法即可。

### Label() Button()

控件。

- Label(): 创建一个标签
- Entry(): 输入框
  - 参数: show: 传入字符串，每个字符用这个字符串的第一个字符显示出来；validate: 验证输入（'focus' 'focusin' 'focusout' 'key' 'all' 'none'）；validatecommand: 验证时调用的函数；invalidatecommand: 无效输入时调用的函数；state: 输入模式（'readonly' 'disabled'）；takefocus: Tab 键焦点转移，填布尔值
  - 实例可使用的方法属性: get() 获取值；insert() 插入值；delete() 删除值
- Button(): 创建一个按钮
  - 参数: command: 触发函数
- Checkbutton(): 勾选按钮
  - 参数: command: 触发函数；variable: 传入 StringVar() 或 IntVar() 实例对象
- Radiobutton(): 按钮组
  - 参数: command: 触发函数；variable: 传入 StringVar() 或 IntVar() 实例；value: 值；indicatoron: 按钮形式，默认 True，False 是按钮
- Listbox(): 选项列表
  - 参数: selectmode: 选择模式（'single' 'browse' 'multiple' 'extended'）；yscrollcommand: 每次滚动调用的函数
  - 实例可用方法属性: insert() 插入元素；delete() 删除元素；activate() 指定选中的元素；yview() 获取或修改浏览到的位置
- Text(): 主题，能显示多种形式的主题
  - 实例可用方法属性: insert() 以某种形式加入字符串；window_create() 以某种形式加入控件；image_create() 以某种形式加入图片
- Canvas(): 画布
  - 实例可用方法属性: create_line() 创建一条直线；create_rectangle() 创建一个矩形；create_text() 创建一个文本；create_oval() 创建一个椭圆；coords() 调整坐标；itemconfig() 再次配置参数；move() 移动图形；moveto() 移动图形；delete() 删除图形
- Scrollbar(): 滚动条
  - 参数: master: 上级；command: 每次滚动调用的函数
  - 实例可用方法属性: set() 设置滚动条起始和结束百分比位置；get() 获取滚动条起始和结束百分比位置
- Scale(): 滑动条
  - 参数: from_: 起始；to: 终止；orient: 朝向（'vertical' 'horizontal'）；tickinterval: 间隔多少标记一次滑动条数值；resolusion: 分辨率，可移动的大小；length: 滑动条长度
  - 实例可用方法: set() 设置滑动条当前位置；get() 获取滑动条当前位置

以上都可填写的参数:

- textvariable: 文本变量，传入 StringVar() 实例对象
- text: 显示的文本
- image: 图片，传入 tkinter.PhotoImage() 实例对象
- compound: 文本图片混合（'center'）
- font: 字体（('fontname', size)）
- justify: 文本对齐（'left' 'right' 'center'）
- foreground: 可简写成 fg，前景颜色，填入字符串
- padx: 内部 x 轴间距
- pady: 内部 y 轴间距
- master: 上级
- background: 可简写成 bg，背景颜色
- width: 控件长
- height: 控件宽
- config: 配置，再次填写参数

### StringVar() IntVar() PhotoImage()

各种参数对象。

- StringVar(): 提供可变的字符串对象
  - 参数: value: 值
  - 实例可使用方法属性: set() 设置值，填入字符串；get() 获取值
- PhotoImage():
  - 参数: file: 图片文件路径

以上都可填写的参数:

- master: 上级
- name:

## configparser 模块

配置文件。

导入方式:

```python
import configparser
```

## copy 模块

拷贝。

导入方式:

```python
import copy
```

### copy() deepcopy()

- copy(): 和一般的拷贝一样，都是浅拷贝
- deepcopy(): 深拷贝

示例:

```python
import copy

lst = [1, 2, 3]
print('原列表', lst)
lst2 = copy.copy(lst)
print('拷贝的列表', lst2)

lst = [[1], [2], [3]]
print('原列表', lst)
lst2 = copy.deepcopy(lst)
print('拷贝的列表', lst2)
```

## hashlib 模块

加密算法。

导入方式:

```python
import hashlib
```

### md5() sha1() sha256()

对字符串编码加密。

- md5(): 密文长度 32
- sha1(): 密文长度 40
- sha256(): 密文长度 64

以上返回的对象可用方法属性:

- hexdigest(): 十六进制密文
- update(): 相当于在末尾额外添加字符

示例:

```python
import hashlib

msg = '你好'
p = hashlib.md5(msg.encode('UTF-8'))
print(p.hexdigest())

p = hashlib.sha1(msg.encode('UTF-8'))
print(p.hexdigest())

p = hashlib.sha256(msg.encode('UTF-8'))
print(hashlib.sha256(msg.encode('UTF-8')).hexdigest())

p = hashlib.sha256(msg.encode('UTF-8'))
p.update(msg.encode('UTF-8'))
print(p.hexdigest())

p = hashlib.sha256((2 * msg).encode('UTF-8'))
print(p.hexdigest())
```

## json 模块

基于JavaScript语言的轻量级的数据交换格式(JavaScript Object Notation)。

导入方式:

```python
import json
```

### loads()

读取，转换JSON字符串为Python对象。

参数:

- s: 传入JSON格式的字符串

## pickle 模块

转换二进制数据存储的模块，用于Python对象的序列化和反序列化。

导入方式:

```python
import pickle
```

### dump() load()

转换成二进制存储和载入。

- dump(): 填入对象和文件，把对象转换成二进制存入文件
- load(): 加载二进制，参数填文件，返回Python对象

示例:

```python
import pickle

a = [123, 3.14, 'pickle', ['pickle']]
with open('pickle.pkl', 'wb') as file:
    pickle.dump(a, file)

with open('pickle.pkl', 'rb') as file:
    print(pickle.load(file))
```

## decimal 模块

用于精确计算小数的模块，避免浮点数计算误差。

导入方式:

```python
import decimal
```

### Decimal()

保存精确的十进制数字。因Python计算浮点数会产生误差，所以使用这个来避免误差。

格式：`decimal.Decimal('0.1')`
注意：填入的是一个字符串

示例:

```python
import decimal

print('不使用模块计算 0.1 + 0.2=', 0.1 + 0.2)
print('使用该模块计算 0.1 + 0.2=', decimal.Decimal('0.1') + decimal.Decimal('0.2'))
```

### decimal.getcontext().prec

调整计算精度。

示例:

```python
import decimal

print(decimal.Decimal('1') / decimal.Decimal('3'))

# 保存当前精度
original_prec = decimal.getcontext().prec
# 设置新精度
decimal.getcontext().prec = 100
print(decimal.Decimal('1') / decimal.Decimal('3'))
# 恢复原精度
decimal.getcontext().prec = original_prec
```

## fractions 模块

分式计算模块，用于处理分数运算。

导入方式:

```python
import fractions
```

### Fraction()

创建分数对象。第一个参数是分子，第二个参数是分母。

格式：`fractions.Fraction(1, 2)`

示例:

```python
import fractions

print(fractions.Fraction(1, 2))
print(fractions.Fraction(3, 4) + fractions.Fraction(1, 4))
```

## random 模块

随机数生成模块。

导入方式:

```python
import random
```

### random() randrange() randint()

- random(): 随机生成 0 到 1 的小数（包含0，不包含1）
- randrange(): 在范围内产生随机数，参数 start, stop, step
- randint(): 在a和b之间（包含a和b）随机生成一个整数

示例:

```python
import random

print(random.random())
print(random.randrange(2, 10, 2))
print(random.randint(1, 10))
```

### choice() choices() sample() shuffle()

- choice(): 随机选择一个序列中元素，返回该元素
- choices(): 随机选择多个序列中的元素，返回列表，k值指定选择次数（可重复）
- sample(): 随机抽取指定数量的元素，返回列表，不重复，k值不能大于序列长度
- shuffle(): 打乱列表元素顺序（原地修改）

示例:

```python
import random

lst = list(range(5))
print(random.choice(lst))
print(random.choices(lst, k=5))
print(random.sample(lst, k=5))

lst2 = lst.copy()
random.shuffle(lst2)
print(lst2)
```

### getstate() setstate()

- getstate(): 获取当前随机数生成器的内部状态
- setstate(): 设置随机数生成器的状态，使用之前的随机数状态可以重现随机数序列

示例:

```python
import random

# 保存当前状态
state = random.getstate()

# 生成一些随机数
print(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

# 恢复状态，重现相同的随机数序列
random.setstate(state)
print(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
```

## re 模块

正则表达式操作。

导入方式:

```python
import re
```

示例:

```python
import re
text = 'abc:bca:defg'
print(re.findall(r'[a-zA-Z]+', text))
```

## 网址状态码规则

HTTP 状态码分类：

- 100-299: OK，表示成功，没有问题
- 300-399: 默认 Python 会自动帮忙处理重定向方面的问题
- 400-599: 表示响应出了问题
  - 400-499: 错误来自客户端
    - 400: 包含语法错误，请求无法被服务器理解
    - 401: 需要人工验证
    - 403: 请求被拒绝，禁止访问
    - 404: 找不到页面
  - 500-599: 错误来自服务端

## urllib.parse 模块

URL 解析和处理。

导入方式:

```python
import urllib.parse
```

示例:

```python
import urllib.parse
params = {'key': 'value', 'name': 'test'}
print(urllib.parse.urlencode(params))
```

## urllib.request 模块

网络请求操作。

导入方式:

```python
import urllib.request
```

示例:

```python
import urllib.request
response = urllib.request.urlopen('http://example.com')
print(response.read().decode('utf-8'))
```

## os 模块

操作系统接口。

导入方式:

```python
import os
```

示例:

```python
import os
print('当前工作目录:', os.getcwd())
print('路径分隔符:', repr(os.sep))
print('系统名称:', os.name)
```

## sys 模块

系统相关的参数和函数。

导入方式:

```python
import sys
```

示例:

```python
import sys
print('Python 路径:', sys.path)
print('Python 版本:', sys.version)
print('命令行参数:', sys.argv)
```

## shutil 模块

高级文件操作。

导入方式:

```python
import shutil
```

示例:

```python
import shutil
# 删除文件夹及其内容
# shutil.rmtree('folder_to_delete')
```

## multiprocessing 模块

进程池和多进程操作。

导入方式:

```python
import multiprocessing
```

示例:

```python
import multiprocessing
import os

def worker(num):
    print(f'进程 {num} 正在运行，PID: {os.getpid()}')

if __name__ == '__main__':
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
```

## queue 模块

队列数据结构。

导入方式:

```python
import queue
```

示例:

```python
import queue

q = queue.Queue()
q.put('item1')
q.put('item2')
print(q.get())  # 输出: item1
print(q.get())  # 输出: item2
```

## threading 模块

多线程操作。

导入方式:

```python
import threading
```

示例:

```python
import threading
import time

def worker():
    print(f'线程 {threading.current_thread().name} 开始')
    time.sleep(2)
    print(f'线程 {threading.current_thread().name} 结束')

threads = []
for i in range(3):
    t = threading.Thread(target=worker, name=f'Thread-{i}')
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```
