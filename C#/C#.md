# C\#

## Hello World

项目名: `Project`
文件名: `Program.cs`

```cs
using System;

namespace Project
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World !");
        }
    }
}
```

## 输入输出

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| [`WriteLine`](#consolewriteline) | 向控制台输出一行字符串 (默认带换行) |  |
| [`Write`](#consolewrite) | 向控制台输出一串字符串 |  |
| [`ReadLine`](#consolereadline) | 向控制台输出一串字符串 |  |

### Console.WriteLine

示例:

```cs
Console.WriteLine("Hello World"); // 默认输出
// Hello World
Console.WriteLine("我的名字是{0}, 今年{1}岁了。", "张三", 18); // 格式化输出
// 我的名字是张三, 今年18岁了
```

### Console.Write

示例:

```cs
Console.Write("Hello"); // 默认不附带换行的输出方式
// Hello
Console.Write(" World");
// Hello World
```

### Console.ReadLine

示例:

```cs
string name;
Console.Write("你的名字是: ");
name = Console.ReadLine(); // 从控制台读取一行内容
```

## 格式化字符串

语法:

```cs
$"{expression}"
```

示例:

```cs
string s = "下午";
int t = 13;
Console.Write($"现在是{s}{t}点");
// 现在是下午13点
```

## 注释

语法:

```cs
// 单行注释

/*
多行注释
*/

/// 文档注释
/// 文档注释
/// 文档注释
```

## region

语法:

```cs
#region ...的字段
// 代码块
#endregion
```

## 数据类型

常用数据类型

| 数据类型 | 描述 | 示例 |
| --- | --- | --- |
| `int` | 整型 | `int a = 1024;` |
| `float` | 浮点型 | `float f = 3.14;` |
| `double` | 双精度浮点型 | `double f = 3.14159;` |
| `char` | 字符型 | `char c = 'A';` |
| `string` | 字符串 | `string s = "hello world";` |
| `bool` | 布尔类型 | `bool flag = true;`, `bool flag = false;` |

### 数组

语法:

```cs
int[] a;
int[,] b;
```

#### 获取数组长度

通过 `数组名.Length` 获取数组长度

## 语句

### if-else

条件判断语句

语法:

```java
if (condition)
{
}

if (condition)
{
}
else
{
}

if (condition)
{
}
else if (condition)
{
}
else
{
}
```

### switch

条件分支语句

语法:

```java
switch (expression)
{
    case const1:
        break;
    case const2:
    case const3:
        break;
    default:
        break;
}
```

### while

语法:

```cs
while (condition)
{
    // 代码块
}
```

### do while

语法:

```cs
do
{
    // 代码块
} while (condition);
```

### for

语法:

```cs
for ([初始化];[条件判断];[增量])
{
    // 代码块
}
```

### foreach

语法:

```cs
foreach ([迭代变量] in [可迭代对象])
{
    // 代码块
}
```

### try

搭配: try-catch, try-finally, try-catch-finally

语法:

```cs
try
{
    // 可能会报错的代码
}
catch (异常类型 异常变量)
{
    // 捕获到异常时
}
finally
{
    // 执行完 try 和 catch 代码后必定执行的代码块
}
```

## 类和对象

类是一个抽象概念的集合  
对象是这个类的个体实例, 拥有这个类的全部属性

语法:

```cs
[访问修饰符] [修饰符] class 类名
{
    // 属性, 成员变量
    string name;
    int age;

    // 入口方法
    static void Main(string[] args)
    {
        // 方法体
    }

    // 普通方法
    void method()
    {
        // 方法体
    }
}
```

示例:

```cs
class Label
{
    string text;

    static void Main(string[] args)
    {
        Label lb = new Label();
        lb.setText("A Label");
        lb.print();
    }

    void setText(string text)
    {
        this.text = text;
    }

    void print()
    {
        Console.WriteLine(this.text);
    }
}
```

### 修饰符

| 修饰符 | 描述 |
| --- | --- |
| **访问修饰符** |  |
| `public` | 公有的, 可以在任何项目中访问类 |
| `private` | 私有的, 仅该类内部访问, 子类和其他方无法访问 |
| `protected` | 受保护的, 访问权限仅文件域中, 文件外部无法访问 |
| `internal` | 默认, 在当前程序集内可以实现对类的的调用 |
| **修饰符** |  |
| `abstract` | 抽象类或抽象方法 |
| `static` | 静态类或静态方法, 类不能被实例化 |
| **类的修饰符** |  |
| `sealed` | 密封类, 不能被继承 |

### 方法

语法:

```cs
[访问修饰符] [修饰符] 返回值类型 方法名([参数])
{
    // 方法体
}
```

示例:

```cs
void test()
{
    Console.WriteLine("Test method.");
}
```

#### 方法中访问实例对象

使用 `this` 关键字访问当前实例对象, `this` 即实例对象本身

示例:

```cs
class Test
{
    public int a;

    public void setA(int a)
    {
        this.a = a;
    }
}
```

#### 引用传递

使用 `ref` 和 `out` 关键字完成引用传递 (本质为指针传递)

示例:

```cs
class Test
{
    public Test()
    {
        int a = 3;
        int b;
        
        method(ref a);
        Console.WriteLine(a);

        method2(out b);
        Console.WriteLine(b);
    }

    public void method(ref int a)
    {
        a += 10;
    }

    public void method2(out int b)
    {
        b = 10;
    }
}
```

### 属性封装

用一个公用属性展示私有属性  
封装内部实现细节, 对外提供安全的接口

语法:

```cs
public [数据类型] Variable { get => variable; set => variable = value; }
```

示例:

```cs
private int a;

public int A { get => a; set => a = value; }
```

#### 调用

示例:

```cs
using System;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {
            Program p = new Program();
            p.testMethod(); // 方法调用
        }

        void testMethod()
        {
            Console.WriteLine("Test method.");
        }
    }
}
```

#### 返回值类型

声明了这个方法的返回值类型, 如果没有返回值则填 `void`

## 内置类

### Math

用于数据运算的类

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| `Round` | 四舍五入 | `Math.Round(3.14); // 3`, `Math.Round(3.14, 1); // 3.1` |

### string

字符串

| 属性 | 描述 |
| --- | --- |
| `Length` | 字符串长度 |

| 方法 | 描述 |
| --- | --- |
| `IndexOf` | 查找一串字符串在此字符串中第一次出现的位置, 找不到返回 -1 |
| `LastIndexOf` | 查找一串字符串在此字符串中最后一次出现的位置, 找不到返回 -1 |
| `StartsWith` | 判断字符串开头是否为某个字符串 |
| `EndsWith` | 判断字符串结尾是否为某个字符串 |
| `Contains` | 判断字符串是否包含某个字符串 |
| `ToLower` | 转换全小写字符串 |
| `ToUpper` | 转换全大写字符串 |
| `Trim` | 裁剪开头和结尾的空白符 |
| `TrimStart` | 裁剪开头的空白符 |
| `TrimEnd` | 裁剪结尾的空白符 |
| `Split` | 按某个字符分隔字符串 |
| `Join` | 拼接字符串数组 |
| `Substring` | 截取字符串, 从第一个参数提供的索引开始, 截取指定长度 (第二个参数) 的字符串, 如果不指定长度则截取之后的全部字符 |

#### Length

示例:

```cs
string s = "Hello World";
Console.WriteLine("Length: {0}", s.Length);
// Length: 11
```

#### IndexOf

示例:

```cs
string s = "Hello World";
Console.WriteLine("IndexOf W: {0}", s.IndexOf("W"));
// IndexOf W: 6
Console.WriteLine("IndexOf A: {0}", s.IndexOf("A"));
// IndexOf W: -1
```

#### LastIndexOf

类似 `IndexOf()`

#### StartsWith

示例:

```cs
string s = "Hello World";
Console.WriteLine("StartsWith H: {0}", s.StartsWith("H"));
// StartsWith H: true
Console.WriteLine("StartsWith Hello: {0}", s.StartsWith("Hello"));
// StartsWith Hello: true
Console.WriteLine("StartsWith A: {0}", s.StartsWith("A"));
// StartsWith A: false
```

#### EndsWith

类似 `StartsWith()`

#### Contains

示例:

```cs
string s = "Hello World";
Console.WriteLine("Contains ello: {0}", s.Contains("ello"));
// StartsWith ello: true
Console.WriteLine("Contains ea: {0}", s.Contains("ea"));
// StartsWith ea: false
```

#### ToLower

示例:

```cs
string s = "Hello World";
Console.WriteLine("ToLower: {0}", s.ToLower());
// hello world
```

#### ToUpper

示例:

```cs
string s = "Hello World";
Console.WriteLine("ToUpper: {0}", s.ToUpper());
// HELLO WORLD
```

#### Trim

示例:

```cs
string s = "\t Hello World \n";
Console.WriteLine("Trim: {0}", s.Trim());
// Hello World
```

#### TrimStart

示例:

```cs
string s = "\t Hello World \n";
Console.WriteLine("TrimStart: {0}", s.TrimStart());
// Hello World \n
```

#### TrimEnd

示例:

```cs
string s = "\t Hello World \n";
Console.WriteLine("TrimEnd: {0}", s.TrimEnd());
// \t Hello World
```

#### Split

示例:

```cs
string s = "Hello World";
string[] sa = s.Split("l");
Console.Write("sa = [");
foreach (string i in sa)
{
    Console.Write("\"{0}\", ", i);
}
Console.WriteLine("\b\b] ");
// sa = ["He", "", "o Wor", "d"]
```

#### Join

示例:

```cs
string[] sa = {"Hello", "World"};
Console.WriteLine(string.Join(" ", sa));
// Hello World
Console.WriteLine(string.Join(",", sa));
// Hello,World
```

#### Substring

示例:

```cs
string s = "Hello World";
Console.WriteLine(1, 3);
// ell
Console.WriteLine(3, 2);
// lo
```

#### 其它数据类型和字符串间的转换

其它数据类型通过 `ToString()` 转换成字符串

### Convert

转换数据类型

| 方法 | 描述 |
| --- | --- |
| Toint32 | 转换为32位有符号整型 |
| ToSignal | 转换为单精度浮点数 |
