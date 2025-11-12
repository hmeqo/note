# functools 模块

函数工具。

导入方式:

```python
import functools
```

## 属性

### reduce()

对数字元素的序列进行加减乘除等计算。

示例:

```python
import functools
print(functools.reduce(lambda x, y: x * y, [i for i in range(1, 6)]))
```
