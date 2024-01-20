"""pygame  模块"""
import pygame


'''
1.游戏开发

导入方式:
    import pygame
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.init()

初始化包
初始化 pygame
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
3.QUIT K_...
一些变量

QUIT  当退出事件发生后，其类型等于该值

K_ 加上按键大写单词就是其对应的 event.key
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
4.surface 对象

像 pygame.display.set_mode()  pygame.image.load() 返回的都是 surface 对象

属性:
    fill()  更新填充背景颜色，传入RGB颜色
    blit()  更新像素，传入 surface 对象，左上角坐标或位置矩阵
    get_rect()  获得图像的位置矩形
        move()  移动图形位置矩阵
        left  矩阵最小x坐标
        right  矩阵最大x坐标
        top  矩阵最小y坐标
        bottom  矩阵最大y坐标
        width  长
        height  宽
        center  中心点坐标
    subsurface()  返回矩阵区域的 surface 对象
    copy()  复制 surface 对象
    convert()  转换格式
    convert_alpha()  转换格式，且每个像素都带有 alpha 通道
    set_colorkey()  设置一种颜色(RGB)的 alpha
    set_alpha()  设置 alpha
    
    get_at()  坐标上的像素信息 RGBA
    set_at()  在坐标上填充 RGBA
'''

print('4.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
5.display
显示
pygame 模块中的一个模块

属性:
    set_mode()  设置窗口大小等参数，返回 surface 对象
        参数:
            size: 元组(width, height)
            flags: pygame.FULLSCREEN 全屏; pygame.HWSURFACE 全屏时硬件加速;
                pygame.DOUBLEBUF 双缓冲; pygame.OPENGL 使用 OpenGL 渲染;
                pygame.RESIZABLE 可调节窗口尺寸;
                pygame.NOFRAMS 窗口没有边框和按钮
                多个选项用按位或(|)分开
    list_modes()  此计算机支持的分辨率
    set_caption()  设置窗口标题
    flip()  刷新界面
'''

print('5.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
6.image
图像
pygame 模块中的一个模块

属性:
    load()  传入图片路径，加载图片，返回 surface 对象
'''

print('6.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
7.transform
旋转，翻转 surface 对象
pygame 模块中的一个模块

属性:
    flip()  翻转，三个参数，surface 对象，是否横向翻转，是否纵向翻转
    scale()  快速缩放 surface 对象
    rotate()  旋转 surface 对象，传入 surface 对象，旋转度数
    rotozoom()  缩放并旋转 surface 对象
    scale2x()  快速放大一倍 surface 对象
    smoothscale()  精准平滑缩放图像，传入 surface 对象和长宽比例
    chop()  裁剪 surface 对象，向中心靠拢
'''

print('7.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
8.event
事件
pygame 模块中的一个模块

属性:
    get()  获取事件，返回字典元素
        其元素的方法属性:
            type  事件类型
'''

print('8.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
9.time
时间
pygame 模块中的一个模块

属性:
    delay()  延迟，以毫秒为单位。相当于 time.sleep
    Clock()  帧率相关
        tick()  设置帧率
'''

print('9.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
10.font
字体
pygame 模块中的一个模块

属性:
    Font()  创建字体对象，参数一字体，默认 None 默认字体，参数二字体大小
        render()  渲染，三个参数，分别是 文本，是否消除锯齿，RGB颜色
        get_linesize()  行高
'''

print('10.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
11.draw
画
pygame 模块中的一个模块

属性:
    rect()  矩形
        surface: 添加到哪个 surface 对象
        color: RGB颜色
        rect: 位置矩阵
        width: 边框宽度，向内扩展，为 0 时填充内部颜色
    polygon()  多边形
        surface: 添加到哪个 surface 对象
        color: RGB颜色
        points: 点的坐标
        width: 边框宽度，向内扩展，为 0 时填充内部颜色
    circle()  圆形:
        surface: 添加到哪个 surface 对象
        color: RGB颜色
        center: 中心点位置
        raidus: 半径
        width: 边框宽度，向内扩展，为 0 时填充内部颜色
    ellipse()  椭圆:
        surface: 添加到哪个 surface 对象
        color: RGB颜色
        rect: 位置矩阵
        width: 边框宽度，向内扩展，为 0 时填充内部颜色
    arc()  弧:
        surface: 添加到哪个 surface 对象
        color: RGB颜色
        rect: 位置矩阵
        start_angle: 起始角度
        stop_angle: 结束角度
        width: 边框宽度，向内扩展，为 0 时不显示
    line()  线:
        surface: 添加到哪个 surface 对象
        color: RGB颜色
        start_pos: 起始角度
        end_pos: 结束角度
        width: 边框宽度，向内扩展，为 0 时不显示
    lines()  线段:
        surface: 添加到哪个 surface 对象
        color: RGB颜色
        closed: 是否和起点坐标相连
        pointlist: 点的坐标
        width: 边框宽度，向内扩展，为 0 时不显示
    aaline()  线(anti-aliasing):
        surface: 添加到哪个 surface 对象
        color: RGB颜色
        start_pos: 起始角度
        end_pos: 结束角度
        blend: 混合背景来达到抗锯齿的目的
    aalines()  线段(anti-aliasing):
        surface: 添加到哪个 surface 对象
        color: RGB颜色
        closed: 是否和起点坐标相连
        pointlist: 点的坐标
        blend: 混合背景来达到抗锯齿的目的
'''

print('11.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
12.mouse
鼠标
pygame 模块中的一个模块

属性:
    get_pos()  鼠标位置
'''

print('12.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
13.surface
pygame 模块中的一个模块

属性:
    Surface()  创建一个 surface 对象
'''

print('13.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
14.sprite
精灵
pygame 模块中的一个模块

属性:
    Sprite()
'''

print('14.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')
