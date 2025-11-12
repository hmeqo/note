# decimal 模块

用于精确计算小数的模块，避免浮点数计算误差。

导入方式:

```python
import decimal
```

## 属性

### Decimal()

保存精确的十进制数字。因Python计算浮点数会产生误差，所以使用这个来避免误差。

格式：`decimal.Decimal('0.1')`
注意：填入的是一个字符串

示例:

```python
import decimal

print('不使用模块计算 0.1 + 0.2=', 0.1 + 0.2)
print('使用该模块计算 0.1 + 0.2=', decimal.Decimal('0.1') + decimal.Decimal('0.2'))
```

### decimal.getcontext().prec

调整计算精度。

示例:

```python
import decimal

print(decimal.Decimal('1') / decimal.Decimal('3'))

# 保存当前精度
original_prec = decimal.getcontext().prec
# 设置新精度
decimal.getcontext().prec = 100
print(decimal.Decimal('1') / decimal.Decimal('3'))
# 恢复原精度
decimal.getcontext().prec = original_prec
```
