"""nonlocal  声明上层变量"""


'''
1.在嵌套函数或方法中声明一个上一层函数或方法的变量
格式:
    nonlocal variabel
'''

print('1.')
print('——————————————————————————————————————————————————')


def a():

    x = 1
    print('a start, x=', x)

    def b():

        x = 2
        print('b start, x=', x)

        def c():

            nonlocal x
            x = 3
            return None
        
        c()
        print('b end, x=', x)
        return None
    
    b()
    print('a end, x=', x)
    return None


print('1.')
a()

print('——————————————————————————————————————————————————')
print('\n')
