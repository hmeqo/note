# KDE

* 将 meta 修饰键修改为 Overview

  ```bash
  > kwriteconfig6 --file kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/kwin,,invokeShortcut,Overview"
  > qdbus6 org.kde.KWin /KWin reconfigure
  ```

* 重新加载启动项
  
  ```bash
  > kbuildsycoca6
  ```

* 清理无效的快捷键
  
  ```bash
  > qdbus6 org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.cleanUp
  ```
