# Arch Linux

## 安装

可以配合官网步骤食用: [https://wiki.archlinux.org/title/Installation_guide](https://wiki.archlinux.org/title/Installation_guide)

### 视频教程

BiliBili: [https://www.bilibili.com/video/BV1J34y1f74E](https://www.bilibili.com/video/BV1J34y1f74E)  
BiliBili: [https://www.bilibili.com/video/BV1XY4y1f77S](https://www.bilibili.com/video/BV1XY4y1f77S)

### 1. 准备

#### WIFI 网络连接

有线网络会自动连接, 不需要手动连接

`ip link` 查看网络设备, 如果网卡被禁用可以使用 `rfkill list` 查询网卡列表, 使用 `rfkill unblock <device>` 解锁设备, 如果 WIFI 未启用, 使用 `ip link set <device> up` 启用设备

通过 `iwctl` 配对设备, `iwctl` 环境中使用 `station <device> scan` 扫描可用 WIFI, 使用 `station <device> get-networks` 列出可用 WIFI, 使用 `station <device> connect <SSID>` 连接 WIFI

之后如果安装了 `networkmanager` 可以用 `nmtui` 连接 WIFI

#### 分区

可以用 `lsblk`、`fdisk -l` 检查电脑中可用的硬盘

推荐使用 `cfdisk` 进行分区, `cfdist` 主界面可以按 h 查看帮助, 按 n 可以新建分区
对照下表设置分区的类型

| 分区     | 类型             |
| -------- | ---------------- |
| efi      | EFI System       |
| 一般分区 | Linux Filesystem |
| swap     | Linux swap       |

如果电脑的启动方式是 UEFI, 需要单独分一个 EFI 分区, 大小推荐不小于 300MB, 如果是双系统推荐 500MB
Windows/Linux 双系统本身已经有 EFI 分区了, 可以不用再分, 只需要把原来的 EFI 分区扩容到推荐大小即可

##### 创建 swapfile 作为 swap 分区

如果不想通过分区使用 swap, 可以通过创建 swapfile 文件作为 swap 分区

!!! info
    在Arch安装过程中, 请注意 swapfile 的文件路径, 例如系统根分区的临时挂载点是 /mnt, 那么应该把 dd 命令的 of 参数路径改成 /mnt/swapfile 或其他 /mnt 下的路径

```bash
# 创建制定大小的 swapfile, 示例中的实际大小为 1M x 8k = 8GB (bs x count)
# /swapfile 可以是你想要的任何路径, 常用的路径 /swapfile /swap.img

# 方式 1
dd if=/dev/zero of=/swapfile bs=1M count=8k status=progress
# 方式2
fallocate -l 8G /swapfile

# 设置 swapfile 的权限
chmod 0600 /swapfile 

mkswap /swapfile
```

#### 格式化和挂载路径

按照表格找到对应的格式化和挂载方式

| 名称               | 挂载点                 | 格式化命令                                                      |
| ------------------ | ---------------------- | --------------------------------------------------------------- |
| EFI 分区           | /boot                  | `mkfs.fat -F 32 /dev/efi_system_partition`                      |
| Linux 文件系统分区 | 必须有一个 /, 其他随意 | `mkfs.ext4 /dev/root_partition` (也可以选择其他的格式, 如 btfs) |
| Swap 分区          | 没有挂载点             | `mkswap /dev/swap_partition`                                    |

##### 如何挂载分区

```bash
# mount 分区路径 u挂载点
# 挂载点需要是已存在的文件夹, 如果挂载点对应的文件夹不存在, 可以加上 --mkdir 自动创建对应的文件夹
mount /dev/sda1 /root

# 如果是 swap 分区
swapon /dev/swap_partition
```

### 2. 安装

#### 镜像源

如果需要可以先配置镜像
调整 `/etc/pacman.d/mirrorlist` 中镜像的顺序即可
需要在运行 `pacstrap` 或 `pacman` 之前配置好

#### 密钥环

如果安装镜像不是最新版本, 先更新 archlinux-keyring

```bash
# 这将更新软件包数据库和密钥环
pacman -Sy archlinux-keyring
```

#### 安装基本软件包

根据 CPU 选择安装 `intel-ucode` (Intel CPU) 或 `amd-ucode` (Amd CPU)
这个安装项是可选的，如果装不了可以不用管

```bash
pacstrap -K /mnt base linux-zen linux-zen-headers linux-firmware base-devel nano vim networkmanager [intel-ucode/amd-ucode]
```

### 3. 配置系统

#### 3.1 导出分区表

```bash
genfstab -U /mnt >> /mnt/etc/fstab
```

#### 3.2 Chroot

```bash
arch-chroot /mnt
```

#### 3.3 设置时区

```bash
# 复制时区文件
ln -sf /usr/share/zoneinfo/<Region>/<City> /etc/localtime
# 生成 /etc/adjtime
hwclock --systohc
```

#### 3.4 设置地区

编辑 `/etc/locale.gen`, 取消注释需要的地区， 然后运行

```bash
locale-gen
```

设置地区, 编辑 `/etc/locale.conf`

```conf
LANG=en_US.UTF-8
```

#### 3.5 设置主机名

编辑 `/etc/hostname`, 文件内容就是主机名

#### 3.6 初始化配置

通常不需要自己创建新的 `initramfs`，因为在执行 `pacstrap` 时安装了 linux 内核，安装 linux 的过程会自动运行 `mkinitcpio`

如果是 LVM、 系统加密或 RAID 等分区配置，请修改 `mkinitcpio.conf` 并用以下命令重新创建一个 `Initramfs`:

```bash
mkinitcpio -P
```

#### 3.7 更改 root 密码

```bash
passwd
```

#### 3.8 网络管理器

`pacman` 安装 `networkmanager`, 然后 `systemctl enable NetworkManager` 设置开机启动

#### 3.9 创建用户

推荐方式, 创建用户，然后一个创建文件到 `/etc/sudoers.d/`，并添加这段配置 `<username> ALL=(ALL:ALL) ALL` 以允许新用户使用 `sudo`

```bash
# 创建用户
useradd -m <username>
# 设置密码
passwd <username>
```

#### 3.10 更新系统时间

自动同步世界时

```bash
timedatectl set-ntp true
```

### 4. 开机引导

常见的引导方式有 `Grub`、`systemd-boot`、`rEFInd` 选择一个引导方式即可

#### grub

##### 安装 grub

`efibootmgr` 是 UEFI 启动方式的依赖, 如果是 BIOS 启动可以不用安装
`os-prober` 是安装双系统推荐一并安装的依赖, 能够自动检测其他操作系统的 UEFI 启动项, 非双系统可以不安装

```bash
pacman -S grub [efibootmgr] [os-prober]
```

如果安装了 os-prober, 需要注意 os-prober 在新版 grub 默认禁用, 修改 `/etc/default/grub` 取消注释 `GRUB_DISABLE_OS_PROBER=false` 即可启用 os-prober

```bash
# UEFI 安装方式
grub-install --efi-directory=esp --bootloader-id=GRUB
# BIOS 安装方式
grub-install /dev/xxx
```

生成 grub 配置

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

##### os-prober 找不到其他系统

初次运行 grub-mkconfig 一般 os-prober 会找不到 Windows, 重启一次并重新生成 grub 配置就能检测到了

或者可以通过 `blkid <device>` 查找启动分区的 UUID, 然后将以下代码添加到 /boot/grub/grub.cfg

```conf
### BEGIN /etc/grub.d/30_os-prober ###
menuentry 'Microsoft Windows 10' {
  insmod part_gpt
  insmod fat
  insmod chain
  search --fs-uuid --no-floppy --set=root <UUID>
  chainloader
}
### END /etc/grub.d/30_os-prober ###
```

##### Grub 主题

- `grub-theme-vimix`Github: [https://github.com/Se7endAY/grub2-theme-vimix](https://github.com/Se7endAY/grub2-theme-vimix)
- Dark Matter GRUB Theme
  GitLab: [https://gitlab.com/VandalByte/darkmatter-grub-theme](https://gitlab.com/VandalByte/darkmatter-grub-theme)

#### systemd-boot

systemd-boot 是 systemd 全家桶的一部分, 在 arch 不需要额外安装

运行以下命令即可安装

```bash
bootctl --esp-path=esp install
```

#### rEFInd

```bash
refind-install
```

!!! warning
    当 refind-install 运行在chroot环境下 (例如：安装Arch Linux时的live环境) /boot/refind_linux.conf 内将会添加live系统的内核选项，而不是安装它的系统。
    编辑 /boot/refind_linux.conf 并确保其中的 内核参数 对于你的系统是正确的，否则下次启动可能会出现内核错误。

## pacman

### pacman 的其他软件源

配置文件路径: `/etc/pacman.conf`

- 启用 32 位软件源

取消配置文件中的 multilib 注释

```conf
[multilib]
Include = /etc/pacman.d/mirrorlist
```

- archlinuxcn 源

将下面内容加入 pacman 配置文件

```conf
[archlinuxcn]
# 清华源
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
```

### 初始化密钥环

```bash
pacman-key --init
pacman-key --populate archlinux
```

### Aur 助手安装

可选的 aur 助手有: [yay](#yay)、[paru](#paru), 选择喜欢的 Aur 助手安装即可, 使用 aur 助手代替 pacman

### pacman 疑难解答

如果使用 pacman 报密钥相关错误, 可以尝试[初始化密钥环](#初始化密钥环)

## 软件包

### 软件推荐

| 软件                | 描述                 |
| ------------------- | -------------------- |
| [`yay`](#yay)       | Aur 助手             |
| [`paru`](#paru)     | Aur 助手             |
| **Shell**           |                      |
| `zsh`               | shell                |
| `zim`               | zsh 扩展管理         |
| `fish`              | shell                |
| `fisher`            | shell 扩展管理       |
| **Shell 工具**      |                      |
| [`tmux`](./tmux.md) | 终端复用             |
| `bat`               | better cat           |
| `exa`               | better ls            |
| `fzf`               | 终端下的 select      |
| `yazi`              | 终端下的 explorer    |
| `ranger`            | 终端下的 explorer    |
| **终端**            |                      |
| `yakuake`           | 终端                 |
| `wezterm`           | 终端                 |
| `kitty`             | 终端                 |
| **搞怪**            |                      |
| `sl`                | 火车                 |
| `cmatrix`           | 黑客字幕             |
| `figlet`            | 艺术字               |
| `toilet`            | 艺术字               |
| `cowsay`            | 奶牛说               |
| `asciiquarium`      | 水族馆               |
| `lolcat`            | 渐变色输出           |
| **视频播放器**      |                      |
| `vlc`               | 视频播放器           |
| `mpv`               | 精简视频播放器       |
| `mplayer`           | 终端操控的视频播放器 |
| **音乐播放器**      |                      |
| `elisa`             | 音乐播放器, 自带电台 |
| **视频编辑**        |                      |
| `kdenlive`          | 视频剪辑             |
| **图像编辑**        |                      |
| `gimp`              | 修图                 |
| `inkscape`          | 矢量图编辑           |
| **文档**            |                      |
| `okular`            | PDF/MD 阅读和编辑    |
| `onlyoffice`        | 仿微软办公套件       |
| `libreoffice`       | 办公套件             |
| **磁盘管理**        |                      |
| `partiionmanager`   | 分区工具             |
| `gparted`           | 分区工具             |
| `etcher`            | 刻录工具             |
| **游戏**            |                      |
| `mangohud`          | 游戏性能监控         |
| `gamemode`          | 使用游戏模式运行游戏 |
| `steam`             | Steam 客户端         |
| `heroic`            | 第三方 Epic 客户端   |
| `lutris`            | 游戏管理器           |

#### yay

```bash
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/yay.git
cd paru
makepkg -si
```

#### paru

GitHub: [https://github.com/Morganamilo/paru](https://github.com/Morganamilo/paru)

```bash
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
```

### 字体

| 包                  | 描述                |
| ------------------- | ------------------- |
| `noto-fonts-cjk`    | 中文                |
| `noto-fonts-emoji`  | 表情                |
| `noto-fonts-extra`  |                     |
| `ttf-fira-code`     | Fira Code           |
| `ttf-firacode-nerd` | Fira Code Nerd Font |
