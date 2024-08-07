# C# 连接 SQL Server

数据提供程序: `SQL Server .NET`  

## 命名空间: `System.Data.SqlClient`

| 类 | 描述 |
| --- | --- |
| [`SqlConnection`](#sqlconnection) | 建立与 SQL Server 数据源的连接 |
| [`SqlCommand`](#sqlcommand) | 对 SQL Server 数据源执行命令 |
| `SqlDataAdapter` | 用 SQL Server 数据源填充 DataSet 并解析更新 |
| [`SqlDataReader`](#sqldatareader) | 从 SQL Server 数据源中读取只进且只读的数据流 |

### SqlConnection

用于连接数据库, 返回 `SqlConnection` 对象

语法:

```cs
SqlConnection connection = new SqlConnection(连接字符串);
```

连接字符串格式:  
`Data Source=服务器名称或IP地址; Initial Catalog=数据库名; User ID=用户名; PWD=密码`

- `Data Source`: 指定连接到的服务器名称或 IP 地址, 若将本机作为服务器, 则该参数的值可以是 "." "(local)" "127.0.0.1"
- `Initial Catalog`: 指定将要访问的数据库名称
- `User ID` 或 `UID`: SQL Server 数据库的用户名
- `Password` 或 `PWD`: SQL Server 数据库用户名的密码
- `Integrated Security`: Windows 身份验证, 填写布尔值 (如: True), 如果填写了这个属性则不需要填写数据库用户名和密码

#### SqlConnection 实例属性

| 属性 | 描述 |
| --- | --- |
| `ConnectionString` | 设置/获取应用程序连接数据库的连接字符串 |

| 方法 | 描述 |
| --- | --- |
| [`void Open()`](#sqlconnectionopen) | 用于打开与指定数据库的连接 |
| [`void Close()`](#sqlconnectionclose) | 关闭与数据库的连接 |

#### SqlConnection.Open

连接数据库

示例:

```cs
SqlConnection connection = new SqlConnection(connString); // 创建连接对象
connection.Open(); // 连接数据库
```

#### SqlConnection.Close

关闭数据库连接

示例:

```cs
SqlConnection connection = new SqlConnection(connString);
connection.Open(); // 连接
// ...
connection.Close(); // 关闭数据库
```

### SqlCommand

用于编写数据库指令

语法:

```cs
SqlCommand command = new SqlCommand(string sql, SqlConnection conn);
```

其中第一个参数为要执行的 SQL 语句, 第二个参数为已经创建好的 SqlConnection 对象

#### SqlCommand 实例属性

| 属性 | 描述 |
| --- | --- |
| `Connection` | Command 对象使用的数据库连接 |
| `CommandText` | 要执行的 SQL 语句 |

| 方法 | 描述 |
| --- | --- |
| `SqlDataReader ExecuteReader()` | 可查询多条数据的命令, 返回 DataReader 对象 |
| `Object ExecuteScalar()` | 查询一条数据的命令, 如执行 COUNT(*) |
| `int ExecuteNonQuery()` | 用于执行非查询类的语句, 返回的值是本次操作所影响的行数 |

#### SqlCommand.ExecuteReader

执行查询语句, 返回 SqlDataReader 对象

示例:

```cs
string connString = "Data Source=127.0.0.1; Initial Catalog=Hospital;  UID=sa; PWD=******";
SqlConnection connection = new SqlConnection(connString);
connection.Open();

SqlCommand command = new SqlCommand("SELECT TOP 10 PatientId, PatientName FROM Patient;", connection);
for (SqlDataReader reader = command.ExecuteReader(); reader.Read();)
{
    Console.WriteLine(reader.GetInt32(0)); // 获取该行第一列数据
    Console.WriteLine(reader.GetString(1)); // 获取该行第二列数据
}

connection.Close();
```

#### SqlCommand.ExecuteScalar

执行查询语句, 返回单个对象

示例:

```cs
string connString = "Data Source=.; Initial Catalog=Hospital;  UID=sa; PWD=******";
SqlConnection connection = new SqlConnection(connString);
connection.Open();

SqlCommand command = new SqlCommand("SELECT TOP 1 PatientName FROM Patient;", connection);
object result = command.ExecuteScalar();
Console.WriteLine(result.ToString());

connection.Close();
```

#### SqlCommand.ExecuteNonQuery

执行非查询语句, 返回影响的行数

### SqlDataReader

可以从数据源中读取数据, 每次读取一条记录  
可以通过下标字段名的方式获取当前记录的数据

| 方法 | 描述 |
| --- | --- |
| `bool Read()` | 读取下一条数据, 成功返回 true, 否则 false |
| `void Close()` | 关闭此对象 |
| `string GetString()` | 获取某一列 (从 0 开始) 的值, 返回字符串数据 |
| `int GetInt32()` | 获取某一列的值, 返回整型数据 |

示例可看 [SqlCommand.ExecuteReader 示例](#sqlcommandexecutereader)

### SqlAdapter

数据适配器

语法:

```cs
SqlAdapter adapter = new SqlAdapter(SQL查询语句, Connection连接对象);
```

#### SqlAdapter.Fill

将查询到的数据填充到 DataSet (命名空间: System.Data) 中

示例:

```cs
SqlAdapter adapter = new SqlAdapter("SELECT * FROM Table", conn);
DataSet dataSet = new DataSet();
adapter.Fill(dataSet);
```

## 命名空间: `System.Data`

| 类 | 描述 |
| --- | --- |
| `DataSet` | 数据集合 |
| `DataTableCollection` | 表的集合 |
| `DataTable` | 单个表 |
| `DataColumnCollection` | 列的集合 |
| `DataColumn` | 单个列 |
| `DataRowCollection` | 行的集合 |
| `DataRow` | 单个行 |

以上类都可以通过下标的方式获取其中某个实体
