"""pickle  模块"""
import pickle


'''
1.转换二进制数据存储的模块

导入方式:
    import pickle
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.dump() load()

转换成二进制存储和载入
dump()  填入对象和文件，把对象转换成二进制存入文件
load()  加载二进制，参数填文件
'''

print('2.')
print('——————————————————————————————————————————————————')

a = [123, 3.14, 'pickle', ['pickle']]
with open('pickle.pkl', 'wb') as file:
    print('1.', pickle.dump(a, file))

with open('pickle.pkl', 'rb') as file:
    print('2.', pickle.load(file))

print('——————————————————————————————————————————————————')
print('\n')
