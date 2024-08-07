"""scrapy  Scripts模块"""


'''
1.爬虫

使用方式:
    cmd 在命令行中使用
格式:
    scrapy <command> [options] [args]
可用命令:
    <command> startproject  创建一个项目文件
        [args]  项目文件名
    <command> crawl  在项目文件下使用，爬取
        [args]  自定义的爬虫类的 name
            [options]  -o <导出的文件名> -t json
                -o 导出, -t 导出形式
    <command> shell  用 shell 环境打开网址
        [args] 网址, 防止报错需要用双引号包围
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.教程

首先创建项目文件夹
# 以下出现被 <> 包围的代码表示自定义内容（不需要把 <> 添上）
步骤:
    # 在命令行中
    # 转到任意目录下
    >>> cd Desktop
    # 在该目录下创建名为 name （自定义）的项目文件夹
    >>> scrapy startproject <name>
之后在项目文件夹中打开和该文件夹同名的文件夹中的文件 items.py
修改其中的类（类名是项目文件夹名加Item）:
    class TutorialItem(scrapy.item):

        # define the fields for your item here like:
        # name = scrapy.Field()
        # pass 改成以下内容
        url = scrapy.Field()
在 items.py 同级目录下的 spider 文件夹下添加 .py 文件，写入信息:
    import scrapy
    
    from tutorial.items import TutorialItem


    class TuTorialScrapy(scrapy.Spider):  # 要求继承 scrapy.Spider 类
        
        # 这只爬虫的名字
        name = 'tutorial'
        # 列表中填入域名，使爬虫不会爬到其他地方
        allowed_domains = ['python.org']
        # 填入需要爬取的网页地址
        start_urls = ['https://python.rog']
        
        def parse(self, response):
            
            # 得到的数据传入 response，之后想用来做什么自定义
            item = TutorialItem()
            item[url] = response.url
            return item
最后在命令行中，第一层目录下（scrapy.cfg 文件同级目录）输入如下内容:
    # 将返回值导出至文件
    # name 是爬虫类的 name 属性的值
    # -o 导出
    # filename 是文件名
    # json 导出形式
    >>> scrapy crawl <name> -o <filename.json> -t json
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
3.shell 环境

可使用属性:
    response  响应
        url  网址
        body  源代码
    sel  就是 scrapy.selector.Selector(response)
        xpath()  映射到 sel.selector.xpath()，根据 xpath 语言筛选
            参数:
                : 字符串
            返回对象的可用方法属性:
                extract()  变成字符串返回
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')
