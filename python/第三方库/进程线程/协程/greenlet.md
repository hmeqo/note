# greenlet

## 安装

```bash
pip install greenlet
```

## 导入模块

```python
from greenlet import greenlet
```

## 属性

| 类/方法      | 描述         |
| ------------ | ------------ |
| `greenlet()` | 创建协程对象 |

### Greenlet 对象

| 方法       | 描述             |
| ---------- | ---------------- |
| `switch()` | 切换到该协程     |
| `dead`     | 检查协程是否已死 |

示例:

```python
from greenlet import greenlet

def test1():
    print('test1: 1')
    gr2.switch()
    print('test1: 2')
    gr2.switch()

def test2():
    print('test2: 1')
    gr1.switch()
    print('test2: 2')

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
```

### 协程状态

- 协程可以处于运行、暂停或死亡状态
- 使用 `switch()` 方法可以在协程之间切换
- 当协程函数执行完毕时，协程进入死亡状态

### 注意事项

- greenlet 提供手动切换的协程
- 与 gevent 不同，greenlet 需要手动控制切换时机
- 常用于需要精确控制协程切换的场景
