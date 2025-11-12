# requests

## 安装

```bash
pip install requests
```

## 导入模块

```python
import requests
```

## 属性

| 方法       | 描述           |
| ---------- | -------------- |
| `get()`    | 发送GET请求    |
| `post()`   | 发送POST请求   |
| `put()`    | 发送PUT请求    |
| `patch()`  | 发送PATCH请求  |
| `delete()` | 发送DELETE请求 |
| `head()`   | 发送HEAD请求   |

### Response 对象

| 属性/方法     | 描述               |
| ------------- | ------------------ |
| `status_code` | HTTP状态码         |
| `text`        | 响应内容（字符串） |
| `content`     | 响应内容（字节）   |
| `encoding`    | 响应编码           |
| `json()`      | 解析JSON响应       |
| `headers`     | 响应头             |

示例:

```python
import requests

# GET请求
url = 'http://www.baidu.com/'
response = requests.get(url)
response.encoding = 'UTF-8'
print('1.', response.text)
print('2.', response.content)
```
