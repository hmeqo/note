"""str  字符串"""


r'''
1.字符串，不可变序列

文本，不被当成代码执行，只原样输出
字符串是被单引号或双引号包含的
成对的单双引号同时出现时，互相包含使用
多个成对的单双引号再加上一个单双引号，可以使用转义字符反斜杠 \ 进行转义
多行长字符串可使用三个单引号或三个双引号

字符串支持使用下标索引和切片操作

字符串可以使用加号和乘号
加号，将两个字符串拼接起来
乘号，将这串字符串输出几遍
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.', 'I love China.')
print('2.', "I love China.")
print('3.', "Let's go!")
print('4.', '"Life is short, you need Python."')
print('5.', '"Life is short, let\'s learn Python"')
print('6.', "I love Python, \nprint('Hello World')")
print('7.', '''one
two
three''')
print('8.', '520' + '1314')
print('9.', '把我输出三遍！\n' * 3)
s1 = '12345'
print('10.', s1[2])
print('11.', s1[::-1])

print('——————————————————————————————————————————————————')
print('\n')


r'''
2.\

转义字符
可选后缀参数:
    \\  反斜杠
    \'  单引号
    \"  双引号
    \t  制表符
    \n  换行
    \r  回退指针至开头
    \b  回退一格
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.', '反斜杠 \\')
print('2.', '\'单引号\'')
print('3.', "\"双引号\"")
print('4.', "'\t'")
print('5.', "'\n'")
print('6.', '\nbanana\r apple')
print('7.', 'banana\b apple')

print('——————————————————————————————————————————————————')
print('\n')


'''
3.
不希望转义字符起作用可以使用转义字符对转义字符转义或使用原始字符串

转义字符转义，只需要两个转义字符就行
原始字符，不希望转义字符起作用，只想原样输出，则在字符串前加上 r
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.', 'D:\\three\\two\\one\\now')
print('1.', r'D:\three\two\one\now')

print('——————————————————————————————————————————————————')
print('\n')


'''
4.upper() lower() casefold() swapcase() title() capitalize()

字符串的大小写转换
upper()  全部为大写
lower()  全部为小写，只能转换英文字母
casefold()  全部为小写，和 lower() 的区别是 casefold() 可以转换一些其他的字符，如德语
swapcase()  大小写互换，大写变小写，小写变大写
title()  单词开头大写，其余小写
capitalize()  第一个字母大写，其余小写
'''

print('4.')
print('——————————————————————————————————————————————————')

s1 = 'I love China'
print('1.', s1.upper())
print('2.', s1.lower())
print('3.', s1.casefold())
print('4.', s1.swapcase())
print('5.', s1.title())
print('6.', s1.capitalize())

print('——————————————————————————————————————————————————')
print('\n')


'''
5.center() ljust() rjust() zfill()

字符串的对齐
center()  居中对齐，两侧填充
ljust()  左对齐，右侧填充
rjust()  右对齐，左侧填充
以上有两个参数，参数一总宽度，参数二填充什么字符，默认填充空格
zfill()  右对齐，左侧在正负号后面填充0。一个参数，总宽度
'''

print('5.')
print('——————————————————————————————————————————————————')

s1 = 'I love China'
print('1.', s1.center(5), len(s1))
print('2.', s1.center(20))
print('3.', s1.center(20, '='))
print('4.', s1.ljust(20))
print('5.', s1.rjust(20))
print('6.', s1.zfill(20))
s1 = '-88995'
print('7.', s1.zfill(10))

print('——————————————————————————————————————————————————')
print('\n')


'''
6.count() find() rfind() index() rindex()

字符串的查找
都是可以传入第二第三个参数指定开始和结束的
count()  该字符在字符串中出现的次数
find()  从左往右找该字符出现的位置，找到抛出索引，不管字符有多少个，只抛出一次，没找到抛出 -1
rfind()  从右往左找，其他同 find()
index()  从左往右找，没找到抛出异常，其他同 find()
rindex()  从右往左找，其他同 index()
'''

print('6.')
print('——————————————————————————————————————————————————')

s1 = 'I love China'
print('1.', s1.count(' '))
print('2.', s1.find('i'))
print('3.', s1.rfind('l', 3, 5))
print('4.', s1.index('o'))
print('5.', s1.rindex('a'))

print('——————————————————————————————————————————————————')
print('\n')


'''
7.expandtabs() replace() translate()

字符串的替换
expandtabs()  把制表符 Tab 替换成空格，参数里填整数，Tab换成几个空格
replace()  把字符串中的某个字符（第一个参数）替换成某个字符（第二个参数），
    替换几次（第三个参数），默认替换全部符合的字符
translate()  按照一个表格进行替换

表格是一个字典，存储了字符十进制编码和如果匹配要替换的十进制编码
所以我觉得 translate() 是把字符准换成十进制编码再与表格中的编码对比

用 str 的静态方法 makertrans() 创建表格需要两个参数，字典的键和值，
它还支持第三个参数，忽略某段字符串
就是把表格字典中对应字符的编码的值设置为 ''，匹配的时候不就把它删除了嘛
'''

print('7.')
print('——————————————————————————————————————————————————')

s1 = """I love China
    I love...
    I..."""
s1 = s1.expandtabs(4)
print('1.', s1)
print('2.', s1.replace('.', '?'))
print('3.', 'I love China'.translate(str.maketrans('abCDef', '123456', 'love')))
print('4.', 'I love Chine'.translate({ord('C'): ord('5')}))

print('——————————————————————————————————————————————————')
print('\n')


'''
8.startswith() endswith() isupper() islower() istitle() isalpha() isspace()
isprintable() isdecimal() isdigit() isnumeric() isalnum() isidentifier()
isascii()

字符串的判断，返回值都是布尔类型
startswith()  一段字符串（参数一）是否在一段字符串的开头，可以指定开始（参数二）和结束（参数三）
endswith()  一段字符串（参数一）是否在一段字符串的结尾，可以指定开始和结束
isupper()  字符串中的英文字母是否全部为大写
islower()  字符串中的英文字母是否全部为小写
istitle()  字符串中的英文字母单词是否全部为开头大写，其余小写
isalpha()  是否全部由英文字母（中文字符也算，解决办法：先编码再判断）组成
isspace()  是否全部由空白字符组成
isprintable()  是否全是由可打印字符组成
isdecimal()  是否全是由十进制数字组成
isdigit()  是否全是由数字组成
isnumeric()  是否全是由数字组成（罗马数字中文数字中文繁体字数字什么的都算）
isalnum()  isalpha() 和 isnumeric() 的集合体
isidentifier()  是否是全合法字符，字母开头，不能有空格，可以用下划线，可以用数字
isascii()  是否是ASCII格式的字符
'''

print('8.')
print('——————————————————————————————————————————————————')

s1 = 'I love China'
print('1.', s1.startswith('I'))
print('2.', s1.startswith('C'))
print('3.', s1.startswith('love', 2, 7))
print('4.', s1.startswith(('C', 'l', 'I')))
print('5.', s1.endswith('h'))
print('6.', s1.endswith('Ch', 0, 9))
print('7.', s1.isupper())
print('8.', s1.upper().isupper())
print('9.', s1.islower())
print('10.', s1.isalpha())
print('11.', s1.replace(' ', '').isalpha())
s1 = 'IloveChina我爱中国'
print('12.', s1.isalpha())
print('13.', s1.encode().isalpha())
s1 = '\t \n'
print('14.', s1.isspace())
s1 = ''
print('15.', s1.isspace())
s1 = 'I love Python'
print('16.', s1.isprintable())
s1 = 'I love Python\n'
print('17.', s1.isprintable())
s1 = '123'
print('18.', s1.isdecimal())
print(s1.isdigit())
print(s1.isnumeric())
s1 = '102²'
print('19.', s1.isdecimal())
print(s1.isdigit())
print(s1.isnumeric())
s1 = '2²一二三壹贰叁ⅠⅡⅢ'
print('20.', s1.isdecimal())
print(s1.isdigit())
print(s1.isnumeric())
s1 = 'abcdefg2²一二三壹贰叁ⅠⅡⅢ'
print('21.', s1.isalnum())
s1 = 'is_identifier_123'
print('22.', s1.isidentifier())
s1 = 'is_identifier_123.1'
print('23.', s1.isidentifier())
s1 = '123_is_identifier'
print('24.', s1.isidentifier())
print('25.', s1.isascii())
s1 = '123_is_ascii吗'
print('26.', s1.isascii())

print('——————————————————————————————————————————————————')
print('\n')


'''
9.encode()

编码格式
encode()  按编码将字符串转换成字节
'''

print('9.')
print('——————————————————————————————————————————————————')

s1 = 'I love China我爱中国'
print('1.', s1.encode())

print('——————————————————————————————————————————————————')
print('\n')


'''
10.% format() f

格式化字符串
%  在字符串中使用，对字符串中的 % 格式化，字符串中的 % 后缀格式化方式，字符串外的 % 后填入变量
    格式: '%s%s' % ('格式化', '字符串')
    后缀可选参数（必填其一）:
        %c  按编码转换成一个字符串，参数类型 <int> <char>
        %s  字符串，任意参数，通过 str() 函数转换成字符串
        %i  十进制整数，参数是一个数字，不复杂
        %f  浮点数
        %r  以读取的方式得到字符串
        %d  十进制整数，和 %i 功能一样
        %u  无符号的十进制整数
        %o  八进制整数
        %x  十六进制整数
        %e  科学计数法（小写 e）
        %E  科学计数法（大写 E）
        %g  整数部分长度超过6位时使用科学计数法 %e，整数部分未超过时只保留6位数
        %G  和 %g 相似，符号是大写的 E
        可选参数:
            %2s  2 左填充，超过字符长度按原字符输出
            %2.3s  .3 保留几个字符（符号为 f 时，保留几位小数）
format()  在字符串末尾使用，对字符串中的 {} 格式化，{} 中可选的填入格式化方式，括号中填入变量
    格式: '{}{}'.format('格式化', '字符串')
        '{fmt}'.format(fmt='format')
    可选参数:
        {0}  0 索引，在括号中的索引，不填默认从左到右。一个不填，其他也不能填
        {key}  键，在 () 中定义键值对
        
        以冒号（:）分割以上和以下
        [[fill]align][sign][#][O][width][grouping_option][.precision][type]
        [[fill]align]: 填充
            {0:10s}  默认 <
            {0: <10s}  < 左填充，相当于 ''.ljust(10, ' ')
            {0:1>10s}  > 右填充，相当于 ''.rjust(10, '1')
            {0: ^10s}  ^ 居中填充，相当于 ''.center(10, ' ')
            {0:010d}  0 符号后填充0，相当于 ''.zfill(10)。只对数字有效
            {0:0=10d}  0= 作用和 0 大致相同，但可以改变填充的数字
        [sign]: 数值前添加符号
            {0:+}  正数添加正号
            {0:-}  默认行为
            {0: }  正数添加空格
        [#]: [type] 设置进制类型是可用，以0加上符号作为前缀
            {0:#b}  输出 0b...
            {0:#o}  输出 0o...
            {0:#x}  输出 0x...
        [width]: 填充宽度
            {0:10s}  10 为 [[fill]align] 提供宽度
        [grouping_option]: 数字千分位分隔符
            {0:,}  千分位分隔符是逗号
            {0:_}  千分位分隔符是空格
        [.precision]: 精度，整数不能用，对于非数字类型，限定的是字段大小
            对于 'g' 'G' 表示小数点前后总共显示多少位
            {0:10.3s}  .3 保留几个字符（符号为 f 时保留几位小数）
        [type]: 类型
            {:s}  字符串
            {:f}  浮点数，定点表示法，不是数用 'nan' 标识，无穷用 'inf' 标识，默认精度 6
            {:F}  定点表示法，和 'F' 类似，标识为大写
            {:e}  科学计数法，符号为e
            {:E}  科学计数法，符号为E
            {:g}  整数部分长度超过6位时使用科学计数法 %e，整数部分未超过时只保留6位数
            {:G}  和 %g 相似，符号是大写的 E
            {:%}  以百分比输出，乘以一百并附带百分号
            {:b}  整数参数以二进制输出
            {:o}  整数参数以八进制输出
            {:d}  整数参数以十进制输出
            {:x}  整数参数以十六进制输出
            {:X}  整数参数以十六进制输出
            {:c}  十进制编码以 Unicode 字符的形式输出
            {:n}  自动，它会使用当前语言环境设置的分隔符插入到合适的位置
            {:}  自动
f  在字符串开头使用，对字符串中的 {} 格式化，{} 中填入变量
    格式: f'{fmt}{'字符串'}'
    后缀可选参数:
        与 format 一致
想要输出格式化字符串占位符本身，再写一次就可以了，例如: '%%'  '{{}}'
'''

print('10.')
print('——————————————————————————————————————————————————')

s1 = '格式化'
print('1.', '%s%s' % (s1, '字符串'))
print('2.', '{0}{fmt}'.format(s1, fmt='字符串'))
print('3.', f"{s1}{'字符串'}")
print('4.', '%c' % ord('A'))
print('5.', '%c' % 0b1000001)
print('6.', '%i' % 123)
print('7.', '%f' % 1.23)
print('8.', '%20f' % 1.23)
print('9.', '%0.2f' % 1.23)
print('10.', '%d' % -2.2)
print('11.', '%u' % -2.2)
print('12.', '%o' % 30)
print('13.', '%x' % 30)
print('14.', '%e' % 100)
print('15.', '%E' % 100)
print('16.', '%g' % (1 * 10 ** 100))
print('17.', '%G' % (1 * 10 ** 100))
print('18.', '读取%r' % '字符')
print('19.', '{{}}'.format())
print('20.', '%%' % ())
print('21.', '{:%<10s}'.format('12345'))
print('22.', '{:&>10s}'.format('12345'))
print('23.', '{:*^10s}'.format('12345'))
print('24.', '{:010d}'.format(12345))
print('25.', '{:9=10d}'.format(12345))
print('26.', '{:9=+10d}'.format(12345))
print('27.', '{:+10e}'.format(12345))
print('28.', '{:}{:}'.format(123, '123'))
print('29.', '{:f}'.format(123.5634))
print('30.', '{:-,}'.format(123563.4))
print('30.', '{:-_}'.format(123563.4))

print('——————————————————————————————————————————————————')
print('\n')


'''
11.strip() lstrip() rstrip() removeprefix() removesuffix()

截取
strip()  剔除开头和末尾（左右两侧）的空格
    有一个可选参数，传入字符串，匹配删除字符串中的字符
lstrip()  剔除开头（左侧）的空格，参数同上
rstrip()  剔除末尾（右侧）的空格，参数同上
removeprefix()  剔除前缀字符串
removesuffix()  剔除后缀字符串
'''

print('11.')
print('——————————————————————————————————————————————————')

s1 = '  I love China  '
print('1.', '%r' % s1.strip())
print('2.', '%r' % s1.lstrip())
print('3.', '%r' % s1.rstrip())
s1 = 'Hello world.com'
print('4.', '%r' % s1.strip('Hel com'))
print('5.', '%r' % s1.removeprefix('Hello '))
print('6.', '%r' % s1.removesuffix('.com'))

print('——————————————————————————————————————————————————')
print('\n')


'''
12.partition() rpartition() split() rsplit() splitlines() join()

分割和拼接
partition()  以指定字符为分隔符分割一次字符串，以元组返回其之前，该字符，其之后
rpartition()  从右往左分割，作用和参数同 partition()
split()  以指定字符为分隔符分割字符串，返回列表，可以指定最大分割次数
rsplit()  从右往左分割，作用和参数同 split()
splitlines()  分割换行符，按行分割，作用同 split()，一个可选参数，是否保留换行符
join()  传入的字符串元素的迭代对象按.join()前的字符串拼接起来
'''

print('12.')
print('——————————————————————————————————————————————————')

s1 = 'I love China'
print('1.', s1.partition(' '))
print('2.', s1.rpartition(' '))
print('3.', s1.split(' '))
print('4.', s1.split(' ', 1))
print('5.', s1.rsplit(' ', 1))
s1 = 'I\nlove\r\nChina'
print('6.', s1.splitlines())
print('7.', s1.splitlines(True))
s1 = s1.splitlines()
print('8.', ' '.join(s1))

print('——————————————————————————————————————————————————')
print('\n')
