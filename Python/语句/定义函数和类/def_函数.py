"""def  函数"""


'''
1.定义一个函数
格式:
    def func_name(*arg, **keywords):

        pass
    
    命名约定以小写字母和下划线组成 或 小驼峰法
        小驼峰法: 首字母小写之后的单词首字母大写，单词间不使用下划线隔开
    
    设置函数形参的默认值:
        a=1  不传入与 a 匹配的参数时，a默认为1
        a=...  这三个点是 ellipsis 类的实例，表示省略
    
    形参的一种特殊写法:
        arg: int = ...  告诉说这只接收 int 类型的数据
            : 号右侧 = 号左侧是信息，填什么都可以
            = 右侧是默认值

    位置形参，例: func_name(1, 2, 3)
    关键字形参，例: func_name(a=1, b=2, c=3)
    *arg  个数可变的位置形参，把传入的位置形参打包成一个元组
    **keywords  个数可变的关键字形参，把传入的关键字形参打包成字典
    关键字形参必须在位置形参之后
    
    对序列使用会将其拆分，例如:
        *(1, 2, 3) -- 1, 2, 3
        **{'a': 1, 'b': 2, 'c': 3} -- a=1, b=2, c=3
        可以将解包后的值放在函数调用时的括号内，也可以放在序列中
'''

print('1.')
print('——————————————————————————————————————————————————')


def func_name(*args, **kwargs):

    for i in args:
        print(i)
    for i in kwargs:
        print(i, kwargs[i])
    
    def n(*args, **kwargs):

        print(*args, kwargs, **{'end': ' wooh\n'})

    n(*args, **kwargs)


print('1.')
func_name(1, 0, 3, a='我是a', b='b', r=4)

print('——————————————————————————————————————————————————')
print('\n')


'''
2.闭包
'''

print('2.')
print('——————————————————————————————————————————————————')


def func_name(a):

    def inner_func(*args, **kwargs):

        return a, args, kwargs
    
    return inner_func


print('1.', func_name(1))

print('——————————————————————————————————————————————————')
print('\n')
