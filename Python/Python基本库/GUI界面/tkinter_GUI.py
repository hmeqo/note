"""tkinter  模块"""
import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.filedialog
import tkinter.simpledialog


'''
1.制作GUI窗口的模块

导入方式:
    import tkinter
'''

print('1.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
2.Tk()

创建一个窗口
注: 必须先创建一个根窗口，才能进行其它操作
Tk()  实例化一个根窗口
Toplevel()  实例化根窗口的顶层窗口，子窗口

以上实例都可使用的方法属性:
    mainloop()  窗口循环显示（一个大的 while 循环）
    quit()  离开 TCL 解释器，所有控件将被销毁
    destroy()  销毁窗口及其所有控件，将终止应用于它的 TCL 解释器
    title() wm_title()  窗口标题，括号中填入字符串
    geometry() wm_geometry()  窗口初始大小和位置（O点在左上角，箭头往右下）
        参数: 
            newGeometry: 传入字符串
                格式: <width>x<height>+<x>+<y>（长乘宽注意是小写 x）
    minsize() wm_minsize()  最小尺寸，参数: x, y
    maxsize() wm_maxsize()  最大尺寸，参数: x, y
    resizable() wm_resizable()  可调整窗口大小
        参数:
            width: 可调整长度，填 0 为不可调整
            height: 可调整高度，填 0 为不可调整
    iconbitmap() wm_iconbitmap()  设置图标，字符串参数填路径
    register()  新创建一个 TCL 函数，参数填入 Python 函数

如果使用 destroy() 窗口无法退出，那么就先调用 quit()
'''

print('2.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
3.=====占位=====
'''

print('3.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
4.Frame() LabelFrame()

框架
提供一个框架，可在里面添加控件
Frame()  普通的框架
LabelFrame()  标签框架
    参数:
        text: 文本
        foreground: 可简写成 fg，前景颜色，填入字符串

以上实例都可用的方法属性:
    master: 上级
    # 以下为 kwargs 参数。不强制填写
    image: 图片，传入 tkinter.PhotoImage() 实例对象
    background: 可简写成 bg，背景颜色
    width: 控件长
    height: 控件宽
    padx: x 轴间距
    pady: y 轴间距
    config: 配置参数
'''

print('4.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
5.pack() grid() place()

放置控件
pack()  上下左右自动放置
    参数:
        # 以下为 kwargs 参数。不强制填写
        side: 位置
            值: 'top'  'bottom'  'left'  'right'（上下左右）
        anchor: 锚，对齐
            值: 'e'  's'  'w'  'n'  'ne'  'nw'  'se'  'sw'
        fiil: 填充空白，值: 'x'  'y'（横向填充，纵向填充）
grid()  网格布局放置
    参数:
        # 以下为 kwargs 参数。不强制填写
        row: 行
        column: 列
        sticky: 粘性，和 pack() 的 anchor 类似
以上实例都可用的方法属性:
    # 以下为 kwargs 参数。不强制填写
    padx: 外部 x 轴间距
    pady: 外部 y 轴间距

place()  放置至指定位置
    参数:
        x: 横坐标
        y: 纵坐标
        anchor: 锚点
'''

print('5.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
6.pack_forget() place_forget() grid_forget() forget()

注: 只能对创建好的控件对象使用
拿起控件
pack_forget()  拿起被 pack() 放置的控件
place_forget()  拿起被 place() 放置的控件
grid_forget()  拿起被 grid() 放置的控件
forget()  看文档好像是只能拿起被 pack() 放置的控件，如果我没理解错

想重新放置使用放置控件的方法即可
'''

print('6.')
print('——————————————————————————————————————————————————')

print('1.', )

print('——————————————————————————————————————————————————')
print('\n')


'''
7.quit() destroy()

销毁控件
quit()  离开 TCL 解释器，所有控件将被销毁。可再次调用 mainloop()
destroy()  销毁窗口及其所有控件，将终止应用于它的 TCL 解释器
'''

print('7.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
8.Label() Button()

控件
Label()  创建一个标签
Entry()  输入框
    参数:
        show: 传入字符串，每个字符用这个字符串的第一个字符显示出来
        validate: 验证输入
            值: 'focus'  'focusin'  'focusout'  'key'  'all'  'none'
            （当获得或失去焦点，获得焦点，失去焦点，被编辑，以上情况，没有）
        validatecommand: 验证时调用的函数
            值可以传入元组，第一个是调用函数，之后是额外参数（将被传入函数）
            可用的额外参数:
                '%d': 0 删除，1 插入，2 获得或失去焦点或 textvariabel 被修改
                '%i': 插入或删除操作的位置索引，其他情况为 -1
                '%P': 输入框最新内容（如果允许修改）
                '%s': 调用函数前的输入框内容
                '%S': 文本被插入或删除的内容
                '%v': 当前 validate 的值
                '%V': 调用原因（'focus'  'focusout'  'forced'）
                '%W': 组件名字
        invalidatecommand: 无效输入（验证函数返回值为 False）时调用的函数
        state: 输入模式
            值: 'readonly'  'disabled'
            （只读，完全禁止）
        takefocus: Tab 键焦点转移，填布尔值
    实例可使用的方法属性:
        get()  获取值
        insert()  插入值
        delete()  删除值
Button()  创建一个按钮
    参数:
        command: 触发函数
    被点击时调用 command 函数
Checkbutton()  勾选按钮
    参数:
        command: 触发函数
        variable: 传入 StringVar() 或 IntVar() 实例对象
    被点击时将传入 variable 的实例设置为 1，未被选中时设置为 0
Radiobutton()  按钮组
    参数:
        command: 触发函数
        variable: 传入 StringVar() 或 IntVar() 实例
        value: 值，如果 variable 是 StringVar() 就传入 str 类型的值
        indicatoron: 按钮形式，默认 True，False 是按钮
    被点击时将 variable 的值设置为 value 的值
    通过 variable 的值 和 value 的值决定是否是被选中的状态，值相同就被选中
以上都可填写的参数:
    textvariable: 文本变量，传入 StringVar() 实例对象
    text: 显示的文本
    image: 图片，传入 tkinter.PhotoImage() 实例对象
    compound: 文本图片混合
        值: 'center'

Listbox()  选项列表
    参数:
        selectmode: 选择模式
            值: 'single'  'browse'  'multiple'  'extended'
            （单选，单选 可拖动，多选，多选 需要按住 shift 或 ctrl 或拖拽）
        yscrollcommand: 每次滚动调用的函数
            分别传入顶端和底端的百分比位置（小数，例: 0.0, 0.1）
    实例可用方法属性:
        insert()  插入元素，填入位置（数字或指定字符串）和字符串参数
        delete()  删除元素，填入一个或两个位置（数字或指定字符串）
        指定字符串: 'end'  'active'
        activate()  指定选中的元素，填入正数索引，索引即使超出也没事
        yview()  获取或修改浏览到的位置
            修改时传入正数索引
            或传入类似 'moveto', 0.0 的参数，0.0 指顶端百分比位置
            不论整数索引或小数是否超出
Text()  主题，能显示多种形式的主题
    实例可用方法属性:
        insert()  以某种形式加入字符串
        window_create()  以某种形式加入控件
        image_create()  以某种形式加入图片
        以上第一个参数填入的字符串: 'insert'  'current'  'end'
        （光标位置， 鼠标位置 鼠标空闲后相应，末尾）
        ......
以上都可填写的参数:
    # 以下为 kwargs 参数。不强制填写
    font: 字体
        值: ('fontname', size)  传入元组，第一个填字体，第二个填大小
    justify: 文本对齐
        值: 'left'  'right' 'center'
    foreground: 可简写成 fg，前景颜色，填入字符串
    padx: 内部 x 轴间距
    pady: 内部 y 轴间距

Canvas()  画布
    实例可用方法属性:
        create_line()  创建一条直线
        create_rectangle()  创建一个矩形
        create_text()  创建一个文本，坐标传入中心点坐标
        create_oval()  创建一个椭圆
        以上都可填写的参数:
            x1, y2  起始坐标（非元组）
            x2, y2  终点坐标
            fill: 填充
            width: 线条粗细
            dash: 虚线，传入元素是整数的元组，取值区间: [1-255]
        coords()  调整坐标，传入图形实例对象，后面跟着新的起点终点坐标
        itemconfig()  传入图形实例，再次配置参数
        move()  移动图形，传入实例，传入移动的 xy 坐标
            正数坐标往右下，负数坐标往左上
        moveto()  移动图形，传入实例，可以传入新的图形左上角字符串坐标
        delete()  删除图形，传入实例对象或 'all'
以上都可填写的参数:
    master: 上级
    background: 可简写成 bg，背景颜色
    width: 控件长
    height: 控件宽

Scrollbar()  滚动条
    参数:
        master: 上级
        command: 每次滚动调用的函数，将位置作为参数传入
    实例可用方法属性:
        set()  设置滚动条起始和结束百分比位置（小数，例: 0.0, 0.1）
        get()  获取滚动条起始和结束百分比位置
Scale()  滑动条
    参数:
        from_: 起始
        to: 终止
        orient: 朝向
            值: 'vertical'  'horizontal'（垂直，水平）
        tickinterval: 间隔多少标记一次滑动条数值
        resolusion: 分辨率，可移动的大小
        length: 滑动条长度
    实例可用方法:
        set()  设置滑动条当前位置
        get()  获取滑动条当前位置

以上实例都可用的方法属性:
    config: 配置，再次填写参数
'''

print('8.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')


'''
9.StringVar() IntVar() PhotoImage()

各种参数对象
StringVar()  提供可变的字符串对象
    参数:
        value: 值
    实例可使用方法属性:
        set()  设置值，填入字符串
        get()  获取值
PhotoImage()
    参数:
        file: 图片文件路径

以上都可填写的参数:
    master: 上级
    name:
'''

print('9.')
print('——————————————————————————————————————————————————')

print('1.')

print('——————————————————————————————————————————————————')
print('\n')
