"""requests  模块"""
import requests


'''
1.向网址爬取数据的模块

导入方式:
    import requests
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.get() post()

request(): 构造请求，支撑以下方法的基础方法
get(): 获取网页，对应html中的 GET
post(): 提交post请求，对应html中的 POST
put(): 提交put请求，对应html中的 PUT
patch(): 提交局部修改请求，对应html中的 PATCH
delete(): 提交删除请求，对应html中的 DELETE
head(): 获取网页头部，对应html中的 HEAD

以上返回的对象可用的方法属性:
    text: content 转字符串文本
    content: 内容，字节类型
    encoding: content 转换为 text 时使用的编码类型
'''

print('2.')
print('——————————————————————————————————————————————————')

url = 'http://www.baidu.com/'
response = requests.get(url)
response.encoding = 'UTF-8'
print('1.', response.text)
print('2.', response.content)

print('——————————————————————————————————————————————————')
print('\n')
