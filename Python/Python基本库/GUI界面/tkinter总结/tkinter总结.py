import tkinter as tk

# 创建窗口
window = tk.Tk()

# 标题
window.title('主界面')

# 界面大小
window.geometry('+300+200')

# 最小尺寸，最大尺寸使用.maxsize()
window.minsize(500, 300)

# 窗口位置由谁决定，填 'user' 或 'program'
window.positionfrom('program')

# 窗口尺寸由谁决定，填 'user' 或 'program'
window.sizefrom('program')

# 添加到窗口群中，括号里填窗口群的主窗口
window.group(window)

# 设置或获取窗口属性，如果只给出选项名，则返回当前窗口该选项的值
window.attributes('-alpha', 0.8)  # （Windows,Mac）透明度
# window.attributes('-disabled')  # （Windows）禁用整个窗口，这时候只能在任务管理器关闭它
# window.attributes('-fullscreen', True)  # （Windows,Mac）全屏显示
# window.attributes('-modified', True)  # （Mac）如果设置为True，该窗口被标记为改动过
# window.attributes('-titlepath')  # （Mac）设置代理图标窗口的路径
# window.attributes('-toolwindow', True)  # （Windows）设置为True，该窗口采用工具窗口的样式
# window.attributes('-topmost', True)  # （Windows）设置为True，该窗口将永远置于顶层

# 图标化（最小化？）
# window.iconify()  # 使用.deiconify()重新显现

# 遗忘它（消失，但没有销毁）
# window.withdraw()  # 使用.deiconify()重新显现

# 没有标题栏边框等部件
# window.overrideredirect(True)  # 设为True，将没有传统的边框等等

# 监控键盘操作，返回多个值，.keysym 是按键名称，<KeyPress> 按下 <KeyRelease> 松开，<KeyPress-A> 指定按键，func= 触发的函数
window.bind('<KeyPress>', func=lambda event: print('haha', event.keysym))

# 开始循环窗口
window.mainloop()
