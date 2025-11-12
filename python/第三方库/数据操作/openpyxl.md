# openpyxl

## 安装

```bash
pip install openpyxl
```

## 导入模块

```python
import openpyxl
```

## 属性

| 类/方法           | 描述           |
| ----------------- | -------------- |
| `load_workbook()` | 加载Excel文件  |
| `Workbook()`      | 创建新的工作簿 |

### Workbook 类

| 方法/属性                              | 描述                                           |
| -------------------------------------- | ---------------------------------------------- |
| `[]`                                   | 键入sheet名字获取sheet工作表                   |
| `worksheets`                           | 包含所有sheet工作表的列表，通过下标来获取sheet |
| `sheetnames`                           | 包含所有sheet工作表的名字的列表                |
| `create_sheet(title=None, index=None)` | 创建sheet                                      |
| `move_sheet(sheet, offset=0)`          | 移动sheet，形参sheet为sheet或sheet的名字       |
| `copy_worksheet(from_worksheet)`       | 复制sheet                                      |
| `save(filename)`                       | 保存到指定文件                                 |
| `close()`                              | 关闭，只影响只读或只写模式                     |
| `del wb[]`                             | 移除sheet工作表                                |

### Worksheet 类

| 方法/属性                       | 描述                                  |
| ------------------------------- | ------------------------------------- |
| `[]`                            | 下标格式: "A1", "A2", ...，获取单元格 |
| `title`                         | sheet的名字                           |
| `rows`                          | 所有行，以列行排列                    |
| `columns`                       | 所有列，以行列排列                    |
| `max_row`                       | 最大行                                |
| `max_column`                    | 最大列                                |
| `values`                        | 所有单元格的值，以行列排列            |
| `cell(row, column, value=None)` | 单元格                                |
| `column_dimensions[].width`     | 宽                                    |
| `row_dimensions[].height`       | 高                                    |

示例:

```python
import openpyxl

# 创建新工作簿
wb = openpyxl.Workbook()
ws = wb.active

# 设置单元格值
ws['A1'] = 'Hello'
ws['B1'] = 'World'

# 保存文件
wb.save('example.xlsx')
```
