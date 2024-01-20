"""str  字符串"""


r'''
1.\033[0;35m ... \033[m

字体颜色
用法:
    开头: \033[0;30m
    结尾: \033[m
    新的开头会覆盖原有的开头

    分号后面的数字 30 到 37 是颜色，40 到 47 是方块颜色:
        30 黑，31 红，32 绿，33 黄，34 蓝，35 紫，36 偏绿的蓝，37 灰
        40 - 47 个位数对应的颜色与 30 - 37 一致

    分号前的数字:
        0  ...
        21  下划线
        100  灰色背景
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.', '\033[21;34m哈哈哈哈\033[m')
print('2.', '\033[100;30m哈哈哈哈\033[m')

print('——————————————————————————————————————————————————')
print('\n')
