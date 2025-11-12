# pygame

## 安装

```bash
pip install pygame
```

## 导入模块

```python
import pygame
```

## 初始化

```python
pygame.init()
```

## 属性

| 模块        | 描述     |
| ----------- | -------- |
| `display`   | 显示管理 |
| `image`     | 图像处理 |
| `transform` | 图像变换 |
| `event`     | 事件处理 |
| `time`      | 时间控制 |
| `font`      | 字体渲染 |
| `draw`      | 绘图功能 |
| `mouse`     | 鼠标输入 |
| `surface`   | 表面对象 |
| `sprite`    | 精灵系统 |

### display 模块

| 方法            | 描述                 |
| --------------- | -------------------- |
| `set_mode()`    | 设置显示窗口         |
| `list_modes()`  | 此计算机支持的分辨率 |
| `set_caption()` | 设置窗口标题         |
| `flip()`        | 更新显示             |

### Surface 类

| 方法              | 描述                                |
| ----------------- | ----------------------------------- |
| `fill()`          | 填充颜色                            |
| `blit()`          | 绘制表面                            |
| `get_rect()`      | 获取矩形区域                        |
| `subsurface()`    | 返回矩阵区域的surface对象           |
| `copy()`          | 复制surface对象                     |
| `convert()`       | 转换格式                            |
| `convert_alpha()` | 转换格式，且每个像素都带有alpha通道 |
| `set_colorkey()`  | 设置一种颜色(RGB)的alpha            |
| `set_alpha()`     | 设置alpha                           |
| `get_at()`        | 坐标上的像素信息RGBA                |
| `set_at()`        | 在坐标上填充RGBA                    |

### event 模块

| 方法    | 描述                                                    |
| ------- | ------------------------------------------------------- |
| `get()` | 获取事件，返回字典元素，其元素的方法属性: type 事件类型 |

### time 模块

| 方法      | 描述                                 |
| --------- | ------------------------------------ |
| `delay()` | 延迟，以毫秒为单位。相当于time.sleep |
| `Clock()` | 帧率相关，tick() 设置帧率            |

### font 模块

| 方法     | 描述                                                                                                                                      |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `Font()` | 创建字体对象，参数一字体，默认None默认字体，参数二字体大小，render()渲染，三个参数，分别是文本，是否消除锯齿，RGB颜色，get_linesize()行高 |

### draw 模块

| 方法        | 描述                                                                                                                                               |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rect()`    | 矩形，surface:添加到哪个surface对象，color:RGB颜色，rect:位置矩阵，width:边框宽度，向内扩展，为0时填充内部颜色                                     |
| `polygon()` | 多边形，surface:添加到哪个surface对象，color:RGB颜色，points:点的坐标，width:边框宽度，向内扩展，为0时填充内部颜色                                 |
| `circle()`  | 圆形，surface:添加到哪个surface对象，color:RGB颜色，center:中心点位置，radius:半径，width:边框宽度，向内扩展，为0时填充内部颜色                    |
| `ellipse()` | 椭圆，surface:添加到哪个surface对象，color:RGB颜色，rect:位置矩阵，width:边框宽度，向内扩展，为0时填充内部颜色                                     |
| `arc()`     | 弧，surface:添加到哪个surface对象，color:RGB颜色，rect:位置矩阵，start_angle:起始角度，stop_angle:结束角度，width:边框宽度，向内扩展，为0时不显示  |
| `line()`    | 线，surface:添加到哪个surface对象，color:RGB颜色，start_pos:起始位置，end_pos:结束位置，width:边框宽度，向内扩展，为0时不显示                      |
| `lines()`   | 线段，surface:添加到哪个surface对象，color:RGB颜色，closed:是否和起点坐标相连，pointlist:点的坐标，width:边框宽度，向内扩展，为0时不显示           |
| `aaline()`  | 线(anti-aliasing)，surface:添加到哪个surface对象，color:RGB颜色，start_pos:起始位置，end_pos:结束位置，blend:混合背景来达到抗锯齿的目的            |
| `aalines()` | 线段(anti-aliasing)，surface:添加到哪个surface对象，color:RGB颜色，closed:是否和起点坐标相连，pointlist:点的坐标，blend:混合背景来达到抗锯齿的目的 |

### image 模块

| 方法     | 描述     |
| -------- | -------- |
| `load()` | 加载图像 |
| `save()` | 保存图像 |

### transform 模块

| 方法            | 描述                                                    |
| --------------- | ------------------------------------------------------- |
| `flip()`        | 翻转，三个参数，surface对象，是否横向翻转，是否纵向翻转 |
| `scale()`       | 快速缩放surface对象                                     |
| `rotate()`      | 旋转surface对象，传入surface对象，旋转度数              |
| `rotozoom()`    | 缩放并旋转surface对象                                   |
| `scale2x()`     | 快速放大一倍surface对象                                 |
| `smoothscale()` | 精准平滑缩放图像，传入surface对象和长宽比例             |
| `chop()`        | 裁剪surface对象，向中心靠拢                             |

### mouse 模块

| 方法        | 描述     |
| ----------- | -------- |
| `get_pos()` | 鼠标位置 |

### sprite 模块

| 类       | 描述 |
| -------- | ---- |
| `Sprite` | 精灵 |

示例:

```python
import pygame

pygame.init()

# 设置窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My Game')

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 填充背景
    screen.fill((255, 255, 255))
    
    # 更新显示
    pygame.display.flip()

pygame.quit()
```
