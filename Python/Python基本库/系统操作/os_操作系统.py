"""os  模块"""
import os


'''
1.常用于文件操作的模块

导入方式:
    import os

目录:
    2-4  文件处理
    5-n  系统操作
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.curdir pardir sep linesep name

字符串变量
curdir  当前系统指代当前目录使用的字符串
pardir  当前系统指代上一级目录使用的字符串
sep  当前系统的路径分隔符
linesep  当前系统的行分隔符
name  当前系统名字
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.', repr(os.curdir))
print('2.', repr(os.pardir))
print('3.', repr(os.sep))
print('4.', repr(os.linesep))
print('5.', repr(os.name))

print('——————————————————————————————————————————————————')
print('\n')


'''
3.getcwd() chdir() listdir()
mkdir() makedirs()
remove() rmdir() removedirs() rename()
startfile()

操作文件
getcwd()  获取当前工作目录
chdir()  改变当前工作目录
listdir()  目录下的文件
mkdir()  创建文件夹，已存在则报错
makedirs()  创建多层文件夹，已存在则报错
remove()  删除文件
rmdir()  删除文件夹
removedirs() 删除多层文件夹
rename()  重命名，填两参数 old 和 new
startfile()  打开文件
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.', os.getcwd())

print('——————————————————————————————————————————————————')
print('\n')


'''
4.path

os.path
可选方法:
    # 以下参数都是路径
    abspath(): 文件的绝对路径
    realpath(): 路径的真实路径
    split(): 路径分割成目录路径和最后一项
    basename(): 返回路径中最后一项 E:\\a.txt -- a.txt
    dirname(): 返回目录路径 E:\\a.txt -- E:\\
    join(): 拼接目录路径和 文件或目录
    splitext(): 分割文件和拓展名
    exists(): 文件或目录是否存在
    isabs(): 是否是绝对路径的格式
    isdir(): 是否是存在的目录
    isfile(): 是否是存在的文件
    islink(): 是否是链接（Windows操作系统是快捷方式？）
    ismount(): 是否是挂载点（C盘 D盘，C:\\ D:\\）
    somefile(): 两个路径是否指向同一个文件
    getsize(): 获取文件字节大小
    getctime(): 获取文件创建时间
    getatime(): 获取文件最近访问时间
    getmtime(): 获取文件最近修改时间
    stat(): 文件的属性，大小，创建时间等等
'''

print('4.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
5.environ

一些变量
environ  环境变量
'''

print('5.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
6.system()

系统相关
system()  调用系统的 shell 命令（像是 Windows 的 <运行>）
'''

print('6.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
7.cpu_count() getpid() getppid()
fork()

处理器，进程，线程，协程
cpu_count()  逻辑处理器数
getpid()  当前进程的标识
getppid()  父进程标识

fork()  Linux 操作系统下创建进程（多任务）
    返回一个 int 值，
    小于0表示失败，
    等于0表示当前进程为子进程，
    大于0表示当前进程为父进程，值为创建的进程的标识
'''

print('7.')
print('——————————————————————————————————————————————————')

print('1.', os.cpu_count())
print('2.', os.getpid(), os.getppid())

print('——————————————————————————————————————————————————')
print('\n')
