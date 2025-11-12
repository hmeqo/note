# threading 模块

多线程操作。

导入方式:

```python
import threading
```

示例:

```python
import threading
import time

def worker():
    print(f'线程 {threading.current_thread().name} 开始')
    time.sleep(2)
    print(f'线程 {threading.current_thread().name} 结束')

threads = []
for i in range(3):
    t = threading.Thread(target=worker, name=f'Thread-{i}')
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```
