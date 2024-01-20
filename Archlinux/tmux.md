# tmux

## 开启新 session

tmux

## 开启新 session 并命名

tmux new -s my_session

## 显示所有 session

tmux ls

## 使用 session 编号接入

tmux attach -t 0

## 使用 session 名称接入

tmux attach -t <session-name>
tmux a -t name #简写

## 使用 session 编号 kill

tmux kill-session -t 0

## 使用 session 名称 kill

tmux kill-session -t <session-name>

## 使用 session 编号切换

tmux switch -t 0

## 使用 session 名称切换

tmux switch -t <session-name>

## 重命名会话

tmux rename-session -t 0 <new-name>

## 选择需要跳转的 session 会话

C + b s

## 重命名当前会话

C + b $

## 断开当前 session

C + b d

## 在当前 session 中多加一个 window

C + b c

## 在一个 session 中的多个 window 中作出选择

C + b w

## 关闭当前 session 中的当前 window

C + b x

## 进入 tmux 翻屏模式, 实现上下翻页

C + b [

### 进入翻屏模式后 PgUp PgDn 实现上下翻页（mac 可以用 fn + ↑ ↓ 实现上下翻页）

### q 退出翻屏模式

#############

## 其他常用快捷键

##############

C + b ！ #关闭一个 session 中所有窗口
C + b % #将当前窗口分成左右两分
C + b " #将当前窗口分成上下两分
C + b 方向键 #让光标在不同的窗口中跳转
C + b 方向键 #按住 C+b 不放，同时按住方向键，可以调节光标所在窗口的大小
