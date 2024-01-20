"""if elif else  条件判断语句"""


'''
1.用于条件判断的语句有 if elif else

判断时判断的是对象的布尔值，True 或 False
其包含的内容以一层缩进缩进表示，也就是四个空格

if:
    判断右侧条件是否成立
    条件成立时执行其包含的代码块
    不成立时寻找下一条条件判断语句（elif 或 else）
elif:
    当上一条条件判断语句不成立时开始条件判断
    条件成立时执行其包含的代码块
    不成立时寻找下一条条件判断语句（elif 或 else）
else:
    当以上所有条件判断都不成立时执行，语句后面不填条件，紧跟着冒号

if 可以简写，写成条件表达式:
    格式:
        print('1 < 2 成立') if 1 < 2 else print('1 < 2 不成立')
    表达式过长时为了看着直观，推荐使用括号换行

if 语句支持嵌套
'''

print('1.')
print('——————————————————————————————————————————————————')

a = 10
if a:
    print('1.', a)
print('2.', a if a else False)
if not a:
    pass
elif a == 5:
    pass
else:
    if a == 10:
        print('3.', a)
    else:
        pass
(print('not a 成立') if not a else
 print('a == 5 成立') if a == 5 else
 print('4.', '条件表达式') if a == 10 else
 print('a == 10 不成立'))

print('——————————————————————————————————————————————————')
print('\n')
