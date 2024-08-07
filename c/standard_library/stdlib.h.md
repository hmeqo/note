# stdlib.h

## 属性

| 函数 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| system | 执行shell命令 |  |  |
| exit | 退出程序 | (int) | void |
| **内存分配** |  |  |  |
| [malloc](#malloc) | 申请一块内存 | (size_t) | void * |
| [calloc](#calloc) | 申请一块内存，并清零 | (size_t, size_t) | void * |
| [realloc](#realloc) | 重新分配一块内存 | (void *, size_t) | void * |
| [free](#free) | 释放内存 | (void *) | void |

| 宏定义 | 描述 | 扩展 |
| --- | --- | --- |
| EXIT_FAILURE | 程序因错误退出的返回值 |  |

### malloc

申请一块内存  
**注意：申请的内存没用时要及时释放掉，否则会造成内存泄漏**

示例：

```c
int *p = (int *)malloc(4 * sizeof(int)); // 申请了 4 个 int 类型大小的内存，返回首地址
```

### calloc

示例：

```c
int *p = (int *)calloc(4, sizeof(int)); // 申请了 4 块 int 类型的连在一起的内存，返回首地址
```

### realloc

示例：

```c
int *p = realloc(NULL, 4 * sizeof(int)); // 申请了 4 * sizeof(int) 大小的内存，返回首地址
int *p = realloc(p, 16 * sizeof(int)); // 重新申请内存，返回首地址
realloc(p, 0); // 相当于释放内存
```

### free

示例：

```c
int *p = malloc(4 * sizeof(int));
free(p); // 释放内存
// p 指向的内存被释放，此时 p 指向非法地址
```
