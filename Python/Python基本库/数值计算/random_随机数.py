"""random  模块"""
import random


'''
1.随机数

导入方式:
    import random
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.random() randrange() randint()

random()  随机生成 0 到 1 的小数
randrange()  在范围内产生随机数，参数 start, stop, sep
randint()  在a和b(包含)之间随机生成一个整数
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.', random.random())
print('2.', random.randrange(2, 10, 2))
print('3.', random.randint(1, 10))

print('——————————————————————————————————————————————————')
print('\n')


'''
3.choice() choices() sample() shuffle()

choice()  随机选择一个序列中元素，返回值
choices()  随机选择多个序列中的元素，返回列表，k值指定次数
sample()  随机抽取一节元素，返回列表，不重复，k值不能大于序列长度
shuffle()  打乱列表元素顺序
'''

print('3.')
print('——————————————————————————————————————————————————')

lst = list(range(5))
print('1.', random.choice(lst))
print("2.", random.choices(lst, k=5))
print("3.", random.sample(lst, k=5))
lst2 = lst.copy()
random.shuffle(lst2)
print('4.', lst2)

print('——————————————————————————————————————————————————')
print('\n')


'''
4.getstate() setstate()

getstate()  获取当前随机数种子，可以使用 setstate(随机数种子) 实现重复随机数
setstate()  设置随机数种子，使用之前的随机数种子可以重复之前的随机数
'''

print('4.')
print('——————————————————————————————————————————————————')

x = random.getstate()
print('1.', random.randint(1, 10), random.randint(1, 10),
      random.randint(1, 10))
random.setstate(x)
print('2.', random.randint(1, 10), random.randint(1, 10),
      random.randint(1, 10))

print('——————————————————————————————————————————————————')
print('\n')
