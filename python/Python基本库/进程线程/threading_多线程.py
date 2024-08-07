"""threading  模块"""
import threading


'''
1.多线程

导入方式:
    import threading

GIL: Global Interpreter Lock  全局解释器锁
Python 使用多线程默认加上这把锁，但当计算量大时会自动释放这把锁
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.enumerate()
current_thread() currentThread()
active_count() activeCount()

enumerate()  以列表返回还在运行的线程
current_thread()  返回当前线程对象
currentThread()  同 current_thread()
active_count()  当前还在运行的线程数
activeCount()  同 active_count()
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
3.Thread()

创建线程
参数:
    group:
    target: 启动后调用的对象
    name: 线程名
    args: 调用对象时传入的位置参数
    kwargs: 调用对象时传入的关键字参数
    deamon: 守护线程，启用后主进程/线程死亡，此线程死亡
deamon  布尔值，守护线程
start()  启动线程
setDeamon()  设置守护线程
setName()  命名
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
4.Lock()

锁
Lock()  创建一把锁
以上共同方法属性:
    acquire()  请求加锁，如果已上锁则等待锁被释放
    release()  释放锁
'''

print('4.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')
