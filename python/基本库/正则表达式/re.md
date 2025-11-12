# re 模块

正则表达式操作。

导入方式:

```python
import re
```

示例:

```python
import re
text = 'abc:bca:defg'
print(re.findall(r'[a-zA-Z]+', text))
```
