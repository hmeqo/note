# pillow

## 安装

```bash
pip install pillow
```

## 导入模块

```python
from PIL import Image
```

## 属性

| 类/方法        | 描述         |
| -------------- | ------------ |
| `Image.open()` | 打开图像文件 |
| `Image.new()`  | 创建新图像   |
| `Image.save()` | 保存图像     |

### Image 类

| 方法        | 描述         |
| ----------- | ------------ |
| `show()`    | 显示图像     |
| `resize()`  | 调整图像大小 |
| `crop()`    | 裁剪图像     |
| `rotate()`  | 旋转图像     |
| `filter()`  | 应用滤镜     |
| `convert()` | 转换图像模式 |

示例:

```python
from PIL import Image

# 打开图像
img = Image.open('image.jpg')
img.show()

# 调整大小
resized = img.resize((800, 600))
resized.save('resized.jpg')

# 裁剪
cropped = img.crop((100, 100, 400, 400))
cropped.save('cropped.jpg')
```
