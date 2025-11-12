# urllib.request 模块

网络请求操作。

导入方式:

```python
import urllib.request
```

示例:

```python
import urllib.request
response = urllib.request.urlopen('http://example.com')
print(response.read().decode('utf-8'))
```
