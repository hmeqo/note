# tkinter 模块

制作GUI窗口的模块。

导入方式:

```python
import tkinter
```

## 属性

### Tk()

创建一个窗口。注: 必须先创建一个根窗口，才能进行其它操作。

- Tk(): 实例化一个根窗口
- Toplevel(): 实例化根窗口的顶层窗口，子窗口

以上实例都可使用的方法属性:

- mainloop(): 窗口循环显示（一个大的 while 循环）
- quit(): 离开 TCL 解释器，所有控件将被销毁
- destroy(): 销毁窗口及其所有控件，将终止应用于它的 TCL 解释器
- title() wm_title(): 窗口标题，括号中填入字符串
- geometry() wm_geometry(): 窗口初始大小和位置（O点在左上角，箭头往右下）
  - 参数: newGeometry: 传入字符串，格式: `<width>x<height>+<x>+<y>`（长乘宽注意是小写 x）
- minsize() wm_minsize(): 最小尺寸，参数: x, y
- maxsize() wm_maxsize(): 最大尺寸，参数: x, y
- resizable() wm_resizable(): 可调整窗口大小
  - 参数: width: 可调整长度，填 0 为不可调整；height: 可调整高度，填 0 为不可调整
- iconbitmap() wm_iconbitmap(): 设置图标，字符串参数填路径
- register(): 新创建一个 TCL 函数，参数填入 Python 函数

如果使用 destroy() 窗口无法退出，那么就先调用 quit()

### Frame() LabelFrame()

框架。提供一个框架，可在里面添加控件。

- Frame(): 普通的框架
- LabelFrame(): 标签框架
  - 参数: text: 文本；foreground: 可简写成 fg，前景颜色，填入字符串

以上实例都可用的方法属性:

- master: 上级
- image: 图片，传入 tkinter.PhotoImage() 实例对象
- background: 可简写成 bg，背景颜色
- width: 控件长
- height: 控件宽
- padx: x 轴间距
- pady: y 轴间距
- config: 配置参数

### pack() grid() place()

放置控件。

- pack(): 上下左右自动放置
  - 参数: side: 位置（'top' 'bottom' 'left' 'right'）；anchor: 锚，对齐（'e' 's' 'w' 'n' 'ne' 'nw' 'se' 'sw'）；fill: 填充空白（'x' 'y'）
- grid(): 网格布局放置
  - 参数: row: 行；column: 列；sticky: 粘性，和 pack() 的 anchor 类似
- place(): 放置至指定位置
  - 参数: x: 横坐标；y: 纵坐标；anchor: 锚点

以上实例都可用的方法属性:

- padx: 外部 x 轴间距
- pady: 外部 y 轴间距

### pack_forget() place_forget() grid_forget() forget()

拿起控件。注: 只能对创建好的控件对象使用。

- pack_forget(): 拿起被 pack() 放置的控件
- place_forget(): 拿起被 place() 放置的控件
- grid_forget(): 拿起被 grid() 放置的控件
- forget(): 看文档好像是只能拿起被 pack() 放置的控件

想重新放置使用放置控件的方法即可。

### Label() Button()

控件。

- Label(): 创建一个标签
- Entry(): 输入框
  - 参数: show: 传入字符串，每个字符用这个字符串的第一个字符显示出来；validate: 验证输入（'focus' 'focusin' 'focusout' 'key' 'all' 'none'）；validatecommand: 验证时调用的函数；invalidatecommand: 无效输入时调用的函数；state: 输入模式（'readonly' 'disabled'）；takefocus: Tab 键焦点转移，填布尔值
  - 实例可使用的方法属性: get() 获取值；insert() 插入值；delete() 删除值
- Button(): 创建一个按钮
  - 参数: command: 触发函数
- Checkbutton(): 勾选按钮
  - 参数: command: 触发函数；variable: 传入 StringVar() 或 IntVar() 实例对象
- Radiobutton(): 按钮组
  - 参数: command: 触发函数；variable: 传入 StringVar() 或 IntVar() 实例；value: 值；indicatoron: 按钮形式，默认 True，False 是按钮
- Listbox(): 选项列表
  - 参数: selectmode: 选择模式（'single' 'browse' 'multiple' 'extended'）；yscrollcommand: 每次滚动调用的函数
  - 实例可用方法属性: insert() 插入元素；delete() 删除元素；activate() 指定选中的元素；yview() 获取或修改浏览到的位置
- Text(): 主题，能显示多种形式的主题
  - 实例可用方法属性: insert() 以某种形式加入字符串；window_create() 以某种形式加入控件；image_create() 以某种形式加入图片
- Canvas(): 画布
  - 实例可用方法属性: create_line() 创建一条直线；create_rectangle() 创建一个矩形；create_text() 创建一个文本；create_oval() 创建一个椭圆；coords() 调整坐标；itemconfig() 再次配置参数；move() 移动图形；moveto() 移动图形；delete() 删除图形
- Scrollbar(): 滚动条
  - 参数: master: 上级；command: 每次滚动调用的函数
  - 实例可用方法属性: set() 设置滚动条起始和结束百分比位置；get() 获取滚动条起始和结束百分比位置
- Scale(): 滑动条
  - 参数: from_: 起始；to: 终止；orient: 朝向（'vertical' 'horizontal'）；tickinterval: 间隔多少标记一次滑动条数值；resolusion: 分辨率，可移动的大小；length: 滑动条长度
  - 实例可用方法: set() 设置滑动条当前位置；get() 获取滑动条当前位置

以上都可填写的参数:

- textvariable: 文本变量，传入 StringVar() 实例对象
- text: 显示的文本
- image: 图片，传入 tkinter.PhotoImage() 实例对象
- compound: 文本图片混合（'center'）
- font: 字体（('fontname', size)）
- justify: 文本对齐（'left' 'right' 'center'）
- foreground: 可简写成 fg，前景颜色，填入字符串
- padx: 内部 x 轴间距
- pady: 内部 y 轴间距
- master: 上级
- background: 可简写成 bg，背景颜色
- width: 控件长
- height: 控件宽
- config: 配置，再次填写参数

### StringVar() IntVar() PhotoImage()

各种参数对象。

- StringVar(): 提供可变的字符串对象
  - 参数: value: 值
  - 实例可使用方法属性: set() 设置值，填入字符串；get() 获取值
- PhotoImage():
  - 参数: file: 图片文件路径

以上都可填写的参数:

- master: 上级
- name:
