# random 模块

随机数生成模块。

导入方式:

```python
import random
```

## 属性

### random() randrange() randint()

- random(): 随机生成 0 到 1 的小数（包含0，不包含1）
- randrange(): 在范围内产生随机数，参数 start, stop, step
- randint(): 在a和b之间（包含a和b）随机生成一个整数

示例:

```python
import random

print(random.random())
print(random.randrange(2, 10, 2))
print(random.randint(1, 10))
```

### choice() choices() sample() shuffle()

- choice(): 随机选择一个序列中元素，返回该元素
- choices(): 随机选择多个序列中的元素，返回列表，k值指定选择次数（可重复）
- sample(): 随机抽取指定数量的元素，返回列表，不重复，k值不能大于序列长度
- shuffle(): 打乱列表元素顺序（原地修改）

示例:

```python
import random

lst = list(range(5))
print(random.choice(lst))
print(random.choices(lst, k=5))
print(random.sample(lst, k=5))

lst2 = lst.copy()
random.shuffle(lst2)
print(lst2)
```

### getstate() setstate()

- getstate(): 获取当前随机数生成器的内部状态
- setstate(): 设置随机数生成器的状态，使用之前的随机数状态可以重现随机数序列

示例:

```python
import random

# 保存当前状态
state = random.getstate()

# 生成一些随机数
print(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

# 恢复状态，重现相同的随机数序列
random.setstate(state)
print(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
```
