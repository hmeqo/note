# Arch Linux

## 网站

Archlinux: <https://www.archlinux.org/>  
Archlinuxcn: <https://www.archlinuxcn.org/>

## 安装

> [!NOTE]
> 编程中有许多特殊符号, 例如 \<xxx\> 代表根据实际情况填写的必填项, \[xxx\] 代表可选项, 请根据上下文自行判断

可以配合官网步骤食用: <https://wiki.archlinux.org/title/Installation_guide>

### 视频教程

BiliBili: <https://www.bilibili.com/video/BV1J34y1f74E>  
BiliBili: <https://www.bilibili.com/video/BV1XY4y1f77S>

### 1. 准备

#### 获取系统信息

判断BIOS类型, 分区表类型

#### 硬件准备

一个刻录了安装镜像的U盘, 一台电脑

#### 插入U盘

重启, 在BIOS界面选择通过U盘启动

#### WIFI 网络连接

有线网络会自动连接, 不需要手动连接

`ip link` 可以查看网络设备, 确保你的网络设备有被列出

`rfkill` 或者 `rfkill list` 查询网卡列表  
如果网卡被禁用(SOFT blocked)可以使用 `rfkill unblock <device>` 解锁设备  
如果 WIFI 未启用(HARD blocked), 使用 `ip link set <device> up` 启用设备

通过 `iwctl` 命令进入交互式环境配对设备  
使用 `station <device> scan` 扫描可用 WIFI  
使用 `station <device> get-networks` 列出可用 WIFI  
使用 `station <device> connect <SSID>` 连接 WIFI  
完成后按 `ctrl+d` 或输入 `exit` 即可退出, `ctrl+d` 算是 linux 下 cli 的通用退出快捷键了

安装完系统之后, 如果装了 `networkmanager` 可以用 `nmtui`、`nmcli` 连接 WIFI, archiso环境中用的是 `iwd`, 所以命令不同

#### 分区

##### 创建分区

可以用 `lsblk`、`lsblk -f`、`fdisk -l` 检查电脑中可用的硬盘

推荐使用 `cfdisk` 进行分区, `cfdist` 主界面可以按 h 查看帮助, 按 n 可以新建分区

几种主要的分区方案:

- 一个EFI分区(对于UEFI) + 一个Linux文件系统分区(必须) + 一个swap分区(可选)
- 一个EFI分区(对于UEFI) + 一个Linux文件系统分区(必须) + 一个home目录分区(可选) + 一个swap分区(可选)

如果电脑的启动方式是 UEFI, 需要单独分一个 EFI 分区, 大小推荐不小于 300MB, 如果是双系统推荐 500MB  
Windows/Linux 双系统本身已经有 EFI 分区了, 可以不用再分, 只需要把原来的 EFI 分区扩容到推荐大小即可

swap分区建议放在最后, 以后如果需要修改比较方便, 对于swap分区/文件要分多大, 可以参考这里 [swapspace大小建议](#swapspace大小建议)

然后对照下表设置分区的类型

| 分区     | 类型             |
| -------- | ---------------- |
| efi      | EFI System       |
| 一般分区 | Linux Filesystem |
| swap     | Linux swap       |

`cfdisk` 编辑完之后记得 `Write`, 否则你的更改不会生效

> [!NOTE]
> 也可以使用swapfile而非swap分区, 这样可以动态分配swapspace的大小, 无需调整分区, 可以等挂载完分区后再创建, [创建swapfile](#创建swapfile)  
> 在Arch安装过程中(非arch-chroot下), 请注意 swapfile 的文件路径, 例如系统根分区的临时挂载点是 /mnt, 那么应该把 dd 命令的 of 参数路径改成 /mnt/swapfile 或其他 /mnt 下的路径

##### 格式化分区

创建完分区之后, 需要格式化分区

- 对于 EFI 分区

  ```bash
  mkfs.fat -F 32 /dev/efi_system_partition
  ```

- Linux 文件系统分区

  ```bash
  # mkfs.<格式>, 可以选择其他的格式, 如 btrfs 等 (善用 tab 键和wiki)
  mkfs.ext4 /dev/root_partition
  ```

- swap 分区

  ```bash
  mkswap /dev/swap_partition
  ```

##### 挂载分区

- 首先挂载根分区到 `/mnt`

  ```bash
  mount /dev/<sda2> /mnt
  ```

- 挂载EFI分区和其他分区

  ```bash
  # EFI 分区推荐挂载点
  mount --mkdir /dev/<sda1> /mnt/boot

  ## 其他分区
  # 例如你单独分配了 home 目录的分区
  mount --mkdir /dev/<sda3> /mnt/home
  ```

- swap分区 (如果你分配了swap的分区, 使用swapfile可以跳过这一步)

  ```bash
  swapon /dev/swap_partition
  ```

> [!NOTE]
> 如果你要创建swapfile, 挂载完 `/mnt` 就可以创建了, 创建到 `/mnt/swapfile`, [创建swapfile](#创建swapfile)  
> 如果你提前创建了, `swapoff` 之后移动swapfile到 `/mnt` 下然后 `swapon` 即可

### 2. 安装

#### 镜像源

如果需要可以先配置镜像
调整 `/etc/pacman.d/mirrorlist` 中镜像的顺序即可

推荐一个国内速度较快的镜像源

```conf
Server = http://mirrors.jlu.edu.cn/archlinux/$repo/os/$arch
```

#### 更新密钥环

如果安装镜像不是最新版本, 先更新 archlinux-keyring

```bash
# 这将更新软件包数据库和密钥环
pacman -Sy archlinux-keyring
```

#### 安装基本软件包

根据 CPU 选择安装 `intel-ucode` (Intel CPU) 或 `amd-ucode` (Amd CPU)  
这个安装项是可选的，如果装不了可以不用管  
不会用 `vi/vim/neovim` 可以装 `nano`

```bash
pacstrap -K /mnt base base-devel linux-zen linux-zen-headers linux-firmware vi vim neovim networkmanager [intel-ucode/amd-ucode]
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
hwc/alock --systohc
```

#### 3.4 设置地区

编辑 `/etc/locale.gen`, 取消注释需要的地区， 然后运行

```bash
locale-gen
```

之后设置地区, 编辑 `/etc/locale.conf`, `LANG=你选择的地区`

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

#### 3.11 开机引导

常见的引导方式有下面几种, 选择一个硬件支持的引导方式即可

| 引导方式                        | BIOS 固件 | UEFI 固件 | MBR 分区表 | GPT 分区表 |                    |
| ------------------------------- | --------- | --------- | ---------- | ---------- | ------------------ |
| [`GRUB`](#grub)                 | 支持      | 支持      | 支持       | 支持       | 不知道选啥就选这个 |
| [`rEFInd`](#refind)             | 不支持    | 支持      | 支持       | 支持       | 双系统推荐         |
| [`systemd-boot`](#systemd-boot) | 不支持    | 支持      | 手动       | 支持       | 简单省事           |
| syslinux                        | 支持      | 部分支持  | 支持       | 支持       |                    |

参考文档: <https://wiki.archlinux.org/title/Arch_boot_process#Boot_loader>

##### GRUB

###### 安装GRUB

`efibootmgr` 是 UEFI 启动方式的依赖, 如果是 BIOS 启动可以不用安装
`os-prober` 是安装双系统推荐一并安装的依赖, 能够自动检测其他操作系统的 UEFI 启动项, 非双系统可以不安装

```bash
pacman -S grub [efibootmgr] [os-prober]
```

如果安装了 os-prober, 需要注意 os-prober 在新版 grub 默认禁用, 修改 `/etc/default/grub` 取消注释 `GRUB_DISABLE_OS_PROBER=false` 即可启用 os-prober

- UEFI 安装方式

  确保你安装了 `efibootmgr`

  ```bash
  # 将 esp 改为你的 EFI 分区路径, 例如 --efi-directory=/boot
  grub-install [--target=x86_64-efi] --efi-directory=<esp> --bootloader-id=GRUB
  ```

  ```bash
  grub-install --efi-directory=/boot --bootloader-id=GRUB
  ```

- BIOS 安装方式

  ```bash
  grub-install /dev/xxx
  ```

生成 grub 配置, 记住此命令, 后续如果修改了 `/etc/default/grub` 需要重新生成 grub 配置

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

###### os-prober 找不到其他系统

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

###### Grub 主题

- `grub-theme-vimix`Github: <https://github.com/Se7endAY/grub2-theme-vimix>
- Dark Matter GRUB Theme
  GitLab: <https://gitlab.com/VandalByte/darkmatter-grub-theme>

##### systemd-boot

systemd-boot 是 systemd 全家桶的一部分, 在 arch 不需要额外安装

运行以下命令即可安装

```bash
bootctl --esp-path=<esp> install
```

systemd-boot 使用教程请看此处: <https://wiki.archlinuxcn.org/wiki/Systemd-boot>

##### rEFInd

```bash
refind-install
```

> [!WARNING]
> 当 refind-install 运行在chroot环境下 (例如：安装Arch Linux时的live环境) /boot/refind_linux.conf 内将会添加live系统的内核选项，而不是安装它的系统。
> 编辑 /boot/refind_linux.conf 并确保其中的 内核参数 对于你的系统是正确的，否则下次启动可能会出现内核错误。

### 4. 重启

安装完引导之后, `ctrl+d` 退出 chroot 环境, 重启电脑 (也可以在重启之前先把桌面装好)

### 5. 后续操作

#### 安装桌面环境

建议创建一个非root用户再来安装桌面

- KDE

  参考 [KDE软件生态](#kde软件生态), 选择你需要的软件

  ```bash
  pacman -S plasma dolphin konsole yakuake zen-browser spectacle ark filelight
  ```

  然后设置自启sddm, sddm 是 kde 官方的会话管理器, 如果不喜欢你也可以换成别的

  ```bash
  systemctl enable sddm
  ```

  最后重启电脑即可

#### 显卡驱动

`mesa` 支持所有主流显卡, 基于 opengl

```bash
pacman -S mesa mesa-utils [lib32-mesa-utils]
```

- AMD

  安装 Vulkan 驱动

  ```bash
  pacman -S vulkan-radeon [lib32-vulkan-radeon]
  # 另一种选择, 但是不推荐
  pacman -S amdvlk [lib32-amdvlk]
  ```

- Intel

  安装 Vulkan 驱动

  ```bash
  pacman -S vulkan-intel [lib32-vulkan-intel]
  ```

  安装 VAAPI 驱动

  ```bash
  ## 对于新Intel显卡
  # Intel Media Driver for VAAPI — Broadwell+ iGPUs
  pacman -S intel-media-driver

  ## 对于旧Intel显卡
  # VA-API implementation for Intel G45 and HD Graphics family
  pacman -S libva-intel-driver [lib32-libva-intel-driver]
  ```

- NVIDIA

  首先安装主要驱动, 有NVIDIA官方驱动, 和社区开源驱动, 选择其一安装即可

  官方驱动  
  NVIDIA 官方提供了闭源和开源两种驱动, 分别是 `nvidia` 和 `nvidia-open`  
  nvidia-utils 中包含了 vulkan 驱动

  ```bash
  pacman -S nvidia/nvidia-open nvidia-utils [lib32-nvidia-utils] [opencl-nvidia] [nvidia-prime]
  ```

#### 双显卡管理

- envycontrol

  `envycontrol -q` 查询当前模式

  `envycontrol -s <mode>` 切换模式, 可选项：`hybrid`、`integrated`、`nvidia`

  `envycontrol --reset` 重置

## 系统配置

### 修改分区表

编辑 `/etc/fstab`, 按照这样的格式编写  
`<file system> <dir> <type> <options> <dump> <pass>`  
分别代表:

- `<file system>` 文件系统, 填写 `UUID=xxx`, 或者 `/dev/xxx`
- `<dir>` 挂载点, 对于 swap 或没有挂载点的分区, 填 `none`
- `<type>` 分区类型
- `<options>` 挂载选项, 默认值 `defaults`
- `<dump>` 备份, 填 `0` 即可
  此选项广泛用于 ext2/3 文件系统和磁带备份, 如今, 由于更新的文件系统和实用程序, 它已经过时了, 可选值有
  - `0`: 不备份
  - `1`: 备份
- `<pass>` 系统启动后通过`fsck`检查, 可选值有
  - `0`: 不检查
  - `1`: 检查
  - `2`: 在1之后检查，但不一定检查

示例 :

```fstab
UUID=xxx  /    ext4 rw,relatime 0 1
UUID=xxxx /xxx ext4 defaults    0 2
```

### Swapspace

#### Swapspace大小建议

参考来源 AI

- 对于小内存系统（≤ 2GB）

  交换分区大小建议为内存大小的 两倍。

- 对于较大内存系统（> 2GB）

  - 红帽官方建议：

    - 内存 ≤ 4G，交换分区至少 4G。
    - 内存为 4~16G，交换分区至少 8G。
    - 内存为 16~64G，交换分区至少 16G。
    - 内存为 64~256G，交换分区至少 32G。

  - Ubuntu 的建议（针对是否需要休眠）：

    - 物理内存 < 1G：
      - 不需要休眠：交换分区 = 内存大小。
      - 需要休眠：交换分区 = 内存大小的两倍（但不超过两倍）。
    - 物理内存 ≥ 1G：
      - 不需要休眠：交换分区 = √(RAM)。
      - 需要休眠：交换分区 = RAM + √(RAM)，但不超过两倍内存大小。

- 一般原则

  - 不频繁使用大内存应用：可以参考上述建议的较小值，或者根据实际使用情况调整。
  - 频繁使用大内存应用或服务：可能需要更大的交换分区，但应避免过度依赖交换分区，以免影响系统性能。
  - 休眠功能：确保交换分区足够大，以容纳所有内存内容，通常意味着交换分区的大小至少应等于物理内存大小。

#### 创建swapfile

如果不想通过分区使用 swap, 可以创建 swapfile 作为 swapspace

以下命令中的 /swapfile 可以是你想要的任何路径, 常用的路径有 `/swapfile`、`/swap.img`

- 方式1 (Arch Linux 专用)

  ```bash
  mkswap -U clear --size 4G --file /swapfile
  ```

- 方式2 (快速, 所有发行版都支持)

  ```bash
  fallocate -l 8G /swapfile

  chmod 0600 /swapfile
  mkswap -U clear /swapfile
  ```

- 方式3

  ```bash
  # 创建指定大小的 swapfile, 示例中的实际大小为 1M x 8k = 8GB (bs x count)
  dd if=/dev/zero of=/swapfile bs=1M count=8k status=progress

  chmod 0600 /swapfile
  mkswap -U clear /swapfile
  ```

创建完成后, 可以选择立即挂载Swap

```bash
swapon /swapfile
```

最后写入 /etc/fstab (如果你是在Arch安装过程, 挂载了swap, 并且还未运行genfstab, 可以跳过这一步, genfstab 会帮你写入)

```bash
# ...
# Swap
/swapfile             none        swap        defaults    0 0
```

### 休眠

#### 添加休眠钩子

编辑 `/etc/mkinitcpio.conf` 文件, 找到 HOOKS 配置项

有两种情况

- 对于udev

  参考以下代码, 将 `resume` 添加到 udev 之后

  ```conf
  HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block filesystems resume fsck)
  ```

- 对于systemd

  Systemd 钩子, 自带resume, 不需要手动添加

  ```conf
  HOOKS=(base systemd autodetect modconf kms keyboard sd-vconsole sd-encrypt block filesystems fsck)
  ```

> [!NOTE]
> If stacked storage is used for the swap space, e.g. dm-crypt, RAID or LVM, the final mapped device must be available in the early userspace and before the resume process is initiated. I.e. the resume hook must be placed after hooks like encrypt, lvm2, etc. in such setups.

#### 添加内核参数

使用 `blkid /dev/nvme0n1p1`, 查看 UUID, 写入到内核参数, 格式 `resume=UUID=xxxxxx`

示例:

```bash
❯ sudo blkid /dev/nvme0n1p1
/dev/nvme0n1p1: LABEL="archlinux" UUID="4483df75-6a1d-42a1-9a3e-66406b7a9cac" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="1cf11453-a83c-4dd9-9f88-28a24754818f"
```

对于 swapfile, 需要额外加上 `resume_offset=xxxxxx`, 表示偏移量, 偏移量可以通过此命令快速获取 `filefrag -v <swap_file> | awk '$1=="0:" {print substr($4, 1, length($4)-2)}'`

示例:

```bash
❯ sudo filefrag -v /swap.img | awk '$1=="0:" {print substr($4, 1, length($4)-2)}'
3643392
```

完成后的内核参数示例:

```bash
... root=UUID=4483df75-6a1d-42a1-9a3e-66406b7a9cac rw splash resume=UUID=4483df75-6a1d-42a1-9a3e-66406b7a9cac resume_offset=3643392
```

> [!NOTE]
> 如果你的引导方式是 Grub, 需通过 `/etc/default/grub` 修改内核参数, 完成后记得 `sudo mkinitcpio`

## pacman

配置文件路径: `/etc/pacman.conf`  
镜像服务器列表路径: `/etc/pacman.d/mirrorlist`

### 初始化密钥环

一般正常安装 Archlinux 并不需要自己手动初始化密钥环, 某些情况例如 SteamOS 和 Termux 需要手动初始化

```bash
pacman-key --init
pacman-key --populate archlinux
```

### 配置pacman

#### 多线程下载

在 pacman 配置文件找到并取消注释 `ParallelDownloads`

```confini
[options]
...
#VerbosePkgLists
ParallelDownloads = 5
...
```

#### 颜色

在 pacman 配置文件中取消 `Color` 的注释

```confini
[options]
...
#UseSyslog
Color
#NoProgressBar
...
```

#### pacman 的其他软件源

##### 32 位软件源

安装Steam或其他32位软件包需要此软件源, 在 pacman 配置文件中取消注释 multilib 部分然后运行 `sudo pacman -Sy`

```conf
[multilib]
Include = /etc/pacman.d/mirrorlist
```

##### archlinuxcn 源

> Arch Linux 中文社区仓库是由 Arch Linux 中文社区驱动的非官方软件仓库，包含许多官方仓库未提供的额外的软件包，以及已有软件的 git 版本等变种。一部分软件包的打包脚本来源于 AUR，但也有许多包与 AUR 不一样。

添加步骤: 将下面内容加入 pacman 配置文件末尾 `/etc/pacman.conf`

```conf
[archlinuxcn]
## 阿里云 (Global CDN)
Server = https://mirrors.aliyun.com/archlinuxcn/$arch

# ## 主仓库 (需要魔法)
# Server = https://repo.archlinuxcn.org/$arch
```

> [!TIP]
> 更多archlinuxcn镜像服务器查看此处 <https://github.com/archlinuxcn/mirrorlist-repo>

然后安装archlinuxcn的密钥环

```bash
pacman -Sy archlinuxcn-keyring
```

2023年10月之后, 新系统下安装cn密钥环之前需要额外步骤, 需要在本地信任 farseerfc 的 GPG key

```bash
pacman-key --lsign-key "farseerfc@archlinux.org"
```

#### 彩蛋

在 pacman 配置中加入 `ILoveCandy`, 进度条会被替换成吃豆人

```confini
[options]
ILoveCandy
```

### Aur 助手安装

可选的 aur 助手有: [yay](#yay)、[paru](#paru), 选择喜欢的 Aur 助手安装即可, 使用 aur 助手代替 pacman

### pacman 常用命令

以下为个人理解, 有些地方可能并不准确或非官方叫法

pacman 使用方式和 vim 很像, 格式为一个Operator加n个Motion

常用的 Operator 有 `-S` (同步/安装)、`-R` (卸载)、`-Q` (查询本地)

| 常用命令                       | 描述                                                              |
| ------------------------------ | ----------------------------------------------------------------- |
| `pacman -Syu`                  | 更新数据库(y)和软件包(u)                                          |
| `pacman -S <软件包>`           | 安装软件包                                                        |
| `pacman -Ss <regex>`           | 搜索软件包(s)                                                     |
| `pacman -Si <软件包>`          | 查看软件包信息(i)                                                 |
| `pacman -Syyuu`                | 强制更新数据库(yy)并升级/降级软件包(uu)                           |
| `pacman --fm nvim -S <软件包>` | 安装软件包, 并在安装之前编辑 PKGBUILD (--fm)                      |
| `pacman -Rsn <软件包>`         | 删除软件包以及相关依赖(s)和配置文件(n)                            |
| `pacman -Rsnc <软件包>`        | 删除软件包以及相关依赖(s)和配置文件(n), 并且删除依赖它的软件包(c) |
| `pacman -Rsndd <软件包>`       | 强制删除软件包以及相关依赖(s)和配置文件(n), 忽略依赖问题(dd)      |
| `pacman -c`                    | 删除不再需要的软件包 (不推荐, 不会删除软件包的依赖)               |
| `pacman -Rsnc $(pacman -Qtdq)` | 删除所有孤包 (推荐)                                               |
| `pacman -Q`                    | 列出已安装的软件包                                                |
| `pacman -Qs <regex>`           | 搜索软件包(s)                                                     |
| `pacman -Qi <软件包>`          | 查看软件包信息(i)                                                 |
| `pacman -Ql <软件包>`          | 查看软件包的文件路径(l)                                           |
| `pacman -Qo <file>`            | 查询已安装的文件或命令所属软件包(o)                               |
| `pacman -Qtdq`                 | 列出孤包(td), 即不被需要(t)的软件包依赖(d), 不显示版本信息(q)     |
| `pacman -Qeq`                  | 列出自己安装的软件包(e), 不显示版本信息(q)                        |
| `pacman -Qteq`                 | 列出自己安装(e)的不被其他软件包依赖(t)的软件包, 不显示版本信息(q) |
| `pacman -F <file>`             | 查询文件或命令所属软件包                                          |
| `pacman -Fy`                   | 更新文件数据库(y)                                                 |
| `pacman -U <file>`             | 从文件安装软件包(package.tar.gz)                                  |
| `paru -Gc <软件包>`            | 查看aur软件包评论                                                 |

## 常用软件包/工具/命令

| 软件包/工具/命令        | 描述                             |
| ----------------------- | -------------------------------- |
| [`yay`](#yay)           | Aur 助手                         |
| [`paru`](#paru)         | Aur 助手                         |
| `debtap`                | deb包转pacman包                  |
| **Shell**               |                                  |
| `zsh`                   | shell                            |
| `zim`                   | zsh 扩展管理                     |
| `fish`                  | shell                            |
| `fisher`                | shell 扩展管理                   |
| **终端**                |                                  |
| `konsole`               | 终端                             |
| `yakuake`               | 下拉终端                         |
| `wezterm`               | 终端                             |
| `kitty`                 | 终端                             |
| **Shell 工具**          |                                  |
| [`tmux`](./tmux.md)     | 终端复用                         |
| `bat`                   | better cat                       |
| `exa`                   | better ls                        |
| `fzf`                   | fuzzy finder                     |
| `yazi`                  | 终端下的 explorer                |
| `superfile`             | 终端下的文件管理器               |
| `hyperfine`             | 命令行性能测试                   |
| `mirro-rs`              | 查找速度最快的pacman镜像服务器   |
| `btop`                  | 终端资源监视器                   |
| `nvtop`                 | 终端GPU监视器                    |
| **基础设施**            |                                  |
| `watch`                 | watch 命令                       |
| `cfdisk`                |                                  |
| `lsblk`                 |                                  |
| `lscpu`                 |                                  |
| `lspci`                 |                                  |
| `lsusb`                 |                                  |
| `cfdisk`                |                                  |
| `efibootmgr`            | EFI 启动管理                     |
| `df`                    |                                  |
| `du`                    |                                  |
| `cpupower`              |                                  |
| `turbostat`             | CPU 温度频率监测                 |
| `btmgmt`                | BT 管理                          |
| `pw-top`                | pipewire top                     |
| `power-profiles-deamon` | 电源管理                         |
| **网络**                |                                  |
| `dnsmasq`               | DNS 服务                         |
| `openresolv`            | resolv.conf 管理                 |
| `whois`                 | 域名查询                         |
| `dig`                   | 域名解析工具                     |
| `nslookup`              | 域名解析工具                     |
| `netstat`               | 网络状态                         |
| `nftables`              | 安装 iptables-nft 包即可         |
| **GUI 工具**            |                                  |
| `pavu-control`          | pipewire GUI                     |
| `qpwgraph`              | 音频控制                         |
| `mission-center`        | 类 Windows 任务管理器            |
| `cpu-x`                 | CPU 信息监测                     |
| `qalculate`             | 计算器                           |
| **视频**                |                                  |
| `vlc`                   | 视频播放器                       |
| `mpv`                   | 精简视频播放器                   |
| `kdenlive`              | 视频剪辑                         |
| `obs-studio`            | 视频录制/推流                    |
| **音频**                |                                  |
| `elisa`                 | 音乐播放器, 自带电台             |
| `easyeffects`           | 音频效果                         |
| **图像**                |                                  |
| `gwenview`              | kde 图像查看器                   |
| `gimp`                  | 修图                             |
| `inkscape`              | 矢量图编辑                       |
| `pureref`               | 多图片查看, 钉图, 编辑           |
| **开发工具**            |                                  |
| `neovide`               | nvim的GUI                        |
| `blender`               | 建模                             |
| **通信**                |                                  |
| `thunderbird`           | 邮件                             |
| **办公**                |                                  |
| `okular`                | PDF/MD 阅读                      |
| `onlyoffice`            | 仿微软办公套件                   |
| `calligra`              | KDE 推出的办公套件               |
| **浏览器**              |                                  |
| `firefox`               | Linux 玩家人手一个, 对吧         |
| `zen-browser`           | 基于Firefox的浏览器              |
| `tor-browser`           | 很安全的基于Firefox的浏览器      |
| **磁盘管理**            |                                  |
| `partiionmanager`       | 分区工具                         |
| `gparted`               | 分区工具                         |
| `etcher`                | 刻录工具                         |
| **游戏**                |                                  |
| `mangohud`              | 游戏性能监控                     |
| `gamemode`              | 使用游戏模式运行游戏             |
| `steam`                 | Steam 客户端                     |
| `heroic`                | 第三方 Epic 客户端               |
| `lutris`                | 游戏管理器                       |
| `faugus-launcher`       | wine/proton 启动器               |
| **远程**                |                                  |
| `kdeconnect`            | 手机电脑局域网连接               |
| `scrcpy`                | Android 屏幕远程控制             |
| `remmina`               | 远程连接工具，支持VNC/RDP等      |
| `rustdesk`              | 屏幕分享                         |
| `frpc/frps`             | 内网穿透                         |
| `npc/nps`               | 内网穿透/P2P                     |
| **代理/VPN**            |                                  |
| `proxychains`           | 终端强制代理工具, 可代理ping流量 |
| `v2raya`                | v2ray web ui                     |
| `nekoray`               | sing-box GUI                     |
| `clash-verge-rev`       | clash-meta GUI                   |
| **玩具**                |                                  |
| `lolcat`                | 渐变色输出                       |
| `sl`                    | 火车                             |
| `cmatrix`               | 黑客字幕                         |
| `figlet`                | 艺术字                           |
| `pyfiglet`              | figlet Python 实现               |
| `toilet`                | 艺术字                           |
| `cowsay`                | 奶牛说                           |
| `asciiquarium`          | 水族馆                           |
| `nyancat`               | 彩虹猫                           |
| `carbonyl`              | 终端浏览器                       |
| `GriddyCode`            | 代码编辑器                       |
| **其他**                |                                  |
| `teamspeak3`            | 语音服务器                       |
| `motrix`                | 下载工具                         |
| `wireshark`             | 网络分析工具                     |
| `alist`                 | 整合各种网盘                     |
| **字体**                |                                  |
| `noto-fonts-cjk`        | 中文                             |
| `noto-fonts-emoji`      | 表情                             |
| `noto-fonts-extra`      |                                  |
| `ttf-fira-code`         | Fira Code                        |
| `ttf-firacode-nerd`     | Fira Code Nerd Font              |
| `ttf-maple`             |                                  |

### yay

```bash
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

### paru

GitHub: <https://github.com/Morganamilo/paru>

```bash
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
```

#### 配置paru

配置文件路径: `/etc/paru.conf`

##### 搜索结果倒叙排序

在paru配置中取消注释 `BottomUp`

```confini
[options]
...
#AurOnly
BottomUp
#RemoveMake
...
```

## 桌面环境配置

### KDE配置

#### KDE软件生态

| 软件               | 描述                             |
| ------------------ | -------------------------------- |
| `dolphin`          | 文件管理                         |
| `konsole`          | 终端                             |
| `kate`             | 文件编辑器                       |
| `yakuake`          | 下拉终端                         |
| `ark`              | 归档/压缩文件管理                |
| `filelight`        | 图形化文件占用, 类似spacesnipper |
| `kdf`              | 磁盘使用量                       |
| `partitionmanager` | 分区工具                         |
| `spectacle`        | 屏幕截图/录制                    |
| `gwenview`         | 图片查看                         |
| `kdenlive`         | 视频剪辑工具                     |
| `elisa`            | 音乐播放器                       |
| `okular`           | PDF/MD 阅读                      |
| `calligra`         | 办公套件                         |
| `krdp`             | 远程桌面服务器                   |
| `sweeper`          | 垃圾清理                         |
| `kwalletmanager`   | KDE密钥管理                      |
| `kdeconnect`       | 跨平台的手机电脑局域网连接工具   |
