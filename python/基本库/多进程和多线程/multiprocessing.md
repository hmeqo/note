# multiprocessing 模块

进程池和多进程操作。

导入方式:

```python
import multiprocessing
```

## 属性

示例:

```python
import multiprocessing
import os

def worker(num):
    print(f'进程 {num} 正在运行，PID: {os.getpid()}')

if __name__ == '__main__':
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
```
