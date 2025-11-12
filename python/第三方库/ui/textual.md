# Textual

## App

### BINDINGS

("快捷键", "绑定函数名", "文本信息")

### App 类的反射机制

在 BINDINGS 中绑定的函数会调用名为 action_+绑定函数名 的方法

## Static

### Static 类的反射机制

调用 set_interval 后, 每隔一段时间调用名为 watch_+反射变量名 的方法
