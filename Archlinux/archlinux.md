# Arch Linux

## 安装

按照官网步骤安装: <https://wiki.archlinux.org/title/Installation_guide>  
刚开始可以先分个区

BiliBili: <https://www.bilibili.com/video/BV1J34y1f74E>  
BiliBili: <https://www.bilibili.com/video/BV1XY4y1f77S>

### 1. 准备

#### WIFI 网络连接

有线网络会自动连接, 不需要手动连接

`ip link` 查看网络设备, 如果网卡被禁用可以使用 `rfkill list` 查询网卡列表, 使用 `rfkill unblock <device>` 解锁设备, 如果 WIFI 未启用, 使用 `ip link set <device> up` 启用设备

通过 `iwctl` 配对设备, `iwctl` 环境中使用 `station <device> scan` 扫描可用 WIFI, 使用 `station <device> get-networks` 列出可用 WIFI, 使用 `station <device> connect <SSID>` 连接 WIFI

之后如果安装了 `networkmanager` 可以用 `nmtui` 连接 WIFI

#### 更新系统时间

```bash
timedatectl set-ntp true
```

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
如果是系统安装时就要创建 swapfile, 如果作为跟目录的分区的挂载点是 /mnt, 应该把 of 路径改成 /mnt/swapfile

```bash
# 创建制定大小的 swapfile, 示例中的实际大小为 1M x 8k = 8GB (bs x count)
# /swapfile 可以是你想要的任何路径, 推荐不改
dd if=/dev/zero of=/swapfile bs=1M count=8k status=progress
chmod 0600 /swapfile 
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

如果安装镜像不是最新版本，先更新 archlinux-keyring

```sh
pacman -Sy archlinux-keyring
```

#### 安装基本软件包

根据 CPU 选择安装 `intel-ucode` (Intel CPU) 或 `amd-ucode` (Amd CPU)  
这个安装项是可选的，如果装不了可以不用管

```sh
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
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
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

#### 3.8 grub 开机引导

##### 安装 grub

`os-prober` 是安装双系统推荐一并安装的依赖, 能够自动检测其他操作系统的 UEFI 启动项, 非双系统可以不安装  
`efibootmgr` 是 UEFI 启动方式的依赖

```sh
pacman -S grub [efibootmgr] [os-prober]
```

如果安装了 os-prober, 需要注意os-prober 在新版 grub 默认禁用, 需要在 /etc/default/grub 修改配置手动启动

```sh
# EFI 引导方式
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
# BIOS 引导方式
grub-install [--recheck] /dev/xxx
```

生成 grub 配置

```sh
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

- `grub-theme-vimix`  
     Github: <https://github.com/Se7endAY/grub2-theme-vimix>
- Dark Matter GRUB Theme  
     GitLab: <https://gitlab.com/VandalByte/darkmatter-grub-theme>

#### 3.9 网络管理器

`pacman` 安装 `networkmanager`, 然后 `systemctl enable NetworkManager` 设置开机启动

#### 3.10 创建用户

推荐方式, 创建用户，然后一个创建文件到 `/etc/sudoers.d/`，并添加这段配置 `<username> ALL=(ALL:ALL) ALL` 以允许新用户使用 `sudo`

```sh
# 创建用户
useradd -m <username>
# 设置密码
passwd <username>
```

### 字体安装

| 包                  | 描述                |
| ------------------- | ------------------- |
| `noto-fonts-cjk`    | 中文                |
| `noto-fonts-emoji`  | 表情                |
| `ttf-fira-code`     | Fira Code           |
| `ttf-firacode-nerd` | Fira Code Nerd Font |

#### 设置中文字体优先级

中文字体配置, 将此配置添加到 /etc/fonts/conf.d/50-user.conf 中

```xml
<fontconfig>
  <!-- Chinese -->
  <alias>
    <family>Noto Sans CJK</family>
    <prefer>
      <family>Noto Sans CJK SC</family>
      <family>Noto Sans CJK TC</family>
      <family>Noto Sans CJK JP</family>
      <family>Noto Sans CJK KR</family>
      <family>Noto Color Emoji</family>
      <family>Noto Emoji</family>
    </prefer>
  </alias>
  <alias>
    <family>Noto Serif CJK</family>
    <prefer>
      <family>Noto Serif CJK SC</family>
      <family>Noto Serif CJK TC</family>
      <family>Noto Serif CJK JP</family>
      <family>Noto Serif CJK KR</family>
      <family>Noto Color Emoji</family>
      <family>Noto Emoji</family>
    </prefer>
  </alias>
  <alias>
    <family>Noto Sans Mono CJK</family>
    <prefer>
      <family>Noto Sans Mono CJK SC</family>
      <family>Noto Sans Mono CJK TC</family>
      <family>Noto Sans Mono CJK JP</family>
      <family>Noto Sans Mono CJK KR</family>
      <family>Noto Color Emoji</family>
      <family>Noto Emoji</family>
    </prefer>
  </alias>
  <alias>
    <family>sans-serif</family>
    <prefer>
      <family>Noto Sans</family>
      <family>Noto Sans CJK</family>
    </prefer>
  </alias>
  <alias>
    <family>serif</family>
    <prefer>
      <family>Noto Serif</family>
      <family>Noto Serif CJK</family>
    </prefer>
  </alias>
  <alias>
    <family>monospace</family>
    <prefer>
      <family>Noto Sans Mono</family>
      <family>Noto Sans Mono CJK</family>
    </prefer>
  </alias>
</fontconfig>
```

## 安装桌面环境

### KDE

```bash
pacman -S sddm xorg wayland qt6-wayland plasma konsole dolpin firefox
```

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
Include = /etc/pacman.d/archlinuxcn-mirrorlist
```

## 软件

| 软件                | 描述                 |
| ------------------- | -------------------- |
| [`paru`](#paru)     | Aur 包管理器         |
| **终端**            |                      |
| `yakuake`           | 终端                 |
| `kitty`             | 终端                 |
| `wezterm`           | 终端                 |
| **Shell**           |                      |
| `zsh`               | shell                |
| `zimfw`             | zsh 扩展管理         |
| `powerlevel10k`     | zsh 扩展             |
| `fish`              | shell                |
| **Shell 工具**      |                      |
| [`tmux`](./tmux.md) | 终端复用             |
| `bat`               | better cat           |
| `exa`               | better ls            |
| `zoxide`            | better cs            |
| `fzf`               | 选择                 |
| `ranger`            | 选择                 |
| **搞怪**            |                      |
| `sl`                | 火车                 |
| `cmatrix`           | 黑客字幕             |
| `toilet`            | 艺术字               |
| `cowsay`            | 奶牛说               |
| `asciiquarium`      | 水族馆               |
| `lolcat`            | 渐变色输出           |
| **视频播放器**      |                      |
| `vlc`               | 视频播放器           |
| `mpv`               | 精简视频播放器       |
| `mplayer`           | 终端操控的视频播放器 |
| **音乐播放器**      |                      |
| `elisa`             |                      |
| **视频编辑**        |                      |
| `kdenlive`          | 视频剪辑             |
| **图像编辑**        |                      |
| `gimp`              |                      |
| `krita`             |                      |
| **磁盘管理**        |                      |
| `gparted`           | 分区工具             |
| `etcher`            | 刻录工具             |

### paru

GitHub: <https://github.com/Morganamilo/paru>

```sh
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
```

### pacman 疑难解答

如果使用 pacman 报密钥相关错误，可以尝试初始化密钥环

```bash
pacman-key --init
pacman-key --populate archlinux
```
