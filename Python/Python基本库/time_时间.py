"""time  模块"""
import time
import os


'''
1.和时间有关

导入方式:
    import time
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.sleep()

sleep()  休眠一段时间
'''

print('2.')
print('——————————————————————————————————————————————————')

time1 = time.perf_counter()
print('1.', time.perf_counter() - time1)

print('——————————————————————————————————————————————————')
print('\n')


'''
3.time() time_ns() perf_counter()

计时
time(): 返回当前浮点数秒数时间
time_ns(): 返回当前时间，整数，精度0.000000100，单位纳秒
perf_counter(): CPU运行时间，浮点数秒数，高精度
'''

print('3.')
print('——————————————————————————————————————————————————')

time1 = time.perf_counter()
print('1.', time.time())
print('2.', time.time_ns())
print('3.', time.perf_counter() - time1)

print('——————————————————————————————————————————————————')
print('\n')


'''
4.gmtime() localtime() ctime() mktime() strftime() strptime()

浮点数秒数转换
gmtime()  返回格林时间，或把浮点数秒数转换成格林时间
localtime()  返回本地时间，或把浮点数秒数转换成本地时间
ctime()  将浮点数秒数转换成字符串的本地时间
mktime()  把元组转换成无精度的浮点数秒数
strftime()  格式化浮点数秒数时间
strptime()  按照格式把字符串时间转换成 time.struct_time

转换后返回的对象的可使用方法:
    以下返回值都是整数
    tm_year: 年: 正常值
    tm_mon: 月: 取值区间 [1 - 31]
    tm_mday: 日: 取值区间 [1 - 31]
    tm_hour: 时: 取值区间 [0 - 23]
    tm_min: 分: 取值区间 [0 - 59]
    tm_sec: 秒: 取值区间 [0 - 61]  # ？？？
    tm_wday: 星期: 取值区间 [0 - 6]
    tm_yday: 从一月一日起算过了几天: 取值区间 [1 - 366]
    tm_isdst: 夏令时标识符，实行为正，不实行为 0，不清楚为负
'''

print('4.')
print('——————————————————————————————————————————————————')

a = time.localtime(os.path.getctime(os.curdir))
print('1.', os.path.abspath(os.curdir) + '\n' + str(a))
print(a.tm_year, '年', a.tm_mon, '月', a.tm_mday, '日',
      '星期', a.tm_wday + 1)
print(a.tm_hour, ':', a.tm_min, ':', a.tm_sec, sep='')
print('2.', time.ctime(time.time()))
print('3.', time.mktime(time.localtime()))
a = time.strftime('%Y/%m/%d %H:%M:%S')
print('4.', a)
print('5.', time.strptime(a, '%Y/%m/%d %H:%M:%S'))

print('——————————————————————————————————————————————————')
print('\n')
