# errno.h

## 属性

| 宏定义 | 描述 | 扩展 |
| --- | --- | --- |
| errno | 错误码 |  |

### errno

> 一个宏定义

示例：

```c
#include <stdio.h>
#include <errno.h>

int main(void)
{
    FILE *file = fopen("bucunzaidewenjian", "r");

    printf("出错啦！错误码：%d\n", errno);

    return 0;
}
```

#### 输出错误信息

[perror](stdio.h.md#perror)

#### 错误信息字符串

[strerror](string.h.md#strerror)
