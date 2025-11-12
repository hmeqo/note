# gevent

## 安装

```bash
pip install gevent
```

## 导入模块

```python
import gevent
```

## 属性

| 函数/方法   | 描述             |
| ----------- | ---------------- |
| `spawn()`   | 创建协程         |
| `joinall()` | 等待所有协程完成 |
| `sleep()`   | 协程睡眠         |

### Greenlet 对象

| 方法      | 描述           |
| --------- | -------------- |
| `start()` | 启动协程       |
| `join()`  | 等待协程完成   |
| `value`   | 获取协程返回值 |

示例:

```python
import gevent

def task(n):
    for i in range(n):
        print(f'Task {n}: {i}')
        gevent.sleep(0)  # 让出控制权

# 创建协程
coroutines = [gevent.spawn(task, 5), gevent.spawn(task, 3)]

# 等待所有协程完成
gevent.joinall(coroutines)
```

### 猴子补丁

```python
import gevent.monkey
gevent.monkey.patch_all()  # 打补丁，使标准库变为协程友好
```

这样可以使标准库的阻塞操作变为非阻塞的协程操作。
