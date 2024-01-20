"""re  模块"""
import re


'''
1.正则表达式

导入方式:
    import re
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.ASCII DOTALL IGNORECASS LOCALE MULTILINE VERBOSE

标志
填入方法参数中的 flags
ASCII  A 使一些转义字符只匹配 ASCII 字符
DOTALL  S 使通配符匹配所有字符
IGNORECASS  I 匹配时不区分大小写
LOCALE  L 支持当前的语言（区域）设置
MULTILINE  M 多行匹配
VERBOSE  E 启用详细的正则表达式（可以换行啦）

填写时记得加上模块名，例: re.ASCII
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
3.compile()

编译表达式
参数:
    pattern: 模式
    flags=0: 标志

返回对象的类型 <class 're.Pattern'>
返回的对象的可使用方法属性:
    match()  查找
    search()  查找
    findall()  查找
    以上共同参数:
        string: 字符串
        pos: 起始位置
        endpos: 结束位置
'''

print('3.')
print('——————————————————————————————————————————————————')

a = re.compile(r'[abc]')
print('1.', a)
print('2.', a.search('3c'))

print('——————————————————————————————————————————————————')
print('\n')


'''
4.match search() findall()

匹配查找字符串
match()  只匹配一次，未匹配成功不再进行匹配，返回 None
search()  查找，多次匹配，成功返回包含索引范围和匹配内容的对象
    返回对象的类型 <class 're.Match'>
    匹配成功返回的对象的可使用方法属性:
        group()  组，匹配到的内容
            参数:
                ...: 第几组表达式匹配到的内容
        span()  跨度，索引范围
        start()  起始索引
        end()  终止索引
findall()  找到所有匹配的字符，打包成列表返回
    如果表达式中有子组，只保留子组匹配，多个子组则打包成元组返回
    不想子组的内容被单独返回就使用拓展语法 (?:)
finditer()  类似 findall()，返回一个可迭代器，每次迭代提取一个值
以上共同参数:
    pattern: 模式
    string: 字符串
    flags=0: 标志
'''

print('4.')
print('——————————————————————————————————————————————————')

text = 'abc:bca:defg'
print('1.', re.match(r'bc', text))
print('2.', re.search(r'bc', text))
print('3.', re.findall(r'[a-zA-Z]+', text))

print('——————————————————————————————————————————————————')
print('\n')


'''
5.sub() split()

使用正则操作字符串
sub()  匹配并替换
    参数:
        pattern: 模式
        repl: 替换成什么字符
        string: 字符串
        count: 次数
        flags=0: 标志
split()  分割
    参数:
        pattern: 模式
        string: 字符串
        maxsplit: 最大分割次数
        flags=0: 标志
'''

print('5.')
print('——————————————————————————————————————————————————')

text = '1abc2def3g4'
print('1.', re.sub(r'[a-zA-Z]+', '<word>', text))
print('2.', re.split(r'[a-zA-Z]+', text))

print('——————————————————————————————————————————————————')
print('\n')
