# scrapy

## 安装

```bash
pip install scrapy
```

## 导入模块

```python
import scrapy
```

## 属性

| 命令           | 描述          |
| -------------- | ------------- |
| `startproject` | 创建项目      |
| `crawl`        | 运行爬虫      |
| `shell`        | 进入shell环境 |

### 项目结构

创建项目后生成的目录结构：

```txt
project_name/
├── scrapy.cfg
└── project_name/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders/
        ├── __init__.py
```

### Spider 类

| 属性              | 描述           |
| ----------------- | -------------- |
| `name`            | 爬虫名称       |
| `allowed_domains` | 允许爬取的域名 |
| `start_urls`      | 起始URL列表    |

| 方法    | 描述     |
| ------- | -------- |
| `parse` | 解析响应 |

### 教程

首先创建项目文件夹

步骤:
    # 在命令行中
    # 转到任意目录下
    >>> cd Desktop
    # 在该目录下创建名为 name （自定义）的项目文件夹
    >>> scrapy startproject <name>
之后在项目文件夹中打开和该文件夹同名的文件夹中的文件 items.py
修改其中的类（类名是项目文件夹名加Item）:

修改其中的类（类名是项目文件夹名加Item）:

```python
class TutorialItem(scrapy.item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass 改成以下内容
    url = scrapy.Field()
```

在 items.py 同级目录下的 spider 文件夹下添加 .py 文件，写入信息:

```python
import scrapy
from tutorial.items import TutorialItem

class TuTorialScrapy(scrapy.Spider):  # 要求继承 scrapy.Spider 类
    # 这只爬虫的名字
    name = 'tutorial'
    # 列表中填入域名，使爬虫不会爬到其他地方
    allowed_domains = ['python.org']
    # 填入需要爬取的网页地址
    start_urls = ['https://python.org']

    def parse(self, response):
        # 得到的数据传入 response，之后想用来做什么自定义
        item = TutorialItem()
        item['url'] = response.url
        return item
```

最后在命令行中，第一层目录下（scrapy.cfg 文件同级目录）输入如下内容:

```bash
# 将返回值导出至文件
# name 是爬虫类的 name 属性的值
# -o 导出
# filename 是文件名
# json 导出形式
>>> scrapy crawl <name> -o <filename.json> -t json
```

### shell 环境

可使用属性:

| 属性                    | 描述                                |
| ----------------------- | ----------------------------------- |
| `response`              | 响应                                |
| `response.url`          | 网址                                |
| `response.body`         | 源代码                              |
| `sel`                   | scrapy.selector.Selector(response)  |
| `sel.xpath()`           | 根据xpath语言筛选，返回SelectorList |
| `sel.xpath().extract()` | 变成字符串返回                      |

示例:

```python
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com']

    def parse(self, response):
        # 解析逻辑
        yield {'title': response.css('title::text').get()}
```

### Selector

| 方法      | 描述        |
| --------- | ----------- |
| `css()`   | CSS选择器   |
| `xpath()` | XPath选择器 |

示例:

```python
# CSS选择器
titles = response.css('h1::text').getall()

# XPath选择器
titles = response.xpath('//h1/text()').getall()
```
