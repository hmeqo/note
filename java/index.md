# Java

## Hello World

文件名: HelloWorld.java

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```

每一段代码的末尾需要加上分号 ; 结尾

### 程序入口

与文件名 (不含后缀) 同名的类, 其中的 main 方法为入口方法, 在程序启动后第一个执行

## 基本输入输出

### System.out.println

输出字符串, 结尾自动换行

示例:

```java
System.out.println("hello world");
```

### System.out.print

输出字符串, 结尾不自动换行

示例:

```java
System.out.print("hello world\n");
```

### Scanner

从控制台读取输入的字符  
需导入 Scanner 类:

```java
import java.util.Scanner;
```

| 方法 | 描述 |
| --- | --- |
| next | 获取字符串 |
| nextInt | 获取整型 |
| nextFloat | 获取浮点型 |
| hasNext | 输入是否为 String 类型 |
| hasNextInt | 输入是否为 int 类型 |
| hasNextDouble | 输入是否为 double 类型 |
| hasNextBoolean | 输入是否为 boolean 类型 |

示例:

```java
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        // 创建 Scanner 对象
        Scanner input = new Scanner(System.in);
        System.out.print("输入你的姓名: ");
        String name = input.next(); // 读取字符串
        System.out.print("输入你的年龄: ");
        int age = input.nextInt(); // 读取整数
        System.out.println("姓名: " + name + " 年龄: " + age);
        // 关闭 Scanner
        input.close();
    }
}
```

## 注释

编译器自动忽略的内容, 对代码的注释说明

### 单行注释

关键字:

```java
//
```

示例:

```java
// 这是一段注释
```

### 多行注释

关键字:

```java
/* */
```

示例:

```java
/* 这是一段
注释
*/
```

### 文档注释 (JavaDoc)

生成规范的开发文档, 写在上方

常用的 JavaDoc 标签

| 标签 | 含义 |
| --- | --- |
| @author | 作者名 |
| @version | 版本标识 |
| @parameter | 参数及其含义 |
| @since | 最早使用该方法/类/接口的 JDK 版本 |
| @return | 返回值 |
| @throws | 异常抛出条件 |

关键字:

```java
/** */
```

示例:

```java
/** 
 * description
 * @author ...
 * @version ...
 */
```

## 变量

变量名由字母, 下划线, $, 数字组成, 数字不能作为开头  
变量名不能使用 Java 语言本身定义的关键字, 如 int、class、public 等关键字  
变量名区分大小写

语法:

```java
数据类型 变量名;
```

示例:

```java
// 声明
String name;
char gender;
int age;
double money;

// 初始化
name = "张三";

// 声明的同时初始化
boolean isMember = true;
```

## 常量

常量只能赋值一次, 赋值后不可更改, 常量名使用大写字母

语法:

```java
final 数据类型 常量名;
```

示例:

```java
final int KB = 1024;
final int MB = 1024 * KB;
```

## 数据类型

| 数据类型 | 关键字 | 占用内存空间/字节 | 取值范围 |
| --- | --- | --- | --- |
| 布尔型 | boolean | 1 | ture、false |
| 字节型 | byte | 1 | $-128$ ~ $127$ |
| 字符型 | char | 2 | $0$ ~ $(2^{16} - 1)$ |
| 短整型 | short | 2 | $-2^{15}$ ~ $(2^{15} - 1)$ |
| 整型 | int | 4 | $-2^{31}$ ~ $(2^{31} - 1)$ |
| 长整型 | long | 8 | $-2^{63}$ ~ $(2^{63} - 1)$ |
| 单精度浮点型 | float | 4 | $1.4013E{-45}$ ~ $3.4028E{+38}$ |
| 双精度浮点型 | double | 8 | $4.9E{-324}$ ~ $1.7977E{+308}$ |

### 数组

存储多个同一数据类型

声明形式:

```java
int[] ia = new int[5];
double[] da = new double[5];
String[] sa = new String[5];
```

右侧 [] 内的数值为数组长度, 没有初始化值时填写

#### 初始化数组

在声明时使用 {} 对数组初始化, 数组长度由元素个数决定, 所以括号中不能指定数组长度  
若数组类型为基本数据类型, 在声明时没有对其初始化, 则初始化为默认值 (如: int 类型初始化为 0)

示例:

```java
int[] ia = new int[] {1, 2, 3, 4, 5};
int[] iab = {1, 2, 3, 4, 5};
```

#### 数组元素的访问和赋值

通过 [] 下标获取数组元素或赋值, [] 内填写 0 则代表数组的第一位元素, 1 则代表第二位元素

示例:

```java
int[] array = new int[5];
// 赋值
array[0] = 1;
array[1] = 4;
// 访问
array[2] = array[0] + array[1];
System.out.println(array[2]);
```

#### 获取数组长度

使用 length 属性获取数组长度 (注: length 属性只可读, 不可写)

示例:

```java
int[] ia = new int[5];
int ia_length = ia.length;
System.out.println(ia_length);
```

#### 数组元素排序

使用 `java.util.Arrays` 对数组升序排序

示例:

```java
import java.util.Arrays;

public class Test {
    public static void main(String[] args) {
        int[] array = {9, 3, 7, 2, 8};
        System.out.print("Original: ");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + ", ");
        }
        System.out.println();

        Arrays.sort(array);
        System.out.print("Sorted: ");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + ", ");
        }
        System.out.println();
    }
}
```

### 数据类型转换

#### 自动类型转换

比较小的类型向大的类型转换

#### 强制类型转换

在表达式左侧加上括号并填写类型

示例:

```java
int n = 1024;
float f = (float) n;
double d = (double) (n + f);
```

## 运算符

### 赋值运算符

赋值运算符为 `=`, 作用是把等号右侧的表达式的值赋值给左侧的变量

### 算数运算符

| 算数运算符 | 名称 | 作用 | 示例 |
| --- | --- | --- | --- |
| + | 加法运算符 | 求操作数的和 | 4 + 6 等于 10 |
| - | 减法运算符 | 求操作数的差 | 6 - 4 等于 2 |
| * | 乘法运算符 | 求操作数的乘积 | 6 * 4 等于 24 |
| / | 除法运算符 | 求操作数的商 | 6 / 4 等于 1 |
| % | 求余运算符 | 求操作数相除的余数 | 6 % 4 等于 2 |
| ++ | 自加运算符 | 求操作数加 1 后的结果 | int x = 6; x++; 即 x=x+1 |
| -- | 自减运算符 | 求操作数减 1 后的结果 | int x = 6; x--; 即 x=x-1 |

++ / -- 在前时, 先自增或自减, 再返回其值。在后时, 先返回其值, 再自增或自减

### 关系运算符

表达式成立, 则为真 (true), 否则为假 (false)

| 关系运算符 | 说明 |
| --- | --- |
| > | 大于 |
| < | 小于 |
| >= | 大于等于 |
| <= | 小于等于 |
| == | 等于 (比较两个对象的内存地址) |
| != | 不等于 |

### 逻辑运算符

| 运算符 | 名称 | 说明 |
| --- | --- | --- |
| && | 逻辑与 | 表示并且、与。多个条件同时为 true, 结果为 true, 否则为 false |
| \|\| | 逻辑或 | 表示或、或者。多个条件有一个为 true, 结果为 true; 多个条件同时为 false, 结果为 false |
| ! | 逻辑非 | 条件为 true 时, 结果为 false; 条件为 false 时, 结果为 true |

### 条件运算符

语法:

```java
expressions ? true : false
```

示例:

```java
int n = 1024;
int n2 = 2048;

System.out.println(n > n2 ? n : n2);
```

### 运算符优先级

算数运算符 > 关系运算符 > 逻辑运算符

## 语句

### if

语法:

```java
// 单分支
if (condition) {
    code;
}

// 双分支
if (condition) {
    code;
} else {
    code;
}

// 多分支
if (condition) {
    code;
} else if (condition) {
    code;
} else {
    code;
}
```

示例:

```java
int age = 18;

if (age >= 18) {
    System.out.println("你成年了");
} else {
    System.out.println("你还没成年, 之后的内容等以后再来探索吧");
}
```

### switch

语法:

```java
switch (n) {
    case 0:
        code;
        break;
    case 1:
        code;
        break;
    case 2:
        code;
        break;
    default:
        code;
        break;
}

switch (wday) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        code;
        break;
    case 6:
    case 0:
        code;
        break;
}
```

示例:

```java
int wday = 2;

switch (wday) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        System.out.println("工作日");
        break;
    case 6:
    case 0:
        System.out.println("休息日");
        break;
}
```

### while

循环语句

语法:

```java
while (condition) {
    code;
}
```

### do while

先执行后判断的循环

语法:

```java
do {
    code;
} while (condition);
```

### for

语法:

```java
for (initialize; condition; incremental) {
    code;
}
```

### break continue

break 打断循环, 中断循环  
continue 结束本轮循环, 继续下一轮循环

关键字:

```java
break continue
```

## 类

成员变量会被赋予初始值, 基本数据类型为 0, 引用数据类型为 null

创建类模板:

```java
public class TestClass {
    // attributes 类属性
    int n;
    // methods 方法
    public void test() {
        System.out.println(n); // 访问类属性
    }
}
```

### 实例对象

使用 `new` 关键字创建实例对象, 创建的对象称为实例对象  
使用 `.` 访问实例属性

示例:

```java
class TestClass {
    int n;
    public void testMethod() {
        System.out.println(n);
    }
}

public class Test {
    public static void main(String[] args) {
        TestClass instance = new TestClass(); // 创建实例对象
        instance.n = 1024;
        instance.testMethod();
    }
}
```

### 方法

声明形式:

```java
void method() {
    // code
}
```

void 表示该方法的返回值, void 为没有返回值。method 为方法名。() 中为方法的参数。{} 中为代码。

使用 `return` 返回值

示例:

```java
float pi() {
    return 3.14;
}
```

有参方法示例:

```java
int add(int x, int y) {
    return x + y;
}
```

#### 方法中访问实例对象

使用 `this` 关键字访问当前实例对象, `this` 即实例对象本身

示例:

```java
public class Test {
    public int a;

    public void setA(int a) {
        this.a = a;
    }
}
```

### 修饰

| 关键字 | 描述 |
| --- | --- |
| **访问修饰符** |  |
| public | 表示该属性为公有。文件中外层只能有一个 public, 即文件名的类 |
| protected | 保护, 访问权限仅文件域中, 文件外部无法访问 |
| private | 私有, 仅该类内部访问, 子类和其他方无法访问 |
| default | 默认访问权限, 只能在同一包内访问 |
| **修饰符** |  |
| final | 常量修饰 |
| **类的修饰符** |  |
| abstract | 定义抽象类 |
| **属性和方法的修饰符** |  |
| static | 静态方法和属性 |

#### static

静态, 被修饰的属性和方法无法被实例化, 属于类本身拥有的, 无需实例化对象即可使用  
静态方法和属性之间可以相互访问, 普通方法可以访问静态属性和方法, 反之则不可以

语法:

```java
public class Test {
    static int a; // 静态属性
    
    // 静态方法
    static void method() {
        // 方法体
    }
}
```

示例:

```java
public class Test {
    static int a = 0;
    
    public static void main(String[] args) {
        a = 1024;
        System.out.println(a);
        method1();
        Test.method2();
    }

    public static method1() {
        System.out.println("method1");
    }

    public static method2() {
        System.out.println("method2");
    }
}
```

#### abstract

抽象类无法被实例化  
抽象类可以定义属性和抽象方法, 抽象方法没有方法体, 只有方法声明, 方法体通过继承者 (继承者也可以是另一个抽象方法) 实现  
对抽象方法实例化相当于创建了一个继承自它的匿名类

语法:

```java
abstract class Test {
    int attr;
    abstract void method();
}
```

示例:

```java
abstract class A {
    int n = 64;
    abstract void method();
}

public class Main extends A {
    public static void main(String[] args) {
        Main m = new Main();
        System.out.println(m.n);
        m.method();
        System.out.println(m.n);
    }

    @Override
    void method() {
        this.n = 1024;
    }
}
```

### 类继承

一个类继承另一个类的方法和属性
**Java 类只能单继承, 不能多继承**

关键字:

```java
extends
```

语法:

```java
class A {
    int a;
    
    void method1() {
        // method1
    }
}

class B extends A {
    void method2() {
        // method2
    }
}
```

#### 访问父类的方法和属性

使用 `super` 关键字访问父类的方法和属性  
`super()` 为父类的初始化方法, `super.method()` 调用父类的其它方法和属性

示例:

```java
class A {
    public void methodA() {
        System.out.println("A");
    }
}

class B extends A {
    public void methodA() {
        super.methodA();
        System.out.println("B");
    }
}
```

### 封装

封装内部实现细节, 对外提供安全的接口

### 泛型

是指在定义函数、接口或类的时候，不预先指定具体的类型，而在使用的时候再指定类型的一种特性

语法:

```java
class Generic<E>
E obj
E method()
```

示例:

```java
// file: Generic.java
public class Generics<E> {
    public E obj;
    
    Generic(E obj) {
        this.obj = obj;
    }

    public E get() {
        return obj;
    }
}
```

## 接口

与抽象类相似, 但其中定义的属性被默认加上了 final static 修饰, 方法默认加上 abstract 修饰  
对接口初始化操作相当于创建了一个匿名类继承了这个接口  
**接口可以多继承**

语法:

```java
interface MyIface {
    int a = 1024; // final 修饰的静态常量

    void method1(); // 抽象方法
}
```

### 实现接口

关键字:

```java
implements
```

```java
interface MyIface {
    int a = 1024;

    void method1();
}

class A implements MyIface {
    @override
    void method1() {
        System.out.println("Method1");
    }
}
```

### 接口继承

关键字:

```java
extends
```

示例:

```java
interface A {
    public void method1();
}

interface B {
    public void method2();
}

interface C extends A, B {
    @Override
    default void method1() {
        System.out.println("Method1");
    }
}

public class Main implements C {
    public static void main(String[] args) {
        Main m = new Main();
        m.method1();
        m.method2();
    }

    @Override
    public void method2() {
        System.out.println("Method2");
    }
}
```

```java
// file: Main.java
public class Main {
    public static void main(String[] args) {
        Generics<String> = new Generics<>("Hello World");
        System.out.println(Generic.get());
    }
}
```

## 迭代对象

实现 Iterable 接口的对象可被迭代  
实现 Iterator 接口即可创建自己的迭代器

示例:

```java
import java.util.ArrayList;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        Test<String> t = new Test<>(new ArrayList<>());
        t.array.add("123");
        t.array.add("abc");
        for (String item : t) {
            System.out.println(item);
        }
    }
}

class Test<E> implements Iterable<E>, Iterator<E> {
    public ArrayList<E> array;
    public int index = -1;

    Test(ArrayList<E> array) {
        this.array = array;
    }

    @Override
    public Iterator<E> iterator() {
        index = -1;
        return this;
    }

    @Override
    public boolean hasNext() {
        return ++index < array.size();
    }

    @Override
    public E next() {
        return array.get(index);
    }
}
```

## 异常

`Exception` / `Error`, 异常就是错误, 当程序发生异常是会中断程序, 并输出异常信息

异常有很多种, 例如索引超出抛出 `IndexOutOfBoundsException` 这个异常, 但大部分异常都继承自 `Exception` 这个父类, 抛出的异常都是实例对象

### 抛出异常

语法:

```java
throw 异常示例对象;
```

示例:

```java
throw new Exception("发生错误啦");
```

### 异常捕获

语法:

```java
try {
    // 代码块
} catch (Exception e) { // 要捕获的异常类型和存放异常的变量名
    // 捕获异常, 成功捕获到异常后 e 就是异常的实例对象
} finally {
    // try 代码块之后执行, 无论如何是否出现异常都会执行
}
```

示例:

```java
int[] array = new int[5];
try {
    System.out.println(array[5]);
} catch (IndexOutOfBoundsException e) {
    System.out.println("索引超出了");
} finally {
    System.out.println("代码执行完毕");
}
```

## 内置类

### String

String 类位于 java.lang 包中, java.lang 包会自动导入

| 方法 | 描述 |
| --- | --- |
| concat | 拼接字符串 |
| equals | 比较字符串是否相等 |
| equalsIgnoreCase | 比较字符串是否相等, 无视大小写 |
| length | 字符串长度 |
| toCharArray | 将 String 转换为 char 数组 |
| toLowerCase | 转换小写 |
| toUpperCase | 转换大写 |
| split | 按字符串将字符串分隔为数组 |
| **提取和查询** |  |
| charAt | 得到该位置的字符 |
| indexOf | 查询第一个出现的字符或字符串 |
| lastIndexOf | 查询最后一个出现的字符或字符串 |
| substring | 提取从 index 位置开始到最后一个字符为止的部分, 或指定结束位置 |
| trim | 返回前后不含空格的字符串 |
| **类方法** |  |
| valueOf | 将任意对象转换为 String 类型, 使用 String 类名调用 |

### StringBuffer

于 String 基本一致, 但比 String 更高效, 且可更改值

| 方法 | 描述 |
| --- | --- |
| append | 将字符串追加到末尾 |
| insert | 在字符串指定位置插入参数 |
| toString | 转换为 String 类型 |

### Math

| 方法 | 描述 |
| --- | --- |
| random | 生成 [0.0, 1.0] 的 double 类型随机数 |

## 作用域

| 作用域 | 描述 |
| --- | --- |
| 成员作用域 | 类内部 |
| 局部作用域 | 如方法 |

## 包

Java 通过包来管理类, 类似于文件存储于文件夹中, Java 的类文件可以存储于包中  
使用 `package` 关键字声明包, 声明语句必须写在开头, 第一句非注释性语句

语法:

```java
package 包名;
```

示例:

```java
package com.javaex.pkg;
```

### 导入包

使用 `import` 语句导入包

语法:

```java
import 包名.类名;
```

示例:

```java
import java.util.Scanner; // 导入 java.util 包下的 Scanner 类
```

使用 `*` 导入包中所有类

示例:

```java
import java.util.*;
```
