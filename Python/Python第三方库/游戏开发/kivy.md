# Kivy

## kivy.app

### App

| 方法 | 描述 |
| --- | --- |
| **事件** |  |
| `build` | 构建窗体时, 返回一个要显示的控件 |

## kivy.uix

### 控件

所有控件均在各自名为 `kivy.uix.控件名小写` 的包中

| 控件 | 描述 |
| --- | --- |
| `Widget` | 控件 |
| `Label` | 文本控件 |
| `Button` | 按钮控件 |
| `TextInput` | 文本输入框 |
| `Image` | 图像 |
| `AsyncImage` | 异步图像 |
| `FileChooserIconView` | 文件选择图标视图 |
| `FileChooserListView` | 文件选择列表视图 |
| `Silder` | 滑块 |
| `CheckBox` | 复选框 |
| `Spinner` | 下拉框 |
| `Splitter` | 可推动分割线 |
| **多屏** |  |
| `ScreenManager` | 屏幕管理 |
| `Screen` | 屏幕 |
| [`Popup`](#popup) | 弹窗 |
| `Accordion` | 手风琴分屏 |
| `AccordionItem` | 手风琴项 |
| `Carousel` | 轮播图 |
| `TabbedPanel` | 选项卡 |
| `TabbedPanelItem` | 选项卡项 |
| **布局** |  |
| [`GridLayout`](#gridlayout) | 网格布局 |
| `FloatLayout` | 浮动布局 |
| `BoxLayout` | 盒子布局 |

### 控件属性

| 属性 | 描述 | 值 |
| --- | --- | --- |
| `parent` | 父控件 | `Widget` |
| **文本** |  |  |
| `text` | 该控件显示的文本 | `str` |
| `color` | 字体颜色 | `tuple[rgba{0~1.0}]` |
| `halign` | 文字水平对齐 | `str` |
| `valign` | 文字垂直对齐 | `str` |
| **字体** |  |  |
| `font_size` | 字体大小 | `int \| str` |
| `font_name` | 字体文件路径 | `str` |
| **背景** |  |  |
| `background_color` | 背景颜色 | `tuple[rgba{0~1.0}]` |
| **外观** |  |
| `opacity` | 透明度 | `float` |
| **位置和大小** |  |  |
| `size` | 大小 | `tuple` |
| `size_hint` | 百分比大小 | `tuple[float{0~1}, float{0~1}]` |
| `width` | 宽度 | `int` |
| `height` | 高度 | `int` |
| `pos` | 控件左下角的相对位置 | `tuple` |
| `pos_hint` | 控件某点的相对百分比位置 | `dict[str, float{0~1}]` |
| `orientation` | 方向 | `str` |
| `direction` | 方向 | `str` |
| **TextInput** |  |  |
| `hint_text` | 提示文本 | `str` |
| `multiline` | 是否为多行输入 | `bool` |
| **Image** |  |  |
| `source` | 图像路径 | `str` |
| `allow_stretch` | 跟随拉伸 | `bool` |
| `keep_ratio` | 保持比例 | `bool` |
| **Slider** |  |  |
| `min` | 最小值 | `int \| float` |
| `max` | 最小值 | `int \| float` |
| `step` | 步长 | `int \| float` |
| **CheckBox** |  |  |
| `active` | 是否激活 | `bool` |
| **Popup** |  |
| `title` | 标题 | `str` |
| `content` | 用于显示内容的 widget | `Widget` |
| `auto_dismiss` | 自动关闭 | `bool` |
| **ScreenManager** |  |  |
| `current` | 当前窗口的name | `str` |
| `transition.direction` | 变换方向 | `str` |
| **Screen** |  |  |
| `name` | 窗口名 | `str` |
| `manager` | 所属 ScreenManager | `ScreenManager` |
| **Spinner** |  |  |
| `values` | 该控件可选值 | `list` |
| **Splitter** |  |  |
| `sizable_from` | 哪个位置可拖动 | `str` |
| **TabbedPanel** |  |  |
| `do_default_tab` | 是否需要 default tab | `bool` |
| `tab_pos` | tab bar 的位置 | `str` |

### 控件方法

| 方法 | 描述 |
| --- | --- |
| **Popup** |  |
| `dismiss` | 关闭 |

### 控件事件

也可以通过 `.bind` 方法绑定事件, 通过此方式绑定的方法固定传入该控件本身作为参数  
touch 相关事件会传入一个 touch 事件对象作为参数

| 事件方法 | 描述 |
| --- | --- |
| `on_press` | 当按钮按下 |
| `on_release` | 当按钮松开 |
| `on_touch_down` | 鼠标/触摸按下 |
| `on_touch_move` | 鼠标/触摸按下时移动 |
| `on_touch_up` | 鼠标/触摸松开 |
| `on_value` | 值发生变化时 |
| `on_active` | 激活状态变化时 |
| `on_text` | 文本发生改变时 |

| touch 事件对象属性 |  |
| --- | --- |
| `pos` | 坐标 |

### Popup

示例:

```python
wdg = Widget()
popup_window = Popup(title="Popup Window", content=wdg, size_hint=(None, None), size=(400, 400))
popup_window.open()
```

### GridLayout

| 属性 | 描述 |
| --- | --- |
| `cols` | 列数 |
| `rows` | 行数 |

| 方法 | 描述 |
| --- | --- |
| `add_widget` | 添加控件 |

## kivy 程序设计语言 .kv

一个和 App 类名同名 (去掉末尾 App) 以 .kv 结尾的文件, 例如: (MyApp -> my.kv)

语法结构:

```python
class MyGrid(Widget):
    pass
```

```text
<MyGrid>:
    GridLayout:
        cols: 1
        Label:
            text: "test"
```

每一个 .kv 文件都是一个根节点控件  
被 <> 包裹的控件代表一个根节点控件, 其下的控件以它为根节点, 根节点不能嵌套  
使用 `@` 表示继承并创建新控件: `<MyButton@Button>`

### 指代对象

| 标识符 | 指代对象 |
| --- | --- |
| `self` | 自身 |
| `root` | 根Widget对象 |
| `app` | app对象 |
| `Factory` | 指代全局 (需导入) |

.kv中也可以使用该对象的id指代该对象  
.py中可以使用.ids.获取该对象以下拥有id的对象  
Factory 导入方式: `#:import Factory kivy.factory.Factory`

## kivy.properties

### ObjectProperty

用于绑定 .kv 中的控件

```text
<MyWidget>:
    name: name    # python中的变量名: 绑定id为name的控件

    Label:
        id: name  # id: id名
```

```python
class MyWidget(Widget):
    name = ObjectProperty(None)  # None 为初始值, 该对象和绑定控件属性一致
```

## 绑定控件

```text
<MyWidget>:
    name: name
    email: email

    GridLayout:
        size: root.width, root.height
        pos: 0, 0
        rows: 2

        GridLayout:
            cols: 2

            Label:
                text: "Name: "

            TextInput:
                id: name
                multiline: False

            Label:
                text: "Email: "

            TextInput:
                id: email
                multiline: False

        Button:
            text: "Submit"
            on_press: root.btn_press()
```

## 条件表达式

```text
<MyWidget>:
    Button:
        id: btn
        text: "Test" if btn.state == "normal" else "Down"
```

## kivy.graphics

| 类 | 描述 |
| --- | --- |
| `Color` | 颜色 |
| `Rectangle` | 矩形 |
| `Line` | 线 |

示例:

```python
def __init__(self):
    super().__init__()
    with self.canvas:
        Color(0, 0, 1, 1, mode="rgba")
        # 接收创建的实例可对其进行更改
        self.rect = Rectangle(pos=(0, 0), size=(50, 50))
        self.rect.pos = (10, 10)
        Color(0, 1, 0, 1, mode="rgba")
        Line(points=(20, 30, 400, 500, 60, 500))
```

### Color

| 属性 | 描述 | 值 |
| --- | --- | --- |
| `rgb` | RGB | `tuple[rgb{0~1.0}]` |
| `rgba` | RGBA | `tuple[rgba{0~1.0}]` |
| `hsv` | HSV | `tuple[hsv{0~1.0}]` |

## kivy.lang

手动加载 .kv 文件示例:

```python
from kivy.app import App
from kivy.lang import Builder

kv = Builder.load_file("test.kv")


class MyApp(App):

    def build(self):
        return kv
```

## 多屏幕示例

file: main.py

```python
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class MainWindow(ScreenManager):
    pass


class TestApp(App):
    pass


if __name__ == "__main__":
    TestApp().run()
```

file: test.kv

```text
MainWindow:
    MainScreen:
    SecondScreen:

<MainScreen>:
    name: "main"

    GridLayout:
        cols: 1

        Label:
            text: "Main Screen"

        Button:
            text: "Next"
            on_press: app.root.current = "second"

<SecondScreen>:
    name: "second"

    GridLayout:
        cols: 1

        Label:
            text: "Second Screen"
        
        Button:
            text: "Go Back"
            on_press: app.root.current = "main"
```

## kivy.core.window

窗口属性 `from kivy.core.window import Window`

## kivy.core.spelling

语法检查 `from kivy.core.spelling import Spelling`
