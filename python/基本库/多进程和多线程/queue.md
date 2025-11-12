# queue 模块

队列数据结构。

导入方式:

```python
import queue
```

示例:

```python
import queue

q = queue.Queue()
q.put('item1')
q.put('item2')
print(q.get())  # 输出: item1
print(q.get())  # 输出: item2
```
