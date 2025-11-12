# copy 模块

拷贝。

导入方式:

```python
import copy
```

## 属性

### copy() deepcopy()

- copy(): 和一般的拷贝一样，都是浅拷贝
- deepcopy(): 深拷贝

示例:

```python
import copy

lst = [1, 2, 3]
print('原列表', lst)
lst2 = copy.copy(lst)
print('拷贝的列表', lst2)

lst = [[1], [2], [3]]
print('原列表', lst)
lst2 = copy.deepcopy(lst)
print('拷贝的列表', lst2)
```
