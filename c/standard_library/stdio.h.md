# stdio.h

## 属性

| 函数 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| printf | 输出 | (char *, ...) | void |
| scanf | 输入 | (char *, ...) | void |
| putchar | 输出一个字符 | (int) | int |
| getchar | 获取一个字符 | (void) | int |
| perror | 输出错误信息 | (char *) | void |
| **文件处理** |  |  |  |
| [fopen](#fopen) | 打开文件 | (char \*, char *) | FILE * |
| [fclose](#fclose) | 关闭文件 | (FILE *) | int |
| [fgetc](#fgetc) | 获取单个字符 | (FILE *) | int |
| [fputc](#fputc) | 写入单个字符 | (int, FILE *) | int |
| [fputs](#fputs) | 写入字符串 | (char \*, FILE *) | int |
| [fgets](#fgets) | 获取字符串 | (char \*, int, FILE *) | char * |
| [fprintf](#fprintf) | 格式化字符串写入 | (FILE \*, char *, ...) | int |
| [fscanf](#fscanf) | 格式化字符串读取 | (FILE \*, char *, ...) | int |
| [fwrite](#fwrite) | 二进制写入 | (void \*, size_t, size_t, FILE *) | size_t |
| [fread](#fread) | 二进制读取 | (void \*, size_t, size_t, FILE *) | size_t |
| [feof](#feof) | 文件是否读到了末尾 | (FILE *) | int |
| [ferror](#ferror) | 文件是否出错 | (FILE *) | int |
| [clearerr](#clearerr) | 清除文件末尾指示器和错误指示器的错误 | (FILE *) | void |
| [ftell](#ftell) | 获取当前指针的位置 | (FILE *) | long |
| [fseek](#fseek) | 设置指针的位置 | (FILE *, long, int) | int |
| [rewind](#rewind) | 使指针回到开头 | (FILE *) | void |
| [fflush](#fflush) | 刷新缓冲区 | (FILE *) | int |
| [setvbuf](#setvbuf) | 设置缓冲区大小 | (FILE \*, char *, int, sizt_t) | int |

| 宏定义 | 描述 | 扩展 |
| --- | --- | --- |
| **文件处理** |  |  |
| EOF | 文件末尾标识符，在读取中遇到EOF表示文件结束 |  |
| SEEK_SET | 指针从文件头开始偏移 |  |
| SEEK_CUR | 指针从当前位置开始偏移 |  |
| SEEK_END | 指针从文件尾开始偏移 |  |
| _IOFBF | 设置缓冲区按块缓冲 |  |
| _IOLBF | 设置缓冲区按行缓冲 |  |
| _IONBF | 设置无缓冲区 |  |
| getc() | fgetc() 的宏定义版本 |  |
| putc() | fputc() 的宏定义版本 |  |

| typedef | 描述 | 原型 |
| --- | --- | --- |
| **文件处理** |  |  |
| FILE |  |  |

### perror

输出错误信息

示例：

```c
#include <stdio.h>

int main(void)
{
    FILE *file = fopen("bucunzaidewenjian", "r");

    perror("出错啦！错误码原因\n");

    return 0;
}
```

### fopen

第一个参数为文件名，第二个为打开模式  
如果文件打开失败返回 NULL  
**注意：打开的文件一定要关闭，使用fclose()函数关闭文件**

| 文件打开模式 | 描述 |
| --- | --- |
| r | 以读的方式打开文件，文件必须存在 |
| w | 以写入的方式打开文件，文件不存在则创建，文件存在会清空文件内容 |
| a | 以追加的方式打开文件，文件不存在则创建，指针在末尾 |
| r+ | 以读写的方式打开文件，文件不存在则创建，写入不会把原有内容后移，而是覆盖 |
| w+ | 以读写的方式打开文件，文件不存在则创建，会清空文件内容 |
| a+ | 以读写追加的方式打开文件，文件不存在则创建 |
| b | 以二进制的方式操作文件，可以和以上模式搭配，如 wb, rb, ab, r+b, w+b, a+b |

示例：

```c
FILE *file, *file2, *file3;

file = fopen("file.txt", "w");
fclose(file);

file2 = fopen("file.txt", "r");
fclose(file2);

if ((file3 = fopen("bucunzaidewenjian", "r")) == NULL)
{
    printf("文件打开失败");
}
fclose(file3);
```

### fclose

关闭一个文件，传入文件指针

示例：

```c
FILE *file = fopen("file.txt", "r");
fclose(file);
```

### fgetc

从文件中读取字符, 返回对应的编码，当读到文件末尾时返回 EOF

示例：

```c
int ch;
FILE *file = fopen("file.txt", "r");

while ((ch = fgetc(file)) != EOF)
{
    putchar(ch);
}

fclose(file);
```

### fputc

写入字符到文件中

示例：

```c
FILE *file = fopen("file.txt", "w");
char s[] = "hello world";
int i;

for (int i; i < 11; i++)
{
    fputc(s[i], file);
}

fclose(file);
```

### fputs

第一个参数为要写入的字符串，第二个参数为文件指针

示例：

```c
FILE *file = fopen("file.txt", "w");

fputs("hello world", file);

fclose(file);
```

### fgets

第一个参数为目标字符串，第二个参数为最大读取多少个字符，第三个参数为文件指针  
读到 '\n' 或 EOF 为止, 如果读到空行则不会改变目标字符串的值  
判断是否读到文件尾可以使用 [feof](#feof) 函数

示例：

```c
FILE *file = fopen("file.txt", "r");
char buffer[1024];

while (!feof(file))
{
    buffer[0] = '\0';
    fgets(buffer, 1024, file);
    printf(buffer);
}

fclose(file);
```

### fprintf

格式化写入，与 printf 相似。第一个参数为文件指针

示例：

```c
FILE *file = fopen("file.txt", "w");

fprintf(file, "%d-%d-%d", 2022, 11, 11);

fclose(file);
```

### fscanf

格式化读取，与 scanf 相似。第一个参数为文件指针

示例：

```c
FILE *file = fopen("file.txt", "r");
int year, month, day;

fscanf(file, "%d-%d-%d", &year, &month, &day);

printf("%d-%d-%d", year, month, day);

fclose(file);
```

### fwrite

二进制写入。第一个参数为要写入数据的地址，第二个参数为数据大小，第三个参数为数据的数量，第四个参数为文件指针

示例：

```c
#include <stdio.h>

int main(void)
{
    struct Date
    {
        int year;
        int month;
        int day;
    };
    
    FILE *file = fopen("file.txt", "wb");
    struct Date date;

    date.year = 2022;
    date.month = 11;
    date.day = 11;
    fwrite(&date, sizeof(struct Date), 1, file);
    
    fclose(file);

    return 0;
}
```

### fread

二进制读取。参数如 fwrite

示例：

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    struct Date
    {
        int year;
        int month;
        int day;
    };
    
    FILE *file = fopen("file.txt", "rb");
    struct Date *date = (struct Date *)malloc(sizeof(struct Date));

    fread(date, sizeof(struct Date), 1, file);
    printf("%d-%d-%d\n", date->year, date->month, date->day);
    
    fclose(file);

    return 0;
}
```

### feof

判断文件指示器是否读到了末尾

在 [fgets](#fgets) 的示例中已有演示

### ferror

判断文件是否出错

示例：

```c
FILE *file;

// 如果文件不存在
if ((file = fopen("bucunzaidewenjian", "r")) == NULL)
{
    printf("文件打开失败");
}
if (ferror(file))
{
    printf("文件出错了");
}

// 如果文件存在，以读的方式打开，但尝试写入
fputs("hello world", file);
if (ferror(file))
{
    printf("文件出错了");
}
```

### clearerr

清除文件错误

示例：

```c
FILE *file = fopen("file.txt", "r");
char s[1024];

fgets(s, 1024, file);
// 假设到此处文件中的字符已全部被读取

fgetc(file); // 读取到 EOF

feof(file);
printf("is eof: %d\n", feof(file)); // 判断为 EOF

clearerr(file);
printf("is eof: %d\n", feof(file)); // 判断不为 EOF

fputc('0', file); // 尝试对只读打开的文件写入
printf("is error: %d\n", ferror(file)); // 判断为 error

clearerr(file);
printf("is error: %d\n", ferror(file)); // 判断不为 error

fclose(file);
```

### ftell

示例：

```c
FILE *file = fopen("file.txt", "w");

fputs("hello world", file);
printf("%d\n", ftell(file)); // 11

fclose(file);
```

### fseek

设置指针的位置。第一个参数为文件指针，第二个参数为偏移量，第三个参数为偏移位置

| 偏移位置 | 描述 |
| --- | --- |
| SEEK_SET | 指针从文件头开始偏移 |
| SEEK_CUR | 指针从当前位置开始偏移 |
| SEEK_END | 指针从文件尾开始偏移 |

示例：

```c
FILE *file = fopen("file.txt", "w");

fputs("hello world", file);
printf("%d\n", ftell(file));

fseek(file, 6, SEEK_SET);
fputs("C", file);
// file = "hello Corld"

fclose(file);
```

### rewind

示例：

```c
FILE *file = fopen("file.txt", "w");

fputs("hello world", file);
printf("%d\n", ftell(file));

rewind(file);
fputs("H", file);
// file = "Hello world"

fclose(file);
```

### fflush

示例：

```c
FILE *file = fopen("file.txt", "w");
char s[1024];

fputs("hello world", file);
printf("按下任意键刷新缓冲区");
getchar();
fflush(file);

fclose(file);
```

### setvbuf

设置缓冲区大小。第一个参数为文件指针，第二个参数为缓冲区指针，第三个参数为缓冲模式，第四个参数为缓冲区大小

| 模式 | 描述 |
| --- | --- |
| _IOFBF | 按块缓冲 |
| _IOLBF | 按行缓冲 |
| _IONBF | 不缓冲 |

此处引入万物皆文件的概念  
以下列举了程序运行时就生成了的文件

| 文件 | 描述 |
| --- | --- |
| stdout | 标准输出流 |
| stdin | 标准输入流 |
| stderr | 标准错误输出流 |

示例：

```c
#include <stdio.h>

int main(void)
{
    char s[1024];
    int ch;
    
    setvbuf(stdout, s, _IOFBF, 1024); // 设置标准输出流的缓冲区
    fprintf(stdout, "按下输入任意字符刷新缓冲区");
    getchar();
    fflush(stdout);

    return 0;
}
```
