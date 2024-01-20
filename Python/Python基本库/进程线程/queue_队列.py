"""queue  模块"""
import queue


'''
1.队列

导入方式:
    import queue

一般用在多线程，多进程用 queues 模块或 multiprocessing.Queue
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.Queue() LifoQueue() PriorityQueue()

队列
Queue()  先进先出队列
LifoQueue()  后进先出队列
PriorityQueue()  优先级队列
以上共同的参数:
    maxsize  队列最大长度
以上共同的方法属性:
    put()  向队列放入一个值，如果队列已满则等待队列有空位
        参数:
            obj: 对象
            block: 如果队列已满，是否阻塞等待
            timeout: 超时。设置后如果超时了，那么报出异常 queue.Full
    get()  向队列取出一个值，如果队列为空则等待队列有值
        参数:
            obj: 对象
            block: 如果队列为空，是否阻塞等待
            timeout: 超时。设置后如果超时了，那么报出异常 queue.Empty
    psize()  当前队列长度
    full()  队列是否已满
    empty()  队列是否为空
    task_done()  在每次 get() 成功后使用，表示已获取到了值
    join()  阻塞，等待任务完成(并不是队列为空)
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')
