# string.h

## 属性

| 函数 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| [strlen](#strlen) | 返回字符串长度 | (char *) | size_t |
| [strcpy](#strcpy) | 复制字符串，参数第一个为目标 | (char \*, char *) | char * |
| [strncpy](#strncpy) | 指定复制字符串的长度，不会自动追加'\n' | (char \*, char *, size_t) | char * |
| [strcat](#strcat) | 两个字符串拼接 | (char \*, char *) | char * |
| [strncat](#strncat) | 只取前几个字符拼接进去 | (char \*, char *, size_t) | char * |
| [strcmp](#strcmp) | 比较两个字符串 | (char \*, char *) | int |
| [strncmp](#strncmp) | 只比较前几个字符 | (char \*, char *, size_t) | int |
| **内存处理** |  |  |  |
| [memset](#memset) | 设置给定内存的每个字节的值 | (void *, int, size_t) | void * |
| [memcpy](#memcpy) | 复制内存的数据到目标内存中 | (void \*, void *, size_t) | void * |
| memmove | 移动内存的数据到目标内存中 | (void \*, void *, size_t) | void * |
| [memcmp](#memcmp) | 比较两块内存是否不等 | (void \*, void *, size_t) | int |
| **异常处理** |  |  |  |
| [strerror](#strerror) | 返回错误码对应的错误信息 | (int) | char * |

### strlen

示例：

```c
char a[] = "hello world";

printf("a length = %d\n", strlen(a));
```

### strcpy

示例：

```c
char a[12];
char b[12] = "hello world";

// 将字符串 b 拷贝到 a 中
strcpy(a, b);
// a = "hello world"
```

### strncpy

示例：

```c
char a[12];
char b[12] = "hello world";

// 将字符串 b 的前5个字符拷贝到 a 中，不会自动追加 '\0'
strncpy(a, b, 5);
a[5] = '\0';
```

### strcat

示例：

```c
char a[12] = "hello";
char b[12] = " world";

// 将字符串 b 拼接到字符串 a 中
strcat(a, b);
// a = "hello world"
```

### strncat

示例：

```c
char a[12] = "hello";
char b[12] = " world";

// 将字符串 b 的前三个字符拼接到字符串 a 中
strcat(a, b, 3);
// a = "hello wo"
```

### strcmp

比较两个字符串，相等返回 0，大于返回 1，小于返回 -1

示例：

```c
printf("abc compare abc: %d\n", strcmp(a, "abc")); // 0
printf("b compare a: %d\n", strcmp(a, b)); // 1
printf("b compare c: %d\n", strcmp(a, b)); // -1
```

### strncmp

> 与 strcmp 同理，不过是只判断前几个字符

### memset

第一个参数是内存地址，第二个参数为每个字节要初始化的值，第三个参数为内存大小

示例：

```c
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int *a = (int *)malloc(5 * sizeof(int));
    
    memset(a, 0, 5 * sizeof(int)); // 将 a 这块内存的所有二进制位擦为 0
    free(a);
    return 0;
}
```

### memcpy

示例：

```c
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int *a = (int *)calloc(5, sizeof(int));
    int *b = (int *)calloc(5, sizeof(int));
    
    b[0] = 1;
    b[1] = 2;
    b[2] = 3;
    memcpy(a, b, 5 * sizeof(int));
    // a = b
    free(a);
    free(b);
    return 0;
}
```

### memcmp

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int *a = (int *)calloc(5, sizeof(int));
    int *b = (int *)calloc(5, sizeof(int));
    
    a[0] = 1;
    b[0] = 1;
    printf("a == b? %d\n", !memcmp(a, b, 5 * sizeof(int)));
    // a == b? 1
    b[0] = 1024;
    printf("a == b? %d\n", !memcmp(a, b, 5 * sizeof(int)));
    // a == b? 0
    free(a);
    free(b);
    return 0;
}
```

### strerror

返回错误码对应的错误信息

示例：

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void)
{
    FILE *file = fopen("bucunzaidewenjian", "r");

    printf("出错啦！错误原因: %s\n", strerror(errno));

    return 0;
}
```
