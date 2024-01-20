# stdarg.h

## 属性

| 宏定义 | 描述 | 扩展 |
| --- | --- | --- |
| [va_start](#vastart) | 开始读取参数 |  |
| [va_arg](#vaarg) | 依次读取参数 |  |
| [va_end](#vaend) | 结束参数读取 |  |

| typedef | 描述 | 原型 |
| --- | --- | --- |
| va_list | 参数列表类型 |  |

### va_start

开始读取可变参数

示例：

```c
va_list lst;

// va_start 第一个参数为 va_list 类型
// 第二个参数为参数的数量
va_start(lst, 5);
```

### va_arg

依次读取被 va_start 初始化的 va_list 中的参数

示例：

```c
int i;
va_list lst;

va_start(lst, 5);
for (i = 0; i < 5; i++)
{
    // 第一个参数为 va_list
    // 第二个参数表明要读取的是什么类型的数据
    va_arg(lst, int);
}
```

### va_end

结束参数读取

示例：

```c
va_list lst;

va_start(lst, 5);
// ...
va_end(lst); // 结束读取可变参数
```
