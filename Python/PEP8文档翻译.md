# PEP8

## 目录

1. [**Introduction**](#介绍)
   > 介绍
2. [**A Foolish Consistency is the Hobgoblin of Little Minds**](#愚蠢的一致性是心胸狭窄的妖怪)
   > 愚蠢的一致性是心胸狭窄的妖怪
3. [**Code Lay-out**](#代码布局)
   > 代码布局
   1. [**Indentation**](#缩进)
      > 缩进
   2. [**Tabs or Spaces?**](#制表符还是空格)
      > 制表符还是空格
   3. [**Maximum Line Length**](#最大行长度)
      > 最大行长度
   4. [**Should a Line Break Before or After a Binary Operator?**](#应该在二元运算符之前还是之后换行)
      > 应该在二元运算符之前还是之后换行
   5. [**Blank Lines**](#空行)
      > 空行
   6. [**Source File Encoding**](#源文件编码)
      > 源文件编码
   7. [**Imports**](#导入)
      > 导入
   8. [**Module Level Dunder Names**](#模块级别dunder名称)
      > 模块级别Dunder名称
4. [**String Quotes**](#字符串引号)
   > 字符串引号
5. [**Whitespace in Expressions and Statements**](#表达式和语句中的空格)
   > 表达式和语句中的空格
   1. [**Pet Peeves**](#厌恶的东西)
      > 厌恶的东西
   2. [**Other Recommendations**](#其他建议)
      > 其他建议
6. [**When to Use Trailing Commas**](#何时使用尾随逗号)
   > 何时使用尾随逗号
7. [**Comments**](#注释)
   > 注释
   1. [**Block Comments**](#块注释)
      > 块注释
   2. [**Inline Comments**](#内联注释)
      > 内联注释
   3. [**Documentation Strings**](#文档字符串)
      > 文档字符串
8. [**Naming Conventions**](#命名规定)
   > 命名约定
   1. [**Overriding Principle**](#压倒一切的原则)
      > 压倒一切的原则
   2. [**Descriptive: Naming Styles**](#描述_命名样式)
      > 描述: 命名样式
   3. [**Prescriptive: Naming Conventions**](#规定_命名约定)
      > 规定: 命名约定
      1. [**Names to Avoid**](#名称以避免)
         > 名称，以避免
      2. [**ASCII Compatibility**](#ascii兼容性)
         > ASCII兼容性
      3. [**Package and Module Names**](#包和模块名)
         > 包和模块名
      4. [**Class Names**](#类名)
         > 类名
      5. [**Type Variable Names**](#类型变量名)
         > 类型变量名
      6. [**Exception Names**](#异常的名字)
         > 异常的名字
      7. [**Global Variable Names**](#全局变量名)
         > 全局变量名
      8. [**Function and Variable Names**](#函数和变量名)
         > 函数和变量名
      9. [**Function and Method Arguments**](#函数和方法参数)
         > 函数和方法参数
      10. [**Method Names and Instance Variables**](#方法名称和实例变量)
          > 方法名称和实例变量
      11. [**Constants**](#常量)
          > 常量
      12. [**Designing for Inheritance**](#设计继承)
          > 设计继承
   4. [**Public and Internal Interfaces**](#公共和内部接口)
      > 公共和内部接口
9. [**Programming Recommendations**](#编程建议)
   > 编程建议
   1. [**Function Annotations**](#函数注释)
      > 函数注释
   2. [**Variable Annotations**](#变量的注释)
      > 变量的注释
10. [**References**](#参考文献)
    > 参考文献
11. [**Copyright**](#版权)
    > 版权

## 介绍

This document gives coding conventions for the Python code comprising
the standard library in the main Python distribution. Please see the
companion informational PEP describing style guidelines for the
C code in the C implementation of Python [1].

This document and PEP 257 (Docstring Conventions) were adapted
from Guido's original Python Style Guide essay, with some additions
from Barry's style guide [2].

This style guide evolves over time as additional conventions are
identified and past conventions are rendered obsolete by changes in
the language itself.

Many projects have their own coding style guidelines.
In the event of any conflicts, such project-specific guides take
precedence for that project.

> 本文档给出了主要Python发行版中包含标准库的Python代码的编码约定。
> 请参阅配套的信息PEP，在Python[1]的C实现中描述C代码的风格指南。
>
> 本文档和PEP 257 (Docstring约定)改编自Guido最初的Python风格指南文章，
> 并从Barry的风格指南[2]中添加了一些内容。
>
> 随着时间的推移，附加的约定被识别出来，而过去的约定由于语言本身的变化而过时，
> 这种风格指南也会不断演变。
>
> 许多项目都有自己的编码风格指南。在任何冲突的情况下，这些特定于项目的指南优先于该项目。

## 愚蠢的一致性是心胸狭窄的妖怪

One of Guido's key insights is that code
is read much more often than it is written.
The guidelines provided here are intended to improve the
readability of code and make it consistent across the wide spectrum
of Python code. As PEP 20 says, "Readability counts".

A style guide is about consistency.
Consistency with this style guide is important.
Consistency within a project is more important.
Consistency within one module or function is the most important.

However, know when to be inconsistent -- sometimes style
guide recommendations just aren't applicable. When in doubt,
use your best judgment. Look at other examples and decide what looks best.
And don't hesitate to ask!

In particular: do not break backwards compatibility
just to comply with this PEP!

Some other good reasons to ignore a particular guideline:

1. When applying the guideline would make the code less readable,
even for someone who is used to reading code that follows this PEP.
2. To be consistent with surrounding code that also breaks it
(maybe for historic reasons) -- although this is also an opportunity to
clean up someone else's mess (in true XP style).
3. Because the code in question predates the introduction of the
guideline and there is no other reason to be modifying that code.
4. When the code needs to remain compatible with older versions of
Python that don't support the feature recommended by the style guide.

> Guido的一个关键观点是，代码的阅读次数比编写次数要多。
> 这里提供的指导原则旨在提高代码的可读性，并使其在广泛的Python代码中保持一致。
> 正如PEP 20所说，“可读性很重要”。
>
> 风格指南是关于一致性的。与此风格指南的一致性是重要的。项目中的一致性更重要。
> 一个模块或功能的一致性是最重要的。
>
> 但是，要知道什么时候不一致——有时风格指南的建议并不适用。有疑问时，请做出最好的判断。
> 看看其他的例子，决定什么看起来最好。不要犹豫，尽管发问!
>
> 特别是:不要为了遵守这个PEP而破坏向后兼容性!
>
> 其他一些忽略特定指导原则的好理由:
>
> 1. 当应用该准则时，代码的可读性会降低，即使对于习惯于阅读遵循这个PEP的代码的人也是如此。
> 2. 与周围的代码保持一致，也打破了它(可能是历史原因)——尽管这也是一个机会来清理别人的混乱
> (在真正的XP风格)。
> 3. 因为有问题的代码早于准则的引入，没有其他理由修改该代码。
> 4. 当代码需要与不支持风格指南推荐特性的旧版本Python保持兼容时。

## 代码布局

### 缩进

Use 4 spaces per indentation level.

Continuation lines should align wrapped elements either vertically using
Python's implicit line joining inside parentheses,
brackets and braces, or using a hanging indent [7].
When using a hanging indent the following should be considered;
there should be no arguments on the first line and further indentation should be
used to clearly distinguish itself as a continuation line:

> 每个缩进级别使用4个空格。
>
> 延续行应该垂直对齐被包装的元素，可以使用Python的隐式行连接括号、方括号和大括号，也可以使用悬挂缩进。
> 当使用悬挂缩进时，应该考虑以下几点:第一行不应该有参数，缩进应该用来清楚地将自己区分为延续行:

```python
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

```python
# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

The 4-space rule is optional for continuation lines.

Optional:

> 对于连续的行，4空格规则是可选的。
>
> 可选:

```python
# Hanging indents *may* be indented to other than 4 spaces.
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)
```

When the conditional part of an if-statement is long enough to require
that it be written across multiple lines,
it's worth noting that the combination of a two character keyword (i.e. if),
plus a single space, plus an opening parenthesis creates
a natural 4-space indent for the subsequent lines of the multiline conditional.
This can produce a visual conflict with the indented suite of
code nested inside the if-statement, which would also naturally
be indented to 4 spaces. This PEP takes no explicit position on how (or whether)
to further visually distinguish such conditional lines from the nested
suite inside the if-statement. Acceptable options in this situation include,
but are not limited to:

> 当条件一个if语句的一部分足够长要求编写跨多个行,值得注意的是,两个字符的组合关键字(即if),
> 加上一个空格,加上开括号创建一个自然4空间缩进的后续行多行条件。
> 这可能会与嵌套在if语句中的缩进代码产生视觉冲突，这也会自然缩进到4个空格。
> 这个PEP没有明确说明如何(或是否)进一步直观地将这些条件行与if语句中的嵌套套件区分开。
> 这种情况下可接受的选择包括但不限于:

```python
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

(Also see the discussion of whether to break before or after binary operators below.)

The closing brace/bracket/parenthesis on multiline constructs may either line
up under the first non-whitespace character of the last line of list, as in:

> (还请参阅下面关于在二进制操作符之前还是之后中断的讨论。)
>
> 在多行结构中，右大括号/方括号/括号可以在列表最后一行的第一个非空格字符下对齐，如:

```python
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```

or it may be lined up under the first character of the line
that starts the multiline construct, as in:

> 或者它可以排在multiline结构开头的行的第一个字符下面，如:

```python
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

### 制表符还是空格

Spaces are the preferred indentation method.

Tabs should be used solely to remain consistent with code
that is already indented with tabs.

Python 3 disallows mixing the use of tabs and spaces for indentation.

Python 2 code indented with a mixture of tabs and spaces
should be converted to using spaces exclusively.

When invoking the Python 2 command line interpreter with the -t option,
it issues warnings about code that illegally mixes tabs and spaces.
When using -tt these warnings become errors. These options are highly recommended!

> 空格是首选的缩进方法。
>
> 制表符应该单独使用，以保持与已经使用制表符缩进的代码一致。
>
> Python 3禁止在缩进中混合使用制表符和空格。
>
> 使用制表符和空格缩进的Python 2代码应该转换为只使用空格。
>
> 当使用-t选项调用Python 2命令行解释器时，它会对非法混合制表符和空格的代码发出警告。
> 当使用-tt时，这些警告变成错误。强烈推荐这些选项!

### 最大行长度

Limit all lines to a maximum of 79 characters.

For flowing long blocks of text with fewer structural restrictions
(docstrings or comments), the line length should be limited to 72 characters.

Limiting the required editor window width makes it possible to have several
files open side-by-side, and works well when using code review tools
that present the two versions in adjacent columns.

The default wrapping in most tools disrupts the visual structure of the code,
making it more difficult to understand. The limits are chosen to
avoid wrapping in editors with the window width set to 80,
even if the tool places a marker glyph in the final column when wrapping lines.
Some web based tools may not offer dynamic line wrapping at all.

Some teams strongly prefer a longer line length. For code maintained
exclusively or primarily by a team that can reach agreement on this issue,
it is okay to increase the line length limit up to 99 characters,
provided that comments and docstrings are still wrapped at 72 characters.

The Python standard library is conservative and requires limiting lines to
79 characters (and docstrings/comments to 72).

The preferred way of wrapping long lines is by using Python's implied line
continuation inside parentheses, brackets and braces. Long lines can be broken
over multiple lines by wrapping expressions in parentheses.
These should be used in preference to using a backslash for line continuation.

Backslashes may still be appropriate at times.
For example, long, multiple with-statements cannot use implicit continuation,
so backslashes are acceptable:

> 限制所有行最多79个字符。
>
> 对于结构限制较少的长文本块(文档字符串或注释)，行长度应限制在72个字符。
>
> 限制必需的编辑器窗口宽度使得可以同时打开多个文件，
> 并且当使用代码检查工具在相邻的列中显示两个版本时工作得很好。
>
> 大多数工具中的默认包装破坏了代码的视觉结构，使其更难理解。
> 选择这些限制是为了避免在窗口宽度设置为80的编辑器中进行换行，
> 即使在换行时工具在最后一列中放置了标记符号。一些基于web的工具可能根本不提供动态换行。
>
> 有些球队强烈喜欢更长的队形。对于能够在这个问题上达成一致的团队专门维护或主要维护的代码，
> 可以将行长度限制增加到99个字符，前提是注释和文档字符串仍然被封装为72个字符。
>
> Python标准库很保守，要求将每行限制为79个字符(文档字符串/注释限制为72个字符)。
>
> 包装长行的首选方式是在圆括号、方括号和大括号内使用Python隐含的行延续。
> 通过将表达式用括号括起来，可以将长行分隔成多行。这些应该优先于使用反斜杠作为续行符。
>
> 有时反斜杠可能仍然是合适的。例如，长且多个with-statement不能使用隐式延续，所以反斜杠是可以接受的:

```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

(See the previous discussion on multiline if-statements for further
thoughts on the indentation of such multiline with-statements.)

Another such case is with assert statements.

Make sure to indent the continued line appropriately.

> (请参阅前面关于多行if-statements的讨论，了解对这种多行with-statements缩进的进一步思考。)
>
> 另一种情况是使用assert语句。
>
> 确保后续行适当缩进。

### 应该在二元运算符之前还是之后换行

For decades the recommended style was to break after binary operators.
But this can hurt readability in two ways:
the operators tend to get scattered across different columns on the screen,
and each operator is moved away from its operand and onto the previous line.
Here, the eye has to do extra work to tell which items are
added and which are subtracted:

> 几十年来，推荐的样式是使用二进制操作符。
> 但这可能在两方面损害可读性:操作符往往分散在屏幕上的不同列中，每个操作符从其操作数移到前一行。
> 在这里，眼睛需要做额外的工作来分辨哪些项目被添加了，哪些项目被删除了:

```python
# Wrong:
# operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

To solve this readability problem, mathematicians and their
publishers follow the opposite convention.
Donald Knuth explains the traditional rule in his
Computers and Typesetting series:
"Although formulas within a paragraph always break after binary operations and
relations, displayed formulas always break before binary operations" [3].

Following the tradition from mathematics usually results in more readable code:

> 为了解决这个可读性问题，数学家和他们的出版商遵循了相反的惯例。
> Donald Knuth解释了他的计算机和排版系列中的传统规则:
> “虽然一段内的公式总是在二进制运算和关系之后中断，
> 但显示的公式总是在二进制运算之前中断”[3]。
>
> 遵循数学的传统通常会导致更可读的代码:

```python
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

In Python code, it is permissible to break before or after a binary operator,
as long as the convention is consistent locally.
For new code Knuth's style is suggested.

> 在Python代码中，允许在二进制操作符之前或之后中断，只要该约定在本地是一致的。
> 对于新代码，建议使用Knuth的风格。

### 空行

Surround top-level function and class definitions with two blank lines.

Method definitions inside a class are surrounded by a single blank line.

Extra blank lines may be used (sparingly)
to separate groups of related functions.
Blank lines may be omitted between a bunch of related one-liners
(e.g. a set of dummy implementations).

Use blank lines in functions, sparingly, to indicate logical sections.

Python accepts the control-L (i.e. ^L) form feed character as whitespace;
Many tools treat these characters as page separators,
so you may use them to separate pages of related sections of your file.
Note, some editors and web-based code viewers may not recognize control-L
as a form feed and will show another glyph in its place.

> 用两个空行包围顶层函数和类定义。
>
> 类中的方法定义由单个空白行包围。
>
> 额外的空行可以(少量地)用来分隔相关的函数组。在一堆相关的一行程序(例如一组虚拟实现)之间可以省略空行。
>
> 在函数中使用空白行来表示逻辑部分。
>
> Python接受control-L(即^L)换页字符作为空格;许多工具将这些字符视为页面分隔符，
> 因此您可以使用它们来分隔文件相关部分的页面。
> 注意，一些编辑器和基于web的代码查看器可能无法将control-L识别为一个提要，并将在其位置上显示另一个符号。

### 源文件编码

Code in the core Python distribution should always use UTF-8
(or ASCII in Python 2).

Files using ASCII (in Python 2) or UTF-8 (in Python 3) should not have
an encoding declaration.

In the standard library, non-default encodings should be used only for
test purposes or when a comment or docstring needs to mention an author
name that contains non-ASCII characters; otherwise,
using \x, \u, \U, or \N escapes is the preferred way to
include non-ASCII data in string literals.

For Python 3.0 and beyond, the following policy is prescribed for
the standard library (see PEP 3131):
All identifiers in the Python standard library MUST use ASCII-only identifiers,
and SHOULD use English words wherever feasible (in many cases,
abbreviations and technical terms are used which aren't English).
In addition, string literals and comments must also be in ASCII.
The only exceptions are (a) test cases testing the non-ASCII features,
and (b) names of authors.
Authors whose names are not based on the Latin alphabet
(latin-1, ISO/IEC 8859-1 character set) MUST provide a transliteration
of their names in this character set.

Open source projects with a global audience are encouraged to
adopt a similar policy.

> 核心Python发行版中的代码应该始终使用UTF-8(或Python 2中的ASCII)。
>
> 使用ASCII(在Python 2中)或UTF-8(在Python 3中)的文件不应该有编码声明。
>
> 在标准库中，非默认编码应该只用于测试目的，或者当注释或文档字符串需要提到包含非ascii字符的作者名称时;
> 否则，使用\x、\u、\U或\N转义是在字符串字面量中包含非ascii数据的首选方法。
>
> 对于Python 3.0及以上版本，为标准库规定了以下策略(参见PEP 3131):
> Python标准库中的所有标识符必须仅使用ascii标识符，
> 并应在可行的情况下使用英语单词(在许多情况下，使用非英语的缩写和技术术语)。
> 此外，字符串字面值和注释也必须是ASCII格式。
> 唯一的例外是(a)测试非ascii特性的测试用例和(b)作者姓名。
> 名称不是基于拉丁字母(Latin -1, ISO/IEC 8859-1字符集)的作者必须提供其名称在该字符集中的音译。
>
> 鼓励具有全球受众的开源项目采用类似的政策。

### 导入

Imports should usually be on separate lines:

> 导入通常应该在单独的行:

```python
# Correct:
import os
import sys
```

```python
# Wrong:
import sys, os
```

It's okay to say this though:

> 不过这样写也可以:

```python
# Correct:
from subprocess import Popen, PIPE
```

Imports are always put at the top of the file,
just after any module comments and docstrings,
and before module globals and constants.

Imports should be grouped in the following order:

Standard library imports.

1. Related third party imports.
2. Local application/library specific imports.
3. You should put a blank line between each group of imports.

Absolute imports are recommended,
as they are usually more readable and tend to be better behaved
(or at least give better error messages) if the import system is
incorrectly configured
(such as when a directory inside a package ends up on sys.path):

> 导入总是放在文件的顶部，就在任何模块注释和文档字符串之后，模块全局变量和常量之前。
>
> 进口应按以下顺序分组:
>
> 标准库进口。
>
> 1. 相关第三方进口。
> 2. 特定于本地应用程序/库的导入。
> 3. 您应该在每组导入之间放一个空白行。
>
> 推荐使用绝对导入，因为如果导入系统配置错误(比如包中的目录在sys.path上结束时)，
> 绝对导入通常更容易读懂，而且往往表现得更好(或者至少给出更好的错误消息):

```python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

However, explicit relative imports are an acceptable
alternative to absolute imports,
especially when dealing with complex package layouts where
using absolute imports would be unnecessarily verbose:

> 然而，显式相对导入是绝对导入的一种可接受的替代方法，
> 特别是在处理复杂的包布局时，使用绝对导入会不必要地冗长:

```python
from . import sibling
from .sibling import example
```

Standard library code should avoid complex package layouts
and always use absolute imports.

Implicit relative imports should never be used and
have been removed in Python 3.

When importing a class from a class-containing module,
it's usually okay to spell this:

> 标准库代码应该避免复杂的包布局，并始终使用绝对导入。
>
> 隐式相对导入永远不应该被使用，并且在Python 3中已经被删除。
>
> 当从包含类的模块导入类时，通常可以这样拼写:

```python
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

If this spelling causes local name clashes, then spell them explicitly:

> 如果这种拼写导致本地名称冲突，则显式地拼写它们:

```python
import myclass
import foo.bar.yourclass
```

and use "myclass.MyClass" and "foo.bar.yourclass.YourClass".

Wildcard imports (from \<module> import *) should be avoided,
as they make it unclear which names are present in the namespace,
confusing both readers and many automated tools.
There is one defensible use case for a wildcard import,
which is to republish an internal interface as part of a public API
(for example, overwriting a pure Python implementation of
an interface with the definitions from an optional accelerator module
and exactly which definitions will be overwritten isn't known in advance).

When republishing names this way,
the guidelines below regarding public and internal interfaces still apply.
并使用“myclass.MyClass”和“foo.bar.yourclass.YourClass”。

> 应该避免通配符导入(from import *)，因为它们使命名空间中出现的名称不清楚，
> 使读者和许多自动化工具感到困惑。有一个站得住脚的通配符导入用例,
> 这是重新发布一个内部接口作为公共API的一部分
> (例如,覆盖一个纯Python实现一个接口的定义从一个可选的加速器模块和哪些定义将被重写不是提前知道)。
>
> 当以这种方式重新发布名称时，下面关于公共和内部接口的指导原则仍然适用。

### 模块级别Dunder名称

Module level "dunders" (i.e. names with two leading and two trailing
underscores) such as \_\_all\_\_, \_\_author\_\_, \_\_version\_\_, etc.
should be placed after the module docstring but before any import
statements except from \_\_future\_\_ imports.
Python mandates that future-imports must appear in the module before
any other code except docstrings:

> 模块级别的"dunders"(即带有两个前导下划线和两个尾随下划线的名称)，
> 如\_\_all\_\_， \_\_author\_\_， \_\_version\_\_等，应该放在模块文档字符串之后，
> 但在除\_\_future\_\_ imports之外的任何导入语句之前。
> Python要求future-imports必须出现在模块中除文档字符串之外的任何其他代码之前:

```python
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

## 字符串引号

In Python, single-quoted strings and double-quoted strings are the same.
This PEP does not make a recommendation for this. Pick a rule and stick to it.
When a string contains single or double quote characters, however,
use the other one to avoid backslashes in the string. It improves readability.

For triple-quoted strings, always use double quote characters to be
consistent with the docstring convention in PEP 257.

> 在Python中，单引号字符串和双引号字符串是相同的。此PEP并不对此提出建议。
> 选择一个规则并坚持下去。但是，当字符串包含单引号或双引号字符时，
> 使用另一个字符来避免字符串中的反斜杠。它提高了可读性。
>
> 对于三引号字符串，总是使用双引号字符，以与PEP 257中的docstring约定保持一致。

## 表达式和语句中的空格

### 厌恶的东西

Avoid extraneous whitespace in the following situations:

Immediately inside parentheses, brackets or braces:

> 在以下情况下避免不必要的空格:
>
> 紧接在括号、方括号或大括号内的:

```python
# Correct:
spam(ham[1], {eggs: 2})
```

```python
# Wrong:
spam( ham[ 1 ], { eggs: 2 } )
```

Between a trailing comma and a following close parenthesis:

> 在尾随逗号和后面的右括号之间:

```python
# Correct:
foo = (0,)
```

```python
# Wrong:
bar = (0, )
```

Immediately before a comma, semicolon, or colon:

> 紧接在逗号、分号或冒号之前:

```python
# Correct:
if x == 4: print x, y; x, y = y, x
```

```python
# Wrong:
if x == 4 : print x , y ; x , y = y , x
```

However, in a slice the colon acts like a binary operator,
and should have equal amounts on either side
(treating it as the operator with the lowest priority).
In an extended slice, both colons must have the same amount of spacing applied.
Exception: when a slice parameter is omitted, the space is omitted:

> 然而，在切片中，冒号的作用就像一个二进制操作符，
> 并且应该在任意一边都有相同的数量(将其视为具有最低优先级的操作符)。
> 在扩展片中，两个冒号必须应用相同的间距。当一个切片参数被省略时，空格被省略:

```python
# Correct:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
```

```python
# Wrong:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```

Immediately before the open parenthesis that starts the argument
list of a function call:

> 紧接在函数调用的参数列表开始的左括号之前:

```python
# Correct:
spam(1)
```

```python
# Wrong:
spam (1)
```

Immediately before the open parenthesis that starts an indexing or slicing:

> 紧接在开始索引或切片的左括号之前:

```python
# Correct:
dct['key'] = lst[index]
```

```python
# Wrong:
dct ['key'] = lst [index]
```

More than one space around an assignment (or other)
operator to align it with another:

> 在赋值操作符(或其他操作符)周围有一个以上的空格，使其与另一个对齐:

```python
# Correct:
x = 1
y = 2
long_variable = 3
```

```python
# Wrong:
x             = 1
y             = 2
long_variable = 3
```

### 其他建议

Avoid trailing whitespace anywhere. Because it's usually invisible,
it can be confusing: e.g. a backslash followed by a space and a
newline does not count as a line continuation marker.
Some editors don't preserve it and many projects (like CPython itself)
have pre-commit hooks that reject it.

Always surround these binary operators with a single space on either side:
assignment (=), augmented assignment (+=, -= etc.),
comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not),
Booleans (and, or, not).

If operators with different priorities are used, consider adding
whitespace around the operators with the lowest priority(ies).
Use your own judgment; however, never use more than one space,
and always have the same amount of whitespace on both
sides of a binary operator:

> 在任何地方都要避免尾随空格。因为它通常是看不见的，它可能会令人困惑:
> 例如，一个反斜杠后跟一个空格和一个换行符不算作是行延续标记。
> 有些编辑器不会保留它，很多项目(比如CPython本身)都有拒绝它的预提交钩子。
>
> 总是在这些二进制操作符的两边用一个空格包围:赋值(=)，增强赋值(+=，-=等)，
> 比较(==，<，>，!=，<>，<=，>=，in, not in, is, is not)，布尔值(and, or, not)。
>
> 如果使用不同优先级的操作符，可以考虑在最低优先级的操作符周围添加空格。
> 使用你自己的判断;然而，永远不要使用多于一个的空格，并且总是在二元操作符的两边使用相同数量的空格:

```python
# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

```python
# Wrong:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

Function annotations should use the normal rules for colons and
always have spaces around the -> arrow if present.
(See Function Annotations below for more about function annotations.):

> 函数注释应该使用冒号的常规规则，并且在->箭头周围总是有空格(如果有的话)。
> (关于函数注释的更多信息，请参见下面的函数注释):

```python
# Correct:
def munge(input: AnyStr): ...
def munge() -> PosInt: ...
```

```python
# Wrong:
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```

Don't use spaces around the = sign when used to indicate a keyword argument,
or when used to indicate a default value for an unannotated function parameter:

> 当用于指示关键字参数或用于指示未注释函数形参的默认值时，不要在=号周围使用空格:

```python
# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```

```python
# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

When combining an argument annotation with a default value,
however, do use spaces around the = sign:

> 但是，当将参数注释与默认值组合在一起时，请务必在=号周围使用空格:

```python
# Correct:
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```

```python
# Wrong:
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```

Compound statements (multiple statements on the same line)
are generally discouraged:

> 通常不鼓励使用复合语句(在同一行上有多个语句):

```python
# Correct:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
```

Rather not:

> 而不是:

```python
# Wrong:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()
```

While sometimes it's okay to put an if/for/while with a
small body on the same line, never do this for multi-clause statements.
Also avoid folding such long lines!

Rather not:

> 虽然有时可以把if/for/ While和一个小主体放在同一行，但是不要在多子句语句中这样做。
> 也不要折这么长的线!
>
> 而不是:

```python
# Wrong:
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()
```

Definitely not:

> 绝对不是:

```python
# Wrong:
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()
```

## 何时使用尾随逗号

Trailing commas are usually optional,
except they are mandatory when making a tuple of one element
(and in Python 2 they have semantics for the print statement).
For clarity, it is recommended to surround the latter in
(technically redundant) parentheses:

> 尾随逗号通常是可选的，除非在创建一个元素的元组时它们是强制性的
> (在Python 2中，它们有print语句的语义)。
> 为了清晰起见，建议将后者用括号括起来(技术上是多余的):

```python
# Correct:
FILES = ('setup.cfg',)
```

```python
# Wrong:
FILES = 'setup.cfg',
```

When trailing commas are redundant, they are often helpful when a
version control system is used, when a list of values,
arguments or imported items is expected to be extended over time.
The pattern is to put each value (etc.) on a line by itself,
always adding a trailing comma, and add the close
parenthesis/bracket/brace on the next line.
However it does not make sense to have a trailing comma on the
same line as the closing delimiter
(except in the above case of singleton tuples):

> 如果尾逗号是多余的，那么当使用版本控制系统时，
> 当一个值、参数或导入项的列表希望随时间扩展时，它们通常是有用的。
> 该模式是将每个值(等等)单独放在一行中，总是添加一个尾随逗号，
> 并在下一行添加右括号/方括号/大括号。
> 然而，在同一行有一个逗号作为结束分隔符是没有意义的(除了在上面的单例元组的情况):

```python
# Correct:
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
```

```python
# Wrong:
FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)
```

## 注释

Comments that contradict the code are worse than no comments.
Always make a priority of keeping the comments up-to-date when the code changes!

Comments should be complete sentences.
The first word should be capitalized,
unless it is an identifier that begins with a lower case letter
(never alter the case of identifiers!).

Block comments generally consist of one or more paragraphs built
out of complete sentences, with each sentence ending in a period.

You should use two spaces after a sentence-ending period in
multi- sentence comments, except after the final sentence.

Ensure that your comments are clear and easily understandable
to other speakers of the language you are writing in.

Python coders from non-English speaking countries:
please write your comments in English,
unless you are 120% sure that the code will never be read by
people who don't speak your language.

> 违背代码的注释比没有注释更糟糕。当代码发生变化时，总是优先保持注释的更新!
>
> 注释应该是完整的句子。第一个单词应该大写，除非它是以小写字母开头的标识符
> (永远不要改变标识符的大小写!)
>
> 块注释通常由一个或多个由完整句子组成的段落组成，每个句子以句号结尾。
>
> 在多句注释中，除最后一句话外，在句点后应该使用两个空格。
>
> 确保你的评论是清晰的，容易被其他使用你所写语言的人理解。
>
> 来自非英语国家的Python程序员:请用英语写注释，除非你120%确信代码不会被不讲你的语言的人阅读。

### 块注释

Block comments generally apply to some (or all) code that follows them,
and are indented to the same level as that code.
Each line of a block comment starts with a # and a single space
(unless it is indented text inside the comment).

Paragraphs inside a block comment are separated by a line containing a single #.

> 块注释通常应用于它们后面的一些(或所有)代码，并且缩进到与该代码相同的级别。
> 块注释的每一行都以#和一个空格开始(除非它是注释中的缩进文本)。
>
> 块注释中的段落由包含单个#的行分隔。

### 内联注释

Use inline comments sparingly.

An inline comment is a comment on the same line as a statement.
Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.

Inline comments are unnecessary and in fact distracting if they
state the obvious. Don't do this:

> 尽量少使用内联注释。
>
> 内联注释是与语句在同一行的注释。内联注释应该用至少两个空格与语句隔开。它们应该以#和一个空格开始。
>
> 内嵌的注释是不必要的，事实上，如果他们陈述了明显的问题，就会分散注意力。不要这样做:

```python
x = x + 1                 # Increment x
```

But sometimes, this is useful:

> 但有时，这是有用的:

```python
x = x + 1                 # Compensate for border
```

### 文档字符串

Conventions for writing good documentation strings (a.k.a. "docstrings")
are immortalized in PEP 257.

Write docstrings for all public modules, functions, classes, and methods.
Docstrings are not necessary for non-public methods,
but you should have a comment that describes what the method does.
This comment should appear after the def line.

PEP 257 describes good docstring conventions. Note that most importantly,
the """ that ends a multiline docstring should be on a line by itself:

> 编写好的文档字符串的约定。“文档字符串”)在PEP 257中永久保存。
>
> 为所有公共模块、函数、类和方法编写文档字符串。文档字符串对于非公共方法不是必需的，
> 但是您应该有一个注释来描述该方法的功能。这个注释应该出现在def行之后。
>
> PEP 257描述了良好的文档字符串约定。请注意，最重要的是，结束多行文档字符串的"""应该单独在一行上:

```python
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
```

For one liner docstrings, please keep the closing """ on the same line:

> 对于一行文档字符串，请保持结尾"""在同一行:

```python
"""Return an ex-parrot."""
```

## 命名规定

The naming conventions of Python's library are a bit of a mess,
so we'll never get this completely consistent -- nevertheless,
here are the currently recommended naming standards.
New modules and packages (including third party frameworks)
should be written to these standards, but where an existing library
has a different style, internal consistency is preferred.
> Python库的命名约定有点混乱，所以我们永远不会完全一致——尽管如此，以下是目前推荐的命名标准。
> 应该根据这些标准编写新的模块和包(包括第三方框架)，但是如果现有的库有不同的风格，最好保持内部一致性。

### 压倒一切的原则

Names that are visible to the user as public parts of the API
should follow conventions that reflect usage rather than implementation.

> 作为API公共部分对用户可见的名称应该遵循反映用法而不是实现的约定。

### 描述_命名样式

There are a lot of different naming styles. It helps to be able to recognize
what naming style is being used, independently from what they are used for.

The following naming styles are commonly distinguished:

b (single lowercase letter)

B (single uppercase letter)

lowercase

lower_case_with_underscores

UPPERCASE

UPPER_CASE_WITH_UNDERSCORES

CapitalizedWords (or CapWords, or CamelCase -- so named because of the
bumpy look of its letters [4]). This is also sometimes known as StudlyCaps.

Note: When using acronyms in CapWords, capitalize all the letters of
the acronym. Thus HTTPServerError is better than HttpServerError.

mixedCase (differs from CapitalizedWords by initial lowercase character!)

Capitalized_Words_With_Underscores (ugly!)

There's also the style of using a short unique prefix to group related
names together. This is not used much in Python, but it is mentioned
for completeness. For example, the os.stat() function returns a tuple
whose items traditionally have names like st_mode, st_size,
st_mtime and so on. (This is done to emphasize the correspondence with
the fields of the POSIX system call struct, which helps programmers
familiar with that.)

The X11 library uses a leading X for all its public functions.
In Python, this style is generally deemed unnecessary because attribute
and method names are prefixed with an object, and function names are
prefixed with a module name.

In addition, the following special forms using leading or trailing
underscores are recognized (these can generally be combined with
any case convention):

_single_leading_underscore: weak "internal use" indicator. E.g. from
M import * does not import objects whose names start with an underscore.

single_trailing_underscore_: used by convention to avoid conflicts
with Python keyword, e.g.

> 有很多不同的命名风格。它有助于识别所使用的命名风格，而不依赖于它们的用途。
>
> 以下命名风格通常是区分的:
>
> b(单小写字母)
>
> B(单个大写字母)
>
> 小写字母
>
> lower_case_with_underscores
>
> 大写字母
>
> UPPER_CASE_WITH_UNDERSCORES
>
> 大写的单词(或者CapWords，或者CamelCase——之所以这样命名是因为它的字母[4]看起来很凹凸不平)。
> 有时也被称为StudlyCaps。
>
> 注意:在CapWords中使用首字母缩略词时，首字母缩略词的所有字母都要大写。
> 因此，HTTPServerError比HTTPServerError更好。
>
> 混合大小写(不同于大写字母的字母!)
>
> Capitalized_Words_With_Underscores(丑!)
>
> 还有一种风格是使用简短的唯一前缀将相关的名称组合在一起。这在Python中使用得并不多，
> 但是为了完整性起见才提到它。例如，os.stat()函数返回一个元组，
> 其项的名称通常是st_mode、st_size、st_mtime等。
> (这样做是为了强调与POSIX系统调用结构的字段的对应关系，这有助于程序员熟悉POSIX系统调用结构。)
>
> X11库对其所有公共函数使用前导X。在Python中，这种风格通常被认为是不必要的，
> 因为属性和方法名都以对象作为前缀，函数名则以模块名作为前缀。
>
> 此外，可以识别以下使用首下划线或尾下划线的特殊形式(它们通常可以与任何大小写约定组合):
>
> _single_leading_下划线:弱“内部使用”指示符。例如from M import *不导入名称以下划线开头的对象。
>
> single_trailing_underscore_:按惯例使用，以避免与Python关键字发生冲突，例如。

```python
tkinter.Toplevel(master, class_='ClassName')
```

_double_leading_underscore: when naming a class attribute,
invokes name mangling
(inside class FooBar, \_\_boo becomes \_FooBar__boo; see below).

\_\_double_leading_and_trailing_underscore\_\_:
"magic" objects or attributes that live in user-controlled namespaces.
E.g. \_\_init\_\_, \_\_import\_\_ or \_\_file\_\_. Never invent such names;
only use them as documented.

> \_\_double_leading\_下划线:当命名类属性时，
> 调用名称mangling(在类FooBar中，\_\_boo变成了\_FooBar__boo;见下文)。
>
> \_\_double_leading_and_trailing_underscore\_\_:
> “magic”对象或属性，存在于用户控制的名称空间中。
> 例如:\_\_init\_\_， \_\_import\_\_或\_\_file\_\_。永远不要捏造这样的名字;只在文档中使用它们。

### 规定_命名约定

#### 名称以避免

Never use the characters 'l' (lowercase letter el),
'O' (uppercase letter oh), or 'I' (uppercase letter eye) as
single character variable names.

In some fonts, these characters are indistinguishable from
the numerals one and zero. When tempted to use 'l', use 'L' instead.

> 不要使用字母'l'(小写字母el)， 'O'(大写字母oh)，或'I'(大写字母eye)作为单字符变量名。
>
> 在某些字体中，这些字符与数字1和0无法区分。当你想用“l”的时候，就用“l”代替。

#### ASCII兼容性

Identifiers used in the standard library must be ASCII compatible as
described in the policy section of PEP 3131.

> 标准库中使用的标识符必须与ASCII兼容，如PEP 3131的policy部分所述。

#### 包和模块名

Modules should have short, all-lowercase names.
Underscores can be used in the module name if it improves readability.
Python packages should also have short, all-lowercase names,
although the use of underscores is discouraged.

When an extension module written in C or C++ has an accompanying
Python module that provides a higher level (e.g. more object oriented)
interface, the C/C++ module has a leading underscore (e.g. _socket).

> 模块应该有简短的、全小写的名称。如果可以提高可读性，可以在模块名中使用下划线。
> Python包也应该有简短的、全小写的名称，尽管不鼓励使用下划线。
>
> 当用C或c++编写的扩展模块附带提供更高级别(例如更多面向对象的)接口的Python模块时，
> C/ c++模块前导有下划线(例如_socket)。

#### 类名

Class names should normally use the CapWords convention.

The naming convention for functions may be used instead in
cases where the interface is documented and used primarily as a callable.

Note that there is a separate convention for builtin names:
most builtin names are single words (or two words run together),
with the CapWords convention used only for exception names
and builtin constants.

> 类名通常应该使用CapWords约定。
>
> 在接口被记录并主要作为可调用对象使用的情况下，可以使用函数的命名约定。
>
> 注意，对于内置名称有一个单独的约定:大多数内置名称是单个单词(或两个单词组合在一起)，
> 而CapWords约定仅用于异常名称和内置常量。

#### 类型变量名

Names of type variables introduced in PEP 484 should
normally use CapWords preferring short names:
T, AnyStr, Num. It is recommended to add suffixes \_co or \_contra to the
variables used to declare covariant or contravariant behavior correspondingly:

> PEP 484中引入的类型变量的名称通常应该使用CapWords，而不是短名称:
> T, AnyStr, Num.建议在用于声明协变或逆变行为的变量上添加后缀_co或_contra:

```python
from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)
```

#### 异常的名字

Because exceptions should be classes, the class naming convention applies here.
However, you should use the suffix "Error" on your exception names
(if the exception actually is an error).

> 因为异常应该是类，所以类命名约定在这里适用。
> 然而，你应该在你的异常名称上使用后缀“Error”(如果异常实际上是一个错误)。

#### 全局变量名

(Let's hope that these variables are meant for use inside one module only.)
The conventions are about the same as those for functions.

Modules that are designed for use via from M import * should use the \_\_all\_\_
mechanism to prevent exporting globals, or use the older convention of
prefixing such globals with an underscore
(which you might want to do to indicate these globals are "module non-public").

> (让我们希望这些变量只在一个模块中使用。)约定与函数的约定大致相同。
>
> 为使用via from M import *而设计的模块应该使用__all__机制来防止导出全局变量，
> 或者使用以前的约定，在这些全局变量前面加下划线(你可能想这样做，以表明这些全局变量是“模块非公共的”)。

#### 函数和变量名

Function names should be lowercase, with words separated by underscores
as necessary to improve readability.

Variable names follow the same convention as function names.

mixedCase is allowed only in contexts where that's already the prevailing
style (e.g. threading.py), to retain backwards compatibility.

> 函数名应该小写，单词之间用下划线分隔，以提高可读性。
>
> 变量名遵循与函数名相同的约定。
>
> mixedCase只允许在已经是主流风格的上下文中使用(例如threading.py)，以保持向后兼容性。

#### 函数和方法参数

Always use self for the first argument to instance methods.

Always use cls for the first argument to class methods.

If a function argument's name clashes with a reserved keyword,
it is generally better to append a single trailing underscore rather than
use an abbreviation or spelling corruption. Thus class_ is better than clss.
(Perhaps better is to avoid such clashes by using a synonym.)

> 总是使用self作为实例方法的第一个参数。
>
> 始终使用cls作为类方法的第一个参数。
>
> 如果函数参数的名称与保留关键字冲突，通常最好在后面附加一个下划线，而不是使用缩写或拼写错误。
> 因此，class_比clss好。(也许最好是使用同义词来避免这种冲突。)

#### 方法名称和实例变量

Use the function naming rules: lowercase with words separated by
underscores as necessary to improve readability.

Use one leading underscore only for non-public methods and instance variables.

To avoid name clashes with subclasses, use two leading underscores to invoke
Python's name mangling rules.

Python mangles these names with the class name: if class Foo has an attribute
named __a, it cannot be accessed by Foo.__a.
(An insistent user could still gain access by calling Foo._Foo__a.) Generally,
double leading underscores should be used only to avoid name conflicts with
attributes in classes designed to be subclassed.

Note: there is some controversy about the use of __names (see below).

> 使用函数命名规则:小写，单词用下划线分隔，以提高可读性。
>
> 只对非公共方法和实例变量使用前下划线。
>
> 为了避免与子类的名称冲突，可以使用两个前导下划线来调用Python的名称转换规则。
>
> Python用类名来修改这些名称:如果类Foo有一个名为__a的属性，它不能被Foo.__a访问。
> (一个坚持的用户仍然可以通过调用Foo._Foo__a获得访问权限。)通常，
> 双前导下划线应该只用于避免与设计为子类的类中的属性的名称冲突。
>
> 注意:对于__name的使用存在一些争议(见下文)。

#### 常量

Constants are usually defined on a module level and written in all capital
letters with underscores separating words.
Examples include MAX_OVERFLOW and TOTAL.

> 常量通常定义在模块级别上，用大写字母和下划线分隔单词。例如MAX_OVERFLOW和TOTAL。

#### 设计继承

Always decide whether a class's methods and instance variables
(collectively: "attributes") should be public or non-public. If in doubt,
choose non-public; it's easier to make it public later than to make a public
attribute non-public.

Public attributes are those that you expect unrelated clients of your class
to use, with your commitment to avoid backwards incompatible changes.
Non-public attributes are those that are not intended to be used by third
parties; you make no guarantees that non-public attributes won't change or
even be removed.

We don't use the term "private" here, since no attribute is really private
in Python (without a generally unnecessary amount of work).

Another category of attributes are those that are part of the "subclass API"
(often called "protected" in other languages). Some classes are designed to
be inherited from, either to extend or modify aspects of the class's behavior.
When designing such a class, take care to make explicit decisions about which
attributes are public, which are part of the subclass API, and which are truly
only to be used by your base class.

With this in mind, here are the Pythonic guidelines:

Public attributes should have no leading underscores.

If your public attribute name collides with a reserved keyword, append a single
trailing underscore to your attribute name. This is preferable to an
abbreviation or corrupted spelling. (However, notwithstanding this rule,
'cls' is the preferred spelling for any variable or argument which is known
to be a class, especially the first argument to a class method.)

Note 1: See the argument name recommendation above for class methods.

For simple public data attributes, it is best to expose just the attribute
name, without complicated accessor/mutator methods. Keep in mind that Python
provides an easy path to future enhancement, should you find that a simple
data attribute needs to grow functional behavior. In that case, use properties
to hide functional implementation behind simple data attribute access syntax.

Note 1: Properties only work on new-style classes.

Note 2: Try to keep the functional behavior side-effect free, although
side-effects such as caching are generally fine.

Note 3: Avoid using properties for computationally expensive operations;
the attribute notation makes the caller believe that access is
(relatively) cheap.

If your class is intended to be subclassed, and you have attributes that
you do not want subclasses to use, consider naming them with double leading
underscores and no trailing underscores. This invokes Python's name
mangling algorithm, where the name of the class is mangled into the attribute
name. This helps avoid attribute name collisions should subclasses
inadvertently contain attributes with the same name.

Note 1: Note that only the simple class name is used in the mangled name,
so if a subclass chooses both the same class name and attribute name,
you can still get name collisions.

Note 2: Name mangling can make certain uses, such as debugging and
\_\_getattr__(), less convenient. However the name mangling algorithm is
well documented and easy to perform manually.

Note 3: Not everyone likes name mangling. Try to balance the need to
avoid accidental name clashes with potential use by advanced callers.

> 总是决定一个类的方法和实例变量(统称为“属性”)应该是公共的还是非公共的。如果有疑问，选择非公开的;
> 稍后将其公开要比将公共属性非公开容易。
>
> 公共属性是希望类的不相关客户端使用的属性，并承诺避免向后不兼容的更改。
> 非公开属性是指不打算由第三方使用的属性;您不能保证非公共属性不会改变，甚至不会被删除。
>
> 这里我们不使用术语“私有”，因为在Python中没有真正私有的属性(通常没有不必要的工作量)。
>
> 另一类属性是“子类API”(在其他语言中通常称为“受保护的”)的一部分。有些类被设计为继承自，
> 扩展或修改类行为的某些方面。在设计这样的类时，要注意明确哪些属性是公共的，哪些是子类API的一部分，
> 哪些真正只供基类使用。
>
> 记住这一点，下面是python的指导方针:
>
> 公共属性不应该有前导下划线。
>
> 如果公共属性名与保留关键字冲突，请在属性名后追加一个下划线。这比缩写或错误的拼写更可取。
> (然而，尽管有这个规则，'cls'是任何已知是类的变量或参数的首选拼写，特别是类方法的第一个参数。)
>
> 注意1:关于类方法，请参阅上面的参数名建议。
>
> 对于简单的公共数据属性，最好只公开属性名，而不公开复杂的访问/修改方法。请记住，
> 如果发现一个简单的数据属性需要扩展函数行为，Python提供了一条易于实现未来增强的路径。
> 在这种情况下，使用属性将函数实现隐藏在简单的数据属性访问语法后面。
>
> 注意1:属性只适用于新型类。
>
> 注意2:尽量避免函数行为的副作用，尽管缓存之类的副作用通常是好的。
>
> 注意3:避免使用属性进行计算昂贵的操作;属性表示法使调用者相信访问是(相对)便宜的。
>
> 如果您的类打算被子类化，并且您有不希望子类使用的属性，
> 请考虑使用双前导下划线和不尾随下划线来命名它们。这将调用Python的名称篡改算法，
> 其中类的名称被篡改为属性名。如果子类无意中包含具有相同名称的属性，这有助于避免属性名称冲突。
>
> 注意1:注意，在错误的名称中只使用简单的类名，所以如果子类同时选择了相同的类名和属性名，
> 您仍然可以得到名称冲突。
>
> 注2:名称mangling可能会使某些用途(如调试和__getattr__())变得不那么方便。
> 然而，名称篡改算法有很好的文档，很容易手动执行。
>
> 注3:并不是每个人都喜欢改名。尽量在避免名字意外冲突和高级呼叫者可能使用的需求之间取得平衡。

### 公共和内部接口

Any backwards compatibility guarantees apply only to public interfaces.
Accordingly, it is important that users be able to clearly distinguish
between public and internal interfaces.

Documented interfaces are considered public, unless the documentation
explicitly declares them to be provisional or internal interfaces exempt
from the usual backwards compatibility guarantees. All undocumented interfaces
should be assumed to be internal.

To better support introspection, modules should explicitly declare the
names in their public API using the \_\_all\_\_ attribute. Setting \_\_all\_\_ to
an empty list indicates that the module has no public API.

Even with \_\_all\_\_ set appropriately, internal interfaces
(packages, modules, classes, functions, attributes or other names)
should still be prefixed with a single leading underscore.

An interface is also considered internal if any containing namespace
(package, module or class) is considered internal.

Imported names should always be considered an implementation detail.
Other modules must not rely on indirect access to such imported names
unless they are an explicitly documented part of the containing module's API,
such as os.path or a package's \_\_init\_\_ module that exposes functionality
from submodules.
> 任何向后兼容性保证都只适用于公共接口。因此，用户能够清楚地区分公共接口和内部接口非常重要。
>
> 文档化的接口被认为是公共的，除非文档显式地声明它们是临时的，
> 或者内部接口不受通常的向后兼容性保证的约束。所有未文档化的接口都应该假定为内部接口。
>
> 为了更好地支持自省，模块应该使用__all__属性在它们的公共API中显式地声明名称。
> 将__all__设置为空列表表明该模块没有公共API。
>
> 即使正确设置了__all__，内部接口(包、模块、类、函数、属性或其他名称)仍然应该在前面加一个下划线。
>
> 如果任何包含的命名空间(包、模块或类)被认为是内部的，那么接口也被认为是内部的。
>
> 导入的名称应该始终被视为实现细节。其他模块不能依赖于对这些导入名称的间接访问，
> 除非它们是包含模块API的显式文档部分，例如os。path或包的__init__模块，该模块公开子模块的功能。

## 编程建议

Code should be written in a way that does not disadvantage other
implementations of Python (PyPy, Jython, IronPython, Cython, Psyco, and such).

For example, do not rely on CPython's efficient implementation of
in-place string concatenation for statements in the form a += b or a = a + b.
This optimization is fragile even in CPython (it only works for some types)
and isn't present at all in implementations that don't use refcounting.
In performance sensitive parts of the library, the ''.join() form should
be used instead. This will ensure that concatenation occurs in linear time
across various implementations.

Comparisons to singletons like None should always be done with is or is not,
never the equality operators.

Also, beware of writing if x when you really mean if x is not None -- e.g. when
testing whether a variable or argument that defaults to None was set to
some other value. The other value might have a type (such as a container)
that could be false in a boolean context!

Use is not operator rather than not ... is. While both expressions are
functionally identical, the former is more readable and preferred:

> 编写代码的方式应该不会对Python的其他实现
> (PyPy、Jython、IronPython、Cython、Psyco等等)造成不利影响。
>
> 例如,不依赖CPython的高效实现就地字符串连接的语句形式a += b或a = a + b。
> 这种优化是脆弱的甚至在CPython的(只适用于某些类型)和不存在在不使用refcounting实现。
> 在库中对性能敏感的部分，应该使用''.join()形式。这将确保在线性时间内跨各种实现进行连接。
>
> 与单例对象(如None)的比较应该始终使用is或is not，而不要使用相等操作符。
>
> 另外，当你真正的意思是如果x不是None时，要注意写if x is not None --例如，
> 当测试一个默认为None的变量或参数是否被设置为其他值时。另一个值的类型(比如容器)
> 在布尔上下文中可能是false !
>
> 使用is not操作符而不是not ... is。虽然这两个表达式在函数上是相同的，但前者可读性更好，更受欢迎:

```python
# Correct:
if foo is not None:
```

```python
# Wrong:
if not foo is None:
```

When implementing ordering operations with rich comparisons,
it is best to implement all six operations
(\_\_eq\_\_, \_\_ne\_\_, \_\_lt\_\_, \_\_le\_\_, \_\_gt\_\_, \_\_ge\_\_) rather than relying
on other code to only exercise a particular comparison.

To minimize the effort involved, the functools.total_ordering()
decorator provides a tool to generate missing comparison methods.

PEP 207 indicates that reflexivity rules are assumed by Python.
Thus, the interpreter may swap y > x with x < y, y >= x with x <= y,
and may swap the arguments of x == y and x != y. The sort() and min()
operations are guaranteed to use the < operator and the max() function
uses the > operator. However, it is best to implement all six operations
so that confusion doesn't arise in other contexts.

Always use a def statement instead of an assignment statement that binds
a lambda expression directly to an identifier:

> 在实现具有丰富比较的排序操作时，最好实现所有6个操作
> (\_\_eq\_\_， \_\_ne\_\_， \_\_lt\_\_， \_\_le\_\_， \_\_gt\_\_， \_\_ge\_\_)，
> 而不是依赖其他代码只执行特定的比较。
>
> 为了减少相关工作，functools.total_order()装饰器提供了一个工具来生成缺失的比较方法。
>
> PEP 207表明自反性规则由Python假定。
> 因此,翻译可能交换y > x x > < y, y = x x < = y,可能交换参数x = = y和! = y。
> 排序()和min()操作保证使用 <操作符和max()函数使用> 操作符。
> 但是，最好实现所有这六个操作，这样在其他上下文中就不会出现混淆。
> 总是使用def语句，而不是直接将lambda表达式绑定到标识符的赋值语句:

```python
# Correct:
def f(x): return 2*x
```

```python
# Wrong:
f = lambda x: 2*x
```

The first form means that the name of the resulting function object is
specifically 'f' instead of the generic '\<lambda>'.
This is more useful for tracebacks and string representations in general.
The use of the assignment statement eliminates the sole benefit a lambda
expression can offer over an explicit def statement
(i.e. that it can be embedded inside a larger expression)

Derive exceptions from Exception rather than BaseException.
Direct inheritance from BaseException is reserved for exceptions where
catching them is almost always the wrong thing to do.

Design exception hierarchies based on the distinctions that code
catching the exceptions is likely to need, rather than the locations where
the exceptions are raised. Aim to answer the question "What went wrong?"
programmatically, rather than only stating that "A problem occurred"
(see PEP 3151 for an example of this lesson being learned for the builtin
exception hierarchy)

Class naming conventions apply here, although you should add the
suffix "Error" to your exception classes if the exception is an error.
Non-error exceptions that are used for non-local flow control or other
forms of signaling need no special suffix.

Use exception chaining appropriately. In Python 3, "raise X from Y"
should be used to indicate explicit replacement without losing the
original traceback.

When deliberately replacing an inner exception
(using "raise X" in Python 2 or "raise X from None" in Python 3.3+),
ensure that relevant details are transferred to the new exception
(such as preserving the attribute name when converting KeyError to
AttributeError, or embedding the text of the original exception in
the new exception message).

When raising an exception in Python 2, use raise ValueError('message')
instead of the older form raise ValueError, 'message'.

The latter form is not legal Python 3 syntax.

The paren-using form also means that when the exception arguments are
long or include string formatting, you don't need to use line continuation
characters thanks to the containing parentheses.

When catching exceptions, mention specific exceptions whenever possible
instead of using a bare except: clause:

> 第一种形式意味着结果函数对象的名称是'f'而不是通用的'\<lambda>'。
> 一般来说，这对于回溯和字符串表示更有用。
> 赋值语句的使用消除了lambda表达式相对于显式def语句所能提供的唯一好处
> (即它可以嵌入到更大的表达式中)
>
> 从Exception而不是BaseException派生异常。从BaseException直接继承为异常保留，
> 在这种情况下捕获它们几乎总是错误的。
>
> 根据捕获异常的代码可能需要的区别来设计异常层次结构，而不是根据引发异常的位置。
> 旨在以编程方式回答“出了什么问题?”，而不是仅仅说明“发生了一个问题”
> (有关内建异常层次结构，请参阅PEP 3151了解本课的一个示例)
>
> 类命名约定适用于这里，但如果异常是错误，则应该在异常类中添加后缀“Error”。
> 用于非本地流控制或其他形式信令的非错误异常不需要特殊的后缀。
>
> 适当使用异常链接。在Python 3中，应该使用"raise X from Y"来表示显式替换，
> 而不会丢失原始的追溯信息。
>
> 当故意更换内部异常(使用Python 2中“提高X”或“提高X从没有“在Python 3.3 +),
> 确保相关信息转移到新异常(如保护属性名称转换KeyError AttributeError时,
> 或嵌入的文本原始异常在新的异常消息)。
>
> 在Python 2中引发异常时，使用raise ValueError('message')代替旧的形式
> raise ValueError, 'message'。
>
> 后一种形式不是合法的Python 3语法。
>
> 使用父类的形式还意味着，当异常参数很长或包含字符串格式时，由于包含圆括号，
> 您不需要使用行延续字符。
>
> 在捕获异常时，尽可能提到特定的异常，而不是使用空的except:子句:

```python
try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None
```

A bare except: clause will catch SystemExit and KeyboardInterrupt
exceptions, making it harder to interrupt a program with Control-C,
and can disguise other problems. If you want to catch all exceptions that
signal program errors, use except Exception: (bare except is equivalent
to except BaseException:).

A good rule of thumb is to limit use of bare 'except' clauses to two cases:

If the exception handler will be printing out or logging the traceback;
at least the user will be aware that an error has occurred.
If the code needs to do some cleanup work, but then lets the exception
propagate upwards with raise. try...finally can be a better way
to handle this case.
When binding caught exceptions to a name, prefer the explicit name
binding syntax added in Python 2.6:

> 一个裸露的except:子句将捕获SystemExit和KeyboardInterrupt异常，
> 使得用Control-C中断程序变得更加困难，并且可以掩盖其他问题。
> 如果您想捕获所有表明程序错误的异常，可以使用except Exception:
> (bare except等价于except BaseException:)。
>
> 一条经验法则是，将“except”子句的使用限制在以下两种情况:
>
> 如果异常处理程序将打印或记录回溯;至少用户会知道发生了错误。
> 如果代码需要做一些清理工作，但随后让异常向上传播提高。试一试……最后可以更好地处理这个案子。
> 当绑定捕捉到一个名称的异常时，请使用Python 2.6中添加的显式名称绑定语法:

```python
try:
    process_data()
except Exception as exc:
    raise DataProcessingFailedError(str(exc))
```

This is the only syntax supported in Python 3, and avoids the ambiguity
problems associated with the older comma-based syntax.

When catching operating system errors, prefer the explicit exception
hierarchy introduced in Python 3.3 over introspection of errno values.

Additionally, for all try/except clauses, limit the try clause to the
absolute minimum amount of code necessary. Again, this avoids masking bugs:

> 这是Python 3中唯一支持的语法，并避免了与基于逗号的旧语法相关的歧义问题。
>
> 当捕捉操作系统错误时，最好使用Python 3.3中引入的显式异常层次结构，而不是errno值的内省。
>
> 此外，对于所有try/except子句，将try子句限制在所需的绝对最小代码量内。同样，这避免了掩蔽漏洞:

```python
# Correct:
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)
```

```python
# Wrong:
try:
    # Too broad!
    return handle_value(collection[key])
except KeyError:
    # Will also catch KeyError raised by handle_value()
    return key_not_found(key)
```

When a resource is local to a particular section of code,
use a with statement to ensure it is cleaned up promptly and
reliably after use. A try/finally statement is also acceptable.

Context managers should be invoked through separate functions or
methods whenever they do something other than acquire and release resources:

> 当某个资源是特定代码段的本地资源时，使用with语句确保在使用后及时、可靠地清理它。
> try/finally语句也可以接受。
>
> 上下文管理器应该通过单独的函数或方法来调用，而不是通过获取和释放资源:

```python
# Correct:
with conn.begin_transaction():
    do_stuff_in_transaction(conn)
```

```python
# Wrong:
with conn:
    do_stuff_in_transaction(conn)
```

The latter example doesn't provide any information to indicate that
the \_\_enter\_\_ and \_\_exit\_\_ methods are doing something other than closing
the connection after a transaction. Being explicit is important in this case.

Be consistent in return statements. Either all return statements in a
function should return an expression, or none of them should. If any return
statement returns an expression, any return statements where no value is
returned should explicitly state this as return None, and an explicit return
statement should be present at the end of the function (if reachable):

> 后一个示例没有提供任何信息来表明__enter__和__exit__方法正在做一些事情，
> 而不是在事务结束后关闭连接。在这种情况下，明确是很重要的。
>
> 在return语句中保持一致。要么函数中的所有返回语句都应该返回一个表达式，要么都不返回。
> 如果任何return语句返回一个表达式，
> 任何没有返回值的return语句都应该显式地将this声明为return None，
> 并且在函数的末尾应该出现一个显式的return语句(如果可到达):

```python
# Correct:

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)
```

```python
# Wrong:

def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)
```

Use string methods instead of the string module.

String methods are always much faster and share the same API
with unicode strings. Override this rule if backwards compatibility
with Pythons older than 2.0 is required.

Use ''.startswith() and ''.endswith() instead of string slicing to
check for prefixes or suffixes.

> startswith() and endswith() are cleaner and less error prone:
> 使用string方法代替string模块。
>
> 字符串方法总是更快，并且与unicode字符串共享相同的API。
> 如果需要与2.0以上的python向后兼容，请重写此规则。
>
> 使用" .startswith()和" .endswith()代替字符串切片来检查前缀或后缀。
>
> startswith()和endswith()更简洁，更不易出错:

```python
# Correct:
if foo.startswith('bar'):
```

```python
# Wrong:
if foo[:3] == 'bar':
```

Object type comparisons should always use
isinstance() instead of comparing types directly:

> 对象类型比较应该总是使用isinstance()而不是直接比较类型:

```python
# Correct:
if isinstance(obj, int):
```

```python
# Wrong:
if type(obj) is type(1):
```

When checking if an object is a string, keep in mind that it might be
a unicode string too! In Python 2, str and unicode have a common base class,
basestring, so you can do:

> 当检查一个对象是否为字符串时，请记住它也可能是一个unicode字符串!在Python 2中，
> str和unicode有一个通用的基类basestring，所以你可以做:

```python
if isinstance(obj, basestring):
```

Note that in Python 3, unicode and basestring no longer exist
(there is only str) and a bytes object is no longer a kind of string
(it is a sequence of integers instead).

For sequences, (strings, lists, tuples), use the fact that empty
sequences are false:

> 请注意，在Python 3中，unicode和basestring不再存在(只有str)，
> bytes对象也不再是一种字符串(而是一个整数序列)。
>
> 对于序列(字符串，列表，元组)，使用空序列为假的事实:

```python
# Correct:
if not seq:
if seq:
```

```python
# Wrong:
if len(seq):
if not len(seq):
```

Don't write string literals that rely on significant trailing whitespace.
Such trailing whitespace is visually indistinguishable and some editors
(or more recently, reindent.py) will trim them.

Don't compare boolean values to True or False using ==:

> 不要写依赖于尾部有效空格的字符串字面值。这样的尾随空格在视觉上是无法区分的，
> 一些编辑器(或者最近的reindent.py)会对它们进行修剪。
>
> 不要使用==来比较布尔值与True或False:

```python
# Correct:
if greeting:
```

```python
# Wrong:
if greeting == True:
```

Worse:

> 更糟糕的是:

```python
# Wrong:
if greeting is True:
```

Use of the flow control statements return/break/continue within the
finally suite of a try...finally, where the flow control statement would
jump outside the finally suite, is discouraged. This is because such
statements will implicitly cancel any active exception that is propagating
through the finally suite:

> 使用流控制语句return/break/continue在最后一套try…最后，
> 不鼓励流控制语句跳到finally套件之外。
> 这是因为这样的语句会隐式地取消在finally套件中传播的任何活动异常:

```python
# Wrong:
def foo():
    try:
        1 / 0
    finally:
        return 42
```

### 变量的注释

> PEP 526引入了变量注释。它们的样式建议类似于上面描述的函数注释:
>
> 模块级变量、类和实例变量以及局部变量的注释应该在冒号后面有一个空格。
>
> 冒号前面不能有空格。
>
> 如果赋值有一个右手边，那么等号两边应该有一个空格:

```python
# Correct:

code: int

class Point:
    coords: Tuple[int, int]
    label: str = '<unknown>'
```

```python
# Wrong:

code:int  # No space after colon
code : int  # Space before colon

class Test:
    result: int=0  # No spaces around equality sign
```

Although the PEP 526 is accepted for Python 3.6,
the variable annotation syntax is the preferred syntax for stub files
on all versions of Python (see PEP 484 for details).

> 尽管Python 3.6接受PEP 526，但变量注释语法是所有Python版本的存根文件的首选语法
> (参见PEP 484了解详细信息)。

### 函数注释

With the acceptance of PEP 484, the style rules for function
annotations are changing.

In order to be forward compatible, function annotations in Python 3
code should preferably use PEP 484 syntax.
(There are some formatting recommendations for annotations in the
previous section.)

The experimentation with annotation styles that was recommended
previously in this PEP is no longer encouraged.

However, outside the stdlib, experiments within the rules of PEP 484
are now encouraged. For example, marking up a large third party library
or application with PEP 484 style type annotations, reviewing how easy
it was to add those annotations, and observing whether their presence
increases code understandability.

The Python standard library should be conservative in adopting such
annotations, but their use is allowed for new code and for big refactorings.

For code that wants to make a different use of function annotations
it is recommended to put a comment of the form:

> 随着PEP 484的接受，函数注释的样式规则发生了变化。
>
> 为了向前兼容，Python 3代码中的函数注释最好使用PEP 484语法。
> (在上一节中有一些关于注释格式的建议。)
>
> 不再鼓励本PEP以前推荐的注释样式试验。
>
> 但是，在stdlib之外，现在鼓励在PEP 484规则内进行实验。
> 例如，用PEP 484风格的类型注释标记大型第三方库或应用程序，检查添加这些注释有多容易，
> 并观察它们的存在是否提高了代码的可理解性。
>
> Python标准库在采用这种注释时应该保持保守，但允许使用它们来编写新代码和进行大型重构。
>
> 对于想要用不同方式使用函数注释的代码，建议在表单中添加注释:

```python
# type: ignore
```

near the top of the file; this tells type checker to ignore all annotations.
(More fine-grained ways of disabling complaints from type checkers can be
found in PEP 484.)

Like linters, type checkers are optional, separate tools. Python
interpreters by default should not issue any messages due to type
checking and should not alter their behavior based on annotations.

Users who don't want to use type checkers are free to ignore them.
However, it is expected that users of third party library packages may want
to run type checkers over those packages. For this purpose PEP 484
recommends the use of stub files: .pyi files that are read by the type
checker in preference of the corresponding .py files. Stub files can be
distributed with a library, or separately
(with the library author's permission) through the typeshed repo [5].

For code that needs to be backwards compatible, type annotations can be
added in the form of comments. See the relevant section of PEP 484 [6].

> 在档案顶部附近;这告诉类型检查器忽略所有注释。
> (在PEP 484中可以找到从类型检查器禁用投诉的更细粒度的方法。)
>
> 像短刺一样，类型检查器是可选的，单独的工具。默认情况下，
> Python解释器不应该因为类型检查而发出任何消息，也不应该基于注释改变它们的行为。
>
> 不想使用类型检查器的用户可以随意忽略它们。然而，第三方库包的用户可能希望在这些包上运行类型检查器。
> 为此，PEP 484建议使用存根文件:.pyi文件，类型检查器优先读取相应的.py文件。
> 存根文件可以与库一起分发，也可以通过typeshed repo[5]单独分发(得到库作者的许可)。
>
> 对于需要向后兼容的代码，可以以注释的形式添加类型注释。请参阅PEP 484[6]的相关章节。

## 参考文献

Footnotes

> [7]Hanging indentation is a type-setting style where all the lines
> in a paragraph are indented except the first line. In the context of Python,
> the term is used to describe a style where the opening parenthesis of a
> parenthesized statement is the last non-whitespace character of the line,
> with subsequent lines being indented until the closing parenthesis.
> 脚注
>
> [7]悬挂缩进是一种排版样式，段落中除第一行外的所有行都缩进。在Python的上下文中，
> 这个术语用来描述这样一种风格:括号括起来的语句的左括号是一行的最后一个非空格字符，
> 随后的行缩进直到右括号。
>
> [1]PEP 7, Style Guide for C Code, van Rossum
>
> [2]Barry's GNU Mailman style guide
> <http://barry.warsaw.us/software/STYLEGUIDE.txt>
>
> [3]Donald Knuth's The TeXBook, pages 195 and 196.
>
> [4]<http://www.wikipedia.com/wiki/CamelCase>
>
> [5]Typeshed repo <https://github.com/python/typeshed>
>
> [6]Suggested syntax for Python 2.7 and straddling code
> <https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code>
>
> [1]PEP 7《C代码风格指南》，van Rossum著
>
> [2]巴里GNU邮差风格指南
> <http://barry.warsaw.us/software/STYLEGUIDE.txt>
> [3]Donald Knuth的的TeXBook，第195和196页。
>
> [4]<http://www.wikipedia.com/wiki/CamelCase>
>
> [5]Typeshed回购<https://github.com/python/typeshed>
>
> [6]Python 2.7和跨代码的建议语法
> <https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code>

## 版权

This document has been placed in the public domain.

Source: <https://github.com/python/peps/blob/master/pep-0008.txt>

> 这份文件已被置于公共领域。
>
> 来源: <https://github.com/python/peps/blob/master/pep-0008.txt>
