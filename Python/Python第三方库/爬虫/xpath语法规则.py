"""xpath语法规则"""


'''
1.专用于过滤网页信息的语言？比用正则表达式专业

如下的网页代码:
    <div id="1">
        <a id="2">
        </a>
    </div>
    提取元素例子:
        '//div'  提取找到的整个 div 元素，即 <div ... 到 </div>（包括）
        '//div/a'  提取找到的的 div 中的整个 a 元素 ，即 <a ... 到 </a>
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.// /

路径表达
/: 根节点，节点分割符 (查找子代)
//: 任意位置 (查找后代)
.: 当前节点
..: 父级节点
@: 属性
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
3.* @*

通配符
*: 任意元素, 任意节点
@*: 任意属性
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
4.[]

谓语，使用中括号来限定元素，称为谓语
例:
    //a[n]  n为大于零的整数，代表子元素排在第n个位置的<a>元素
    //a[last()]  last() 代表子元素排在最后个位置的<a>元素
    //a[last()-]  代表倒数第二个
    //a[position()<3]  位置序号小于3，前两个，xpath中的序列是从1开始
    //a[@href]  拥有href的<a>元素
    //a[@href="www.baidu.com"]  href属性值为"www.baidu.com"的元素
    //book[@price>2]  price值大于2的<book>元素
'''

print('4.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
5.|

多个路径
|: 使用|连接两个表达式，可以进行 或 匹配
'''

print('5.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
6.contains(), starts-with(), ends-with(), upper-case(),
text(), last(), position(), node()

函数
contains(*string): 包含
starts-with(*string): 开头为
ends-with(*string): 结束为  # 不支持
upper-case(string): # 不支持
text(): 文本内容
last(): 最后一个位置
position(): 元素位置序号
node(): 任意子节点
'''

print('6.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')
