# SQL

## 语句

| 语句                                         | 描述 |
| -------------------------------------------- | ---- |
| [`INSERT`](#insert)                          | 增加 |
| [`DELETE`](#delete), [`TRUNCATE`](#truncate) | 删除 |
| [`UPDATE`](#update)                          | 修改 |
| [`SELECT`](#select)                          | 查找 |

### INSERT

插入数据

语法:

```sql
INSERT [INTO] <表名> [(<列>, <列>, ...)]
VALUES (<值>, <值>, ...)
```

插入多行:

```sql
-- VALUES 后面使用多个括号, 
INSERT INTO tablename (column1, column2,...)
VALUES (value1, value2,...),
    (value1, value2,...),
    (value1, value2,...);
```

### SELECT

选择/查询数据

语法:

```sql
SELECT [TOP N] <列名>[, <列名>]
FROM <表名>[, <表名>]
[WHERE <查询条件表达式>]
[ORDER BY <排序的列名>[ASC 或 DESC]]
```

示例:

```sql
-- 查询表的全部数据
SELECT *
FROM tablename;

-- 查询指定列中的数据
SELECT UserName,
    Pwd,
    Age
FROM Tablename;

-- 查询前 20 条数据
SELECT TOP 20 UserName,
    Pwd,
    Age
FROM Tablename;
```

#### AS (别名)

使用 `AS` 关键字给列取别名  
或者显示一个不存在的列, 分别对应值和列名

语法:

```sql
<列名> AS <别名>
<全部列的值> AS <列名>
```

示例:

```sql
-- 给 Name 列和 Age 列取别名
SELECT Name AS 姓名,
    Age AS 年龄
FROM tablename;

-- 增加一个虚拟的列 (民族), 值都是 '汉族'
SELECT Name AS 姓名,
    Age AS 年龄,
    '汉族' AS 名族
FROM tablename;
```

使用空格分隔也可以取别名

示例:

```sql
SELECT Email E
FROM table_name;
```

#### ORDER BY

排序, 可指定排序方式 (ASC 升序, DESC 降序), 默认为 ASC

### UPDATE

更新一行或全表

语法:

```sql
UPDATE <表名> -- 更新某个表
SET <列名> = <值>[, -- 要更新的列
    <列名> = <值>]
[WHERE <列名> = <值>]; -- 给某一行更新数据
```

全表更新示例:

```sql
UPDATE tablename
SET column1 = 'value1',
    column2 = 'value2';
```

给某一行更新数据示例:

```sql
UPDATE tablename
SET column1 = 'value1',
    column2 = 'value2'
WHERE column3 = 'value3';
```

### DELETE

删除一行数据

语法:

```sql
DELETE FROM <表名>
WHERE <列名> = <值>;
```

### TRUNCATE

清空数据或截断数据

语法:

```sql
TRUNCATE TABLE <表名>;
```

## 运算符

### 逻辑运算

| 运算符         | 描述   | 操作数 |
| -------------- | ------ | ------ |
| `AND`          | 并且   | 双目   |
| `OR`           | 或者   | 双目   |
| `NOT`          | 不是   | 单目   |
| `IS NOT`       | 不是   | 双目   |
| `IS NULL`      | 为空   | 单目   |
| `IS NOT NULL`  | 不为空 | 单目   |
| `IS TRUE`      | 为真   | 单目   |
| `IS NOT TRUE`  | 不为真 | 单目   |
| `IS FALSE`     | 为假   | 单目   |
| `IS NOT FALSE` | 不为假 | 单目   |

### 比较运算

| 运算符 | 描述     |
| ------ | -------- |
| `=`    | 等于     |
| `>`    | 大于     |
| `<`    | 小于     |
| `>=`   | 大于等于 |
| `<=`   | 小于等于 |
| `<>`   | 不等于   |
| `!=`   | 不等于   |

## 模糊查询

| 语句                  | 描述         |
| --------------------- | ------------ |
| [`LIKE`](#like)       | 模糊查询     |
| [`BETWEEN`](#between) | 之间         |
| [`IN`](#in)           | 在一个集合中 |

### LIKE

模糊查询

语法:

```sql
WHERE <列名> [NOT] LIKE <表达式>
```

示例:

```sql
-- 匹配邮箱
SELECT *
FROM Info
WHERE Email LIKE '%@%.%';

-- 匹配一个SN和三个字符
SELECT *
FROM Info
WHERE Name LIKE 'SN___';
```

### BETWEEN

在两个数据之间的数据, 两头都包

语法:

```sql
WHERE <列名> [NOT] BETWEEN <数值> AND <数值>
```

示例:

```sql
SELECT *
FROM table_name
WHERE N BETWEEN 10 AND 20;
-- 等价于
SELECT *
FROM table_name
WHERE N >= 10 AND N <= 20
```

### IN

在集合中的数据

语法:

```sql
WHERE <列名> [NOT] IN (<值>, ...)
```

示例:

```sql
SELECT *
FROM table_name
WHERE column IN ('张三', '李四');
```

### 模糊查询通配符

| 通配符 | 描述                                                          |
| ------ | ------------------------------------------------------------- |
| `%`    | 任意长度的字符                                                |
| `_`    | 任意单个字符                                                  |
| `[]`   | 指定范围 (例如 [a-f]) 或集合 (例如 [abcdef]) 内的任何单个字符 |
| `[^]`  | 类似 [], 但取反义, 匹配不在其中的任何单个字符                 |

## 连接查询

| 语句                                    | 描述                                                   |
| --------------------------------------- | ------------------------------------------------------ |
| **内连接查询**                          |                                                        |
| [`INNER JOIN`](#inner-join)             | 查询两张表相匹配部分的数据, 如果其中一张表没有则不匹配 |
| **外连接查询**                          |                                                        |
| [`LEFT OUTER JOIN`](#left-outer-join)   | 查询完整的左表 (从表) 数据, 右表没有的数据显示空值     |
| [`RIGHT OUTER JOIN`](#right-outer-join) | 查询完整的右表 (主表) 数据, 左表没有的数据显示空值     |
| [`FULL OUTER JOIN`](#full-outer-join)   | 查询两张表完整的数据, 没有的数据显示空值               |

### 内连接查询

查询两张表相匹配部分的数据, 如果其中一张表没有则不匹配

#### INNER JOIN

语法:

```sql
FROM <表a> [AS] <a>
    INNER JOIN <表b> [AS] <b> ON <a.b_Id> = <b.Id>
    -- JOIN 后面填写表名, ON 后面填写判断表达式
```

示例:

```sql
SELECT B.Bid,
    B.Bname,
    B.Bprice,
    B.BAuthor,
    C.CategoryName
FROM BookInfo B
    INNER JOIN BooCategory C ON B.CId = C.CategoryCode;
```

#### 通过 WHERE 进行连接查询

语法:

```sql
FROM <表a> [AS] <a>, <表b> [AS] <b>
WHERE <a.b_Id> = <b.Id>;
```

示例:

```sql
SELECT B.Bid,
    B.Bname,
    B.Bprice,
    B.BAuthor,
    C.CategoryName
FROM BookInfo B, BooCategory C
WHERE B.CId = C.CategoryCode;
```

### 外连接查询

#### LEFT OUTER JOIN

查询完整的左表 (从表) 数据, 右表没有的显示空值

语法:

```sql
FROM <表a> [AS] a
    LEFT OUTER JOIN <表b> [AS] b ON <a.b_Id> = <b.Id>
```

示例:

```sql
SELECT B.UserName,
    A.UserId,
    A.BorrowDate,
    A.Status
FROM BorrowInfo A
    LEFT OUTER JOIN UserInfo B ON A.UserId = B.UserId;
```

#### RIGHT OUTER JOIN

查询完整的右表 (主表) 数据, 左表没有的显示空值

语法:

```sql
FROM <表a> [AS] a
    RIGHT OUTER JOIN <表b> [AS] b ON <a.b_Id> = <b.Id>
```

示例:

```sql
SELECT B.UserName,
    A.UserId,
    A.BorrowDate,
    A.Status
FROM BorrowInfo A
    RIGHT OUTER JOIN UserInfo B ON A.UserId = B.UserId;
```

#### FULL OUTER JOIN

查询两张表完整的数据, 没有的显示空值

语法:

```sql
FROM <表a> [AS] a
    FULL OUTER JOIN <表b> [AS] b ON <a.b_Id> = <b.Id>
```

示例:

```sql
SELECT B.UserName,
    A.UserId,
    A.BorrowDate,
    A.Status
FROM BorrowInfo A
    FULL OUTER JOIN UserInfo B ON A.UserId = B.UserId;
```

## 分组查询

### 聚合函数

将一个组内所有元素通过某个函数聚集起来, 变为一个实体, 该实体默认没有列名

| 函数  | 描述             |
| ----- | ---------------- |
| SUM   | 求该列值的和     |
| AVG   | 求该列值的平均值 |
| MIN   | 最小值           |
| MAX   | 最大值           |
| COUNT | 记录的个数       |

### 筛选关键字

紧跟在 SELECT 之后, 像: `SELECT DISTINCT`

| 关键字   | 描述               |
| -------- | ------------------ |
| DISTINCT | 筛选出不重复的记录 |

### GROUP BY

语法:

```sql
SELECT *
FROM <表>
GROUP BY <列>
```

## 表间复制

### 复制并创建新表

如果目标表已存在会报错

语法:

```sql
SELECT * INTO <目标表> FROM <数据表>
```

### 复制到已存在的表

如果目标表不存在会报错

语法:

```sql
INSERT INTO <目标表> SELECT * FROM <数据表>
```

## 模板

一键删除数据库中所有的表, (将下列代码中的 db_test 替换为自己的数据库名运行即可)

```sql
SET @sql = (SELECT concat('DROP TABLE IF EXISTS ', GROUP_CONCAT(table_name), ';') FROM information_schema.tables WHERE table_schema = 'db_test');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```
