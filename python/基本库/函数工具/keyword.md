# keyword 模块

与 Python 标识符有关。

导入方式:

```python
import keyword
```

## 属性

### iskeyword()

判断是否是保留标识符。

示例:

```python
import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('print'))
print(keyword.iskeyword('is'))
```

### kwlist

变量，所有的保留标识符。

示例:

```python
import keyword
print(keyword.kwlist)
```
