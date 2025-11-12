# pickle 模块

转换二进制数据存储的模块，用于Python对象的序列化和反序列化。

导入方式:

```python
import pickle
```

## 属性

### dump() load()

转换成二进制存储和载入。

- dump(): 填入对象和文件，把对象转换成二进制存入文件
- load(): 加载二进制，参数填文件，返回Python对象

示例:

```python
import pickle

a = [123, 3.14, 'pickle', ['pickle']]
with open('pickle.pkl', 'wb') as file:
    pickle.dump(a, file)

with open('pickle.pkl', 'rb') as file:
    print(pickle.load(file))
```
