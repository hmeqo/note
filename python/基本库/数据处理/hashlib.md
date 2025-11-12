# hashlib 模块

加密算法。

导入方式:

```python
import hashlib
```

## 属性

### md5() sha1() sha256()

对字符串编码加密。

- md5(): 密文长度 32
- sha1(): 密文长度 40
- sha256(): 密文长度 64

以上返回的对象可用方法属性:

- hexdigest(): 十六进制密文
- update(): 相当于在末尾额外添加字符

示例:

```python
import hashlib

msg = '你好'
p = hashlib.md5(msg.encode('UTF-8'))
print(p.hexdigest())

p = hashlib.sha1(msg.encode('UTF-8'))
print(p.hexdigest())

p = hashlib.sha256(msg.encode('UTF-8'))
print(hashlib.sha256(msg.encode('UTF-8')).hexdigest())

p = hashlib.sha256(msg.encode('UTF-8'))
p.update(msg.encode('UTF-8'))
print(p.hexdigest())

p = hashlib.sha256((2 * msg).encode('UTF-8'))
print(p.hexdigest())
```
