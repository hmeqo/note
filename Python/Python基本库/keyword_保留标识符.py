"""keyword  模块"""
import keyword


'''
1.与 Python 标识符有关

导入方式:
    import keyword
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.iskeyword()

判断是否是保留标识符
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.', keyword.iskeyword('if'))
print('2.', keyword.iskeyword('print'))
print('3.', keyword.iskeyword('is'))

print('——————————————————————————————————————————————————')
print('\n')


'''
3.kwlist

变量，所有的保留标识符
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.', keyword.kwlist)

print('——————————————————————————————————————————————————')
print('\n')
