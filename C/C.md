# C

## Hello World (C99标准)

```c
#include <stdio.h>

int main(void)
{
    printf("hello world\n");
    return 0;
}
```

每一段代码的末尾需要加上分号 ; 结尾

### 程序入口

程序中的 main 函数作为入口函数, 当程序启动后执行

## 基本输入输出

输入输出函数定义在 [stdio.h](#输入输出) 这个头文件中, 需要在文件开头说明使用到了这个头文件: `#include <stdio.h>`

### printf

输出内容

示例:

```c
printf("hello world\n"); // 正常输出
// hello world

printf("我叫%s, 今年%d岁了\n", "张三", 3); // 以格式化字符串的方式输出
// 我叫张三, 今年3岁了
```

### scanf

获取输入的内容

示例:

```c
int n;
printf("请输入一个数字: "); // 提示文字
scanf("%d", &n); // 捕获一个整型数据并存放到int地址中
```

## 格式化字符串

格式化字符串基础语法, 在 printf 等函数中被格式化

| 格式化字符 | 描述 |
| --- | --- |
| %s | 字符串 (string) |
| %d | 整型 (decimal) |
| %f | 浮点型 (float) |
| %c | 字符 (char) |
| %p | 地址 (pointer) |
| %x | 小写十六进制 (hexadecimal) |
| %X | 大写十六进制 (hexadecimal) |

| 进阶(部分共通) | 描述 |
| --- | --- |
| %.2f | 保留两位小数的浮点数 |
| %11.3f | 表示总占宽度为 11 位, 保留 3 位小数 |
| %2d | 占两个字符宽的整数, 向右对齐, 以空格填充 |

## 转义字符

在字符串中具有特殊意义的字符, 以 \\ 开头

| 字符 | 描述 |
| --- | --- |
| \\\\ | 输出转义字符 \\ 本身 |
| \\0 | C语言中表示字符串结束的字符 |
| \\n | 换行 |
| \\t | 水平制表符(table) |
| \\b | 退格(backspace), 不会删除字符 |
| \\r | 使光标回到开头 |

## 注释

编译器自动忽略的内容, 对代码的注释说明

### 单行注释

关键字:

```c
//
```

示例:

```c
// 这是一段注释
```

### 多行注释

关键字:

```c
/* */
```

示例:

```c
/* 这是一段
注释
*/
```

## 变量

用于存储数据  
变量名由字母, 下划线, 数字组成, 数字不能作为开头  
大致组成:  
1.该变量的地址  
2.变量本身和变量的值

```c
int n = 2; // 2 就是 n 这个变量的值, &n 得到 n 在此处的地址
```

### 声明和定义

```c
int n; // 声明变量
n = 1024; // 定义变量

int n = 1024; // 声明和定义写一起
```

## 头文件

表示该文件使用了哪些文件

```c
#include <stdio.h>
```

## 宏定义

在预处理阶段直接替换为指定常量表达式

```c
#define NAME "constant"
```

示例:

```c
#include <stdio.h>

#define MACRO 2

int main(void)
{
    printf("%d\n", MACRO * MACRO); // 此处的 MACRO 在预处理阶段会被直接替换为 2
    return 0;
}
```

### 带参数的宏

```c
#include <stdio.h>

#define FUN(x) ((x) * (x))

int main(void)
{
    int n = 2;

    printf("%d\n", FUN(n)); // 此处的 FUN(n) 被替换为 ((n) * (n))

    // 需要注意的问题
    printf("%d", FUN(n++)): // 此处的 FUN(n++) 被替换为 ((n++) * (n++))

    return 0;
}
```

### 转字符串和拼接

```c
#include <stdio.h>

// 替换为 "x"
#define A(x) #x
// 替换为 xy
#define B(x, y) x##y
```

可变参数, 通过 \_\_VA\_ARGS\_\_ 访问可变参数

```c
#include A(format, ...) printf(#format ,##__VA_ARGS__)
```

## 运算符

### 赋值运算符

将表达式右侧的值赋值给左侧

### 逗号运算符

C语言中优先级最低的运算符, 甚至比赋值运算符低

### 算数运算符

| 运算符 | 操作数 | 描述 |
| --- | --- | --- |
| + | 双目运算符 | 加 |
| - | 双目运算符 | 减 |
| * | 双目运算符 | 乘 |
| / | 双目运算符 | 除 |
| % | 双目运算符 | 取余 |

### 比较运算符

| 运算符 | 操作数 | 描述 |
| --- | --- | --- |
| < | 双目运算符 | 小于 |
| > | 双目运算符 | 大于 |
| <= | 双目运算符 | 小于等于 |
| >= | 双目运算符 | 大于等于 |
| == | 双目运算符 | 等于 |
| != | 双目运算符 | 不等于 |

### 逻辑运算符

| 运算符 | 操作数 | 描述 |
| --- | --- | --- |
| && | 双目运算符 | 与 |
| \|\| | 双目运算符 | 或 |
| ! | 单目运算符 | 非 |

### 位运算符

| 运算符 | 操作数 | 描述 |
| --- | --- | --- |
| & | 双目运算符 | 按位与 |
| \| | 双目运算符 | 按位或 |
| ^ | 双目运算符 | 按位异或 |
| ~ | 单目运算符 | 按位取反 |
| << | 双目运算符 | 左移 |
| >| 双目运算符 | 右移 |

### 自增自减运算符

| 运算符 | 操作数 | 描述 |
| --- | --- | --- |
| ++ | 单目运算符 | 如在左侧, 操作数自增1后返回其值。如在右侧, 返回其值后自增1 |
| -- | 单目运算符 | 与 ++ 同理, 不过是自减1 |

### 取址运算符和取值运算符

#### 1.取址运算符(&)

拿到一个变量所在的地址

示例:

```c
int a = 1;

printf("%p\n", &a); // 此处 &a 拿到了变量a所在的地址, 可通过 %p 输出查看
```

#### 2.取值运算符(*)

对一个地址解引用拿到其指向的变量

示例:

```c
int a = 1;
int *p = &a; // 将变量a的地址赋值给指针变量p

printf("%d\n", *p); // 对指针变量解引用拿到变量a
*p = 1024; // 对指针变量p解引用得到变量a并对其赋值
```

### 条件运算符

唯一的三目运算符, 类似if语句的缩写

语法

```c
condition ? true : false
```

## sizeof

获取数据字节长度的关键字

关键字

```c
sizeof
```

使用方式:

```c
sizeof(object); // sizeof(对象);
sizeof(type_name); // sizeof(类型);
sizeof object; // sizeof 对象;
```

示例:

```c
printf("size of int: %d\n", sizeof(int));
```

## 数据类型

### 基本类型

### 1.整数类型

存放一个整数的数据类型

声明关键字

```c
int
short int
long int
long long int

unsigned int
```

short int <= int <= long int <= long long int

声明 short int 和 long int 时 int 可以省略

一个整数由符号位和数值组成, 符号位为左往右第一个bit, 为0表示正数和0, 为1表示负数  
在关键字前加上 unsigned 表示无符号整数, 即不存储负数

示例:

```c
int n = 1024;
int n2 = -1024;

unsigned short int n3 = 255;
```

### 2.浮点数类型

存放一个浮点数(小数)的数据类型

声明关键字

```c
float
double
long double
```

float <= double <= long double

示例:

```c
float f = 3.14;
double f2 = 3.1415926;
long double f3 = 3.1415926;
```

### 3.字符类型

存放一个字符的数据类型

声明关键字

```c
char

unsigned char
```

示例:

```c
char a = 'A';
char b = '1';
```

### 4.布尔类型

C99新增数据类型, 存放一个布尔值

声明关键字

```c
_Bool
```

示例:

```c
_Bool a = 0;
_Bool b = 1;
```

### 扩展

### void类型

无类型, 与指针和函数配合使用

声明关键字

```c
void
```

### NULL

一个宏定义的指针

原型

```c
#define NULL ((void *)0)
```

### **高级**

### 1.数组(数组类型)

存储多个同一类型数据的数据类型

声明形式

```c
int variable[n];
int variable[n] = {n1};
int variable[n] = {n1, n2, n3};
int variable[n] = {[n1] = n2, [n3] = n4};
```

用方括号定义一个数组, 方括号中填写数组的长度  
在声明数组时可以对数组进行初始化, 此时声明的第一个括号中的数值可以省略  
可以用下标的方式访问数组中的元素  
注意C语言不会因索引越界而报错, 编写代码时需要注意索引越界问题  
数组变量本身存储的是第一个元素的地址

示例:

```c
int n[5]; // 定义了由5个int组成的数组
int n2[5] = {0}; // 定义并全部初始化为0
int n3[] = {1, 2, 3, 4, 5}; // 定义并按顺序初始化
int n4[5] = {[0] = 10, [4] = 1024}; // 指定位置初始化(C99新增)
char c[5] = {'a', 'b', 'c', 'd', '\0'}; // 5个字符组成的字符串, 末尾的'\0'代表字符串结束
char c2[] = "abcd"; // 定义字符串可简化为这种形式, 实际长度5, 编译器会自动在末尾追加'\0'

// 通过下标的方式访问数组元素, 也可进行赋值操作
// 方括号填写的数组就是索引, 索引从0开始
n[0] = 0;
n[1] = 1;

n[5]; // 索引越界, 将产生意料之外的结果

printf("n = %p, &n[0] = %p", n, &n[0]); // 证明数组本身存储的是第一个元素的地址
```

#### 二维数组

有着二维的表现形式, 实际是一维数组的线性扩展

声明形式

```c
int variable[n][n2];
```

示例:

```c
// 定义一个三行四列的二维数组
// 声明并定义时只有第一个方括号可不写数组长度
int n[][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}};
// 常规写法, 上面那种更直观
int n2[][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};

// 访问二维数组
n[0][1]; // 第一行第二列
```

#### 计算数组长度

通过数组变量除以类型来判断数组长度  
**注意: 此方法只对数组指针无效**

示例:

```c
int array[] = [1, 2, 3 ,4 ,5];

printf("array length = %d\n", sizeof(array) / sizeof(array[0]))
```

### 2.指针(指针类型)

指向一个地址

指针变量的值所指向的不是数据, 而是地址  
**注意: 未被初始化的指针所指向的地址是随机的, 对其解引用并赋值会产生无法预料的结果, 这类指针被称作野指针, 要避免野指针可以在声明时就将其定义为NULL**  
[取值取址运算符](#取址运算符和取值运算符)

声明形式

```c
int *pa;
char *pb;
```

示例:

```c
int n = 100;
int *p; // 声明了一个指向整型数据的指针

// *p = 1024; // 此时不应对未指向任何地址的指针解引用并赋值
p = &n; // 将其指向变量n的地址
*p = 1024; // 对 p 解引用并赋值
```

#### 数组指针

指向一个数组的指针

因数组名本身就是其第一个元素的地址, 所以不需要取址也可以直接赋值给指针变量  

示例:

```c
int n[5];
int *p = n; // 将数组第一个元素的地址赋值给指针
```

地址可以用加法计算下一个地址(跨度在定义指针类型时就告诉编译器了)  
也可用下标的形式获取元素

示例:

```c
int n[] = {1, 2, 3, 4, 5};
int *p = n;

// 以下结果相等, 由此可见数组和指针的相似程度
printf("*(p + 1) = %d, *(n + 1) = %d\n", *(p + 1), *(n + 1));
printf("p[1] = %d, n[1] = %d\n", p[1], n[1]);
```

#### 指针数组

包含多个这样的指针的数组

示例:

```c
int a = 1;
int b = 2;
int c = 3;
int *p[3] = {&a, &b, &c};
```

#### void指针

指向无类型的指针

声明形式

```c
void *p;
```

void指针可以强制转换成任意类型的指针  
最好不对void解引用, 因为void是无类型, 编译器不明白指针所指地址是什么

示例:

```c
int a = 1024;
char c[] = "hello world";
void *p;

p = &a;
printf("p = a, *p = %d\n", *(int *)p);

p = c;
printf("p = c, *p = %s\n", (char *)p);
```

#### NULL指针

指向一个void类型的指针

当不知道给指针初始化为什么值时, 就初始化为NULL, 以避免野指针的形成

示例:

```c
int *p = NULL;
```

#### 常量指针

指向常量的指针

示例:

```c
int a = 100;
const b = 200;

int * const pa = &a; // 声明一个指向 int b 的常量指针, 指针所存储的地址不可改变
const int *pb = &a; // 可修改指针存储的地址, 但不可修改其值
const int * const pc = &b; // 不可修改指针指向的地址, 也不可解引用修改其值
```

#### 二级指针

指向指针的指针

声明形式

```c
int **pp;
```

示例:

```c
int n[] = {1, 2, 3, 4, 5};
int *p = n;
int **pp = &p; // 将指针p的地址赋值给p

printf("(*pp)[1] = %d\n", (*pp)[1]);
printf("p[1] = %d\n", p[1]);
printf("n[1] = %d\n", n[1]);
```

#### 二维数组指针

指向二维数组的指针

声明形式

```c
int (*p)[4];
```

示例:

```c
int n[][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}};
int (*p)[4] = n; // 先是一个指针变量, 然后方括号定义了指针指向一个四个元素的数组

printf("*(*(p + 1) + 2) = %d\n", *(*(p + 1) + 2));
printf("*(*(n + 1) + 2) = %d\n", *(*(n + 1) + 2));
printf("p[1][2] = %d\n", p[1][2]);
printf("n[1][2] = %d\n", n[1][2]);
```

#### 函数指针

指向函数的指针

声明形式

```c
int (*func)(int);
```

示例:

```c
#include <stdio.h>

int add(int, int);

int add(int x, int y)
{
    return x + y;
}

int main(void)
{
    int (*p)(int, int);

    p = add;
    printf("%d\n", p(1, 2));

    return 0;
}
```

#### 通过指针访问结构体成员

通过指针访问结构体、共用体的成员  
可直接通过 -访问成员

示例:

```c
struct Date
{
    int year;
    int month;
    int day;
};

struct Date date;
struct Date *p = &date;

(*p).year = 2022; // 通过解引用访问指针指向的结构体
p->month = 11;
p->day = 11; // 通过 -访问指针指向的结构体的成员
```

### 3.结构体(构造类型)

构造由多个成员构成的结构体

声明形式

```c
struct Name
{
    char first[64];
    char last[64];
};
struct Name name; // 声明结构体变量
```

可通过 . 访问结构体成员  
如果是结构体指针, 可通过 -直接访问成员

示例:

```c
struct Date
{
    int year;
    int month;
    int day;
};

struct Date date;
struct Date *p = &date;

date.year = 2022;
date.month = 11;
p->day = 11;
```

#### 初始化结构体变量

在声明结构体变量时使用 {} 按顺序初始化初始化结构体, 也可通过 .成员变量 指定成员初始化 (C99 语法)

示例:

```c
struct Date
{
    int year;
    int month;
    int day;
};

struct Date date1 = {2022, 6, 18};
struct Date date2 = {.year = 2019, .month = 12, .day = 31};
```

#### 位域

按照 bit 分配成员所占内存

这种情况下成员不再拥有内存地址  
结构体所占内存按照最大的类型算, 且受限

示例:

```c
struct Flags
{
    unsigned int flag1 : 1;
    unsigned int flag2 : 1;
    unsigned int flag3 : 2;
};

struct Flags flags;

flags.flag1 = 0;
flags.flag2 = 1;
flags.flag3 = 2;
```

### 4.共用体(联合类型)

所有成员共用同一个内存地址

声明形式

```c
union Test
{
    int n;
    double f;
    char c[];
};
```

```c
union Test
{
    int n;
    double f;
    char c[];
};

union Test test;

test.n = 1024;
test.f = 3.14;
test.c = "hello world"; // 最终只有 test.c 是可以正常访问的
```

### 5.枚举(枚举类型)

从某个数开始往上列举值

声明形式

```c
enum Test
{
    zero, // 0
    one, // 1
    two // 2
};
enum Ns
{
    n1 = 1, // 1
    n2, // 2
    n3 = 1024, // 1024
    n4 // 1025
};
```

枚举类型的变量都是整类型  
枚举类型中的变量生成在定义的作用域中  
如果一个变量只有其中几个值就使用枚举类型

示例:

```c
enum Ns
{
    n1,
    n2,
    n3
};

enum Ns n = 1;

printf("n1 = %d, n2 = %d, n3 = %d\n", n1, n2, n3);

switch (n)
{
case n1:
    break;
case n2:
    break;
case n3:
    break;
}
```

## 类型转换

类型之间的转换

转换形式

```c
(int)variable;
(char *)variable;
```

在要转换的变量前加上括号, 括号内填写要转换的类型即可

## 常量

声明为常量, 其值为只读, 不可改变

声明关键字

```c
const
```

示例:

```c
const int a = 1024; // 声明一个int常量, 其值不可改变
```

## 符号位

限定整型或char类型是否拥有符号位  
无符号位可以存储更大的正数

| 关键字 | 描述 |
| --- | --- |
| `signed` | 有符号位 (默认) |
| `unsigned` | 无符号位 |

示例:

```c
signed int n = 2;
unsigned int n2 = 4;
```

## 作用域

| 作用域 | 范围 |
| --- | --- |
| 文件作用域 | 声明处开始到文件结束, 代码块之外的声明都具有文件作用域 |
| 代码块作用域 | {}, 从声明开始到代码块结束 |
| 原型作用域 | 只适用于在函数原型中声明的变量名 |
| 函数作用域 | 只适用于 goto 语句, 将 goto 语句的标签限制在函数内  |

## 链接属性

| 属性 | 作用范围 |
| --- | --- |
| external | 外部 |
| internal | 内部 |
| none | 无 |

只有具备文件作用域的标识符才拥有 external 或 internal 属性  
关于 [extern](#extern-外部链接) 和 [static](#static-静态变量)

## 生存期

* 静态存储期 (static storage duration)
    > 具有文件作用域的定义属于静态存储期, 直到程序结束时释放内存
* 自动存储期 (automatic storage duration)
    > 具有代码块作用域的定义一般属于自动存储期, 直到代码块结束时释放内存

## 存储类型

| 类型 | 描述 |
| --- | --- |
| auto | 自动变量 |
| register | 寄存器变量 |
| extern | 外部链接 |
| static | 静态变量 |
| typedef | 类型定义 |

### auto (自动变量)

由编译器自动判断释放内存, 默认的存储类型

声明关键字

```c
auto
```

示例:

```c
auto int n_g = 0; // 在程序结束后自动释放

int main(void)
{
    auto int n_f = 1; // 在 main 函数结束后自动释放;
    {
        auto int n_i = 2; // 离开代码块后被自动释放
    }
    return 0;
}
```

如果在全局和代码块中都声明了同一个变量, 推荐将代码块中的变量声明用上 auto

示例:

```c
int n = 1024;

int main(void)
{
    auto int n = 256;
    return 0;
}
```

### register (寄存器变量)

将一个变量声明为寄存器变量, 该变量有可能存储在寄存器中 (CPU访问寄存器几乎没有延迟)

声明关键字

```c
register
```

寄存器变量和自动变量在很多方面都是一样的, 都有代码块作用域, 自动存储期, 空连接属性  
**注意: register 声明的变量因存储在寄存器中, 所以无法获取内存地址**

示例:

```c
int main(void)
{
    register int n = 1024;

    // &n; // n 没有内存地址
    return 0;
}
```

### extern (外部链接)

告诉编译器该声明在其他地方定义了

声明关键字

```c
extern
```

示例:

```c
#include <stdio.h>

int main(void)
{
    extern int n; // 使用 extern 告诉编译器, 这个 n 在其他地方定义了

    printf("%d\n", n);
    return 0;
}

int n = 1024; // 实际定义 n 的位置
```

多文件示例:

```c
// 文件A
int n = 1024;
```

```c
// 文件B
extern int n; // 这个n在别的文件中定义了

int main(void)
{
    printf("n = %d\n", n);
    return 0;
}
```

### static (静态变量)

定义静态存储类型

声明关键字

```c
static
```

#### 静态局部变量

使局部变量的生存期维持到程序结束

在函数结束时, 静态变量不会被释放内存, 对静态变量定义的初始值只初始化一次

示例:

```c
#include <stdio.h>

int count(void);

int count(void)
{
    static int count = 0;
    return count++;
}

int main(void)
{
    printf("%d\n" count()); // 0
    printf("%d\n" count()); // 1
    printf("%d\n" count()); // 2
    return 0;
}
```

#### 静态全局变量

告诉编译器该定义仅文件内部可用, 其他文件不可用 (只对具有文件作用域的定义生效)

多文件示例:

```c
// 文件A
static int n = 1024;
```

```c
// 文件B
// 编译时会报错, 因为文件A的n是其内部的变量, 所以找不到n的定义
extern int n;

int main(void)
{
    printf("n = %d\n", n);
    return 0;
}
```

## typedef

对已有数据类型封装, 为类型起别名, 简化复杂的声明

声明关键字

```c
typedef
```

示例:

```c
typedef int interger;

// 声明了一个 interger 类型的变量, 这个 interger 是 int 类型
integer n = 1024;
```

进阶示例:

```c
#include <stdio.h>

// 定义了一个 td_func 类型, 此类型返回一个指向两个int参数返回int类型数据的函数指针
typedef int (*td_func)(int, int);

int add(int, int);
int sub(int, int);
int calc(td_func, int, int);
td_func select(char);

int add(int x, int y)
{
    return x + y;
}

int sub(int x, int y)
{
    return x - y;
}

int calc(td_func func, int x, int y)
{
    return func(x, y);
}

td_func select(char c)
{
    switch (c)
    {
    case '+':
        return add;
    case '-':
        return sub;
    }
}

int main(void)
{
    printf("%d\n", calc(select('+'), 1, 2));
    printf("%d\n", calc(select('-'), 1, 2));
    return 0;
}
```

## 语句

### if

条件判断语句

语法

```c
// 单分支结构
if (condition)
{
    code;
}

// if else 双分支结构
if (condition)
{
    code;
}
else
{
    code;
}

// 多分支结构
if (condition)
{
    code;
}
else if (condition2)
{
    code;
}
else
{
    code;
}
```

如果语句后只有一行代码, 那么大括号可以省略, 但为了方便阅读, 不推荐省略

示例:

```c
#include <stdio.h>

int main(void)
{
    char rain[] = "下雨";
    char sun[] = "晴天";
    char *weather = rain;

    if (weather == rain)
    {
        printf("今天下雨, 在家玩\n");
    }
    else
    {
        printf("天气真好, 出去玩玩\n");
    }

    int score = 90;

    if (score == 100)
    {
        printf("无敌\n");
    }
    else if (score >= 90)
    {
        printf("优秀\n");
    }
    else if (score >= 60)
    {
        printf("及格\n");
    }
    else
    {
        printf("不及格\n");
    }

    return 0;
}
```

### switch

根据常量表达式匹配代码块

语法

```c
switch (constant)
{
case constant: // 匹配成功就从这执行
    code;
    break; // 退出switch语句
case constant2:
    code;
    break;
default: // 如果都没匹配的默认执行语句
    code;
    break;
}

switch (constant4)
{
case constant1:
case constant2:
case constant3:
case constant4:
case constant5:
    code;
    break;
case constant6:
case constant7:
    code;
    break;
}
```

switch 语句匹配的代码块最后需要一行 break 表示结束;  
如果不写, 则 swtich 语句不会停止, 将继续往下执行

示例:

```c
#include <stdio.h>

int main(void)
{
    switch (4)
    {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        printf("工作日\n");
        break;
    case 6:
    case 0:
        printf("休息日\n");
        break;
    }

    return 0;
}
```

### while

while 循环语句, 条件符合就继续执行

语法

```c
while (condition)
{
    code;
}
```

示例:

```c
#include <stdio.h>

int main(void)
{
    int i;

    i = 0;
    while (i < 10)
    {
        printf("%d\n", i);
        i++;
    }
    return 0;
}
```

### do while

和 while 循环类似, 但是先执行后判断, 且末尾需要分号

语法

```c
do
{
    code;
} while (condition);
```

### for

for 循环语句, 将初始化语句, 条件判断语句, 自增自减语句缩写到一行

语法

```c
for (initial variable; condition; increment)
{
    code;
}
```

示例:

```c
#include <stdio.h>

int main(void)
{
    int i;

    for (i = 0; i < 10; i++)
    {
        printf("%d\n", i);
    }
    return 0;
}
```

### break continue

循环控制语句

关键字

```c
break
continue
```

break 打断循环, 中断循环  
continue 结束本次循环, 进入下次循环

示例:

```c
#include <stdio.h>

int main(void)
{
    int i = 0

    while (i < 10)
    {
        i++;
        if (i == 5)
        {
            break;
        }
        if (i % 2)
        {
            continue;
        }
        printf("%d\n", i);
    }
    return 0;
}
```

### goto

使程序跳转到指定行

关键字

```c
goto
```

goto 语句跳转到指定标签处, goto 语句具有函数作用域, 不同函数的标签不相通  
最好不适用 goto 语句, 因为这种随意跳转的行为会破坏代码逻辑  
何时使用 goto？例如要跳出多重循环时, 正常写法会相对复杂, 可以使用 goto 一步到位

示例:

```c
#include <stdio.h>

int main(void)
{
    int i = 0;

    while (1)
    {
        if (i == 10)
        {
            goto end; // 跳转到 end 标签处
        }
        printf("%d\n", i++);
    }
end: // end 标签
    printf("END\n");
    return 0;
}
```

## 函数

执行封装好的一串代码并返回结果给调用方

声明形式

```c
// 声明
int func(int, int);

// 定义
int func(int x, int y)
{
    return x + y;
}
```

函数声明时可以不写参数名, 但要写上参数类型  
如果一个函数没有返回值, 则指定类型为 void  
**注意: 不要返回局部变量的地址, 因为局部变量会在函数结束时被销毁**  
C99标准: 如果一个函数没有任何参数, 括号里写 void

示例:

```c
#include <stdio.h>

void funca(void); // 声明一个无参无返回值的函数
int funcb(int, int); // 声明一个有两个 int 参数, 返回 int 类型值的函数
char *funcc(int); // 声明一个有一个参数, 返回 char 类型指针的函数

void funca(void)
{
    printf("hello world");
}

int funcb(int x, int y)
{
    return x * y;
}

char *funcc(int score)
{
    if (score == 100)
    {
        return "优秀";
    }
    else if (score >= 60)
    {
        return "及格";
    }
    else
    {
        return "不及格";
    }
}

int main(void)
{
    funca();
    printf("%d\n", funcb(2, 4));
    printf("%s\n", funcc(100));
    return 0;
}
```

### 可变参数

想要声明函数参数可变, 只需在生命中写上 ...

关键字

```c
...
```

示例:

```c
#include <stdio.h>
#include <stdarg.h>

int test(int, ...);

int test(int n, ...)
{
    int i;
    va_list lst; // 声明 va_list 类型

    va_start(lst, n); // 设置有几个参数
    for (i = 0; i < n; i++)
    {
        printf("%d\n", va_arg(lst, int)); // 开始按指定类型依次提取参数
    }
    va_end(lst); // 结束参数提取

    printf("n = %d\n", n);
    return 0;
}

int main(void)
{
    test(4, 2, 1, 4, 3);
    return 0;
}
```

### 内联函数

编译器会将内联函数在调用处展开

关键字

```c
inline
```

一般来说编译器会自动判断哪些函数需要内联, 哪些不用  
**注意: 手动声明内联函数需要在编译时加上 -O 选项**

示例:

```c
#include <stdio.h>

inline int sqrt(int);

inline int sqrt(int n)
{
    return n * n;
}

int main()
{
    printf("%d\n", sqrt(2));
    return 0;
}
```

## 链表

一个结构体的成员指向另一个结构体

示例:

```c
#include <stdio.h>
#include <stdlib.h>

struct Date
{
    int year;
    int month;
    int day;
    int note;
    struct Date *next;
};

void add(struct Date **);

void add(struct Date **p_date)
{
    struct Date *date = (struct Date *)malloc(sizeof(struct Date));

    if (*p_date == NULL)
    {
        date->day = 0;
    }
    else
    {
        date->day = (*p_date)->day + 1;
    }
    date->next = *p_date;
    *p_date = date;
}

int main(void)
{
    struct Date *date = NULL;

    add(&date);
    add(&date);
    add(&date);
    printf("%d\n", date->day);
    printf("%d\n", date->next->day);
    printf("%d\n", date->next->next->day);

    return 0;
}
```

## 库文件扩展

### 输入输出

[stdio.h](standard_library/stdio.h.md)

### 字符串处理

[string.h](standard_library/string.h.md)

### 函数可变参数

[stdarg.h](standard_library/stdarg.h.md)

### 时间

[time.h](standard_library/time.h.md)

### 内存分配

[stdlib.h](standard_library/stdlib.h.md)  

内存处理: [string.h](standard_library/string.h.md)

### 文件处理

[stdio.h](standard_library/stdio.h.md)

### 错误处理

[errno.h](standard_library/errno.h.md)

输出错误信息: [perror](standard_library/stdio.h.md#perror)

错误信息字符串: [strerror](standard_library/string.h.md#strerror)
