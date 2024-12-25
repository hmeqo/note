# Arch Linux

> [!NOTE]
> Github MD页面右上角可以打开目录树
>
> 本文所有引用部分均来自 archwiki
> Archlinux: <https://www.archlinux.org/>  
> Archlinuxcn: <https://www.archlinuxcn.org/>

## 安装教程

可以配合官网步骤食用: <https://wiki.archlinux.org/title/Installation_guide>

> [!NOTE]
> 编程中有许多特殊符号, 例如 \<xxx\> 代表根据实际情况填写的必填项, \[xxx\] 代表可选项, 请根据上下文自行判断

> [!WARNING]
> 如果你不熟悉 Linux, 建议先到其他有图形化安装发行版 (Manjaro, Mint 等), 熟悉后再尝试 Arch  
> 如果你想用 Arch 作为第一个 Linux 发行版, 建议在身边有人传教的情况下尝试, 且不要使用 archinstall 安装脚本安装
>
> Arch Linux 安装过程没有图形界面, 所有编辑操作都是在终端  
> 本文默认你能使用任何一种终端编辑器, 不会用请自行学习后再来, 建议学习 `vim`

### 视频教程

BiliBili: <https://www.bilibili.com/video/BV1J34y1f74E>  
BiliBili: <https://www.bilibili.com/video/BV1XY4y1f77S>

### 1. 准备

#### 获取系统信息

判断BIOS类型, 分区表类型

#### 硬件准备

一个刻录了安装镜像的U盘, 一台电脑

#### 提前分配空闲分区

强烈建议提前分区一块空闲分区, 使用Windows自带的分区工具或PE提前分一块空闲分区

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

> [!WARNING]
> 请勿对已经存在的分区使用 `cfdisk` 进行二次分区, 会导致分区损坏  
> ntfs文件系统分区建议提前使用Windows自带的分区程序或PE提前分一块空闲分区

几种主要的分区方案:

- 一个EFI分区(建议. 对于UEFI) + 一个Linux文件系统分区(必须) + 一个swap分区(可选)
- 一个EFI分区(建议. 对于UEFI) + 一个Linux文件系统分区(必须) + 一个swap分区(可选) + 一个home目录分区(可选)

如果电脑的启动方式是 UEFI, 需要单独分一个 EFI 分区, 大小推荐不小于 300MB, 如果是双系统推荐 500MB  
Windows/Linux 双系统本身已经有 EFI 分区了, 可以不用再分, 只需要把原来的 EFI 分区扩容到推荐大小即可

swap分区不推荐放第一个, 放后面的话以后如果需要修改比较方便, 对于swap分区/文件要分多大, 可以参考这里 [swap大小建议](#swap大小建议)

然后对照下表设置分区的类型

| 分区          | 类型             |
| ------------- | ---------------- |
| efi           | EFI System       |
| Linux文件系统 | Linux Filesystem |
| swap          | Linux swap       |

`cfdisk` 编辑完之后记得 `Write`, 否则你的更改不会生效

> [!NOTE]
> 也可以使用swapfile而非swap分区, 这样可以动态分配swap的大小, 无需调整分区, 可以等挂载完分区后再创建, [创建swapfile](#创建swapfile)  
> 在Arch安装过程中(非arch-chroot下), 请注意 swapfile 的文件路径, 例如系统根分区的临时挂载点是 /mnt, 那么应该把 dd 命令的 of 参数路径改成 /mnt/swapfile 或其他 /mnt 下的路径

##### 格式化分区

创建完分区之后, 需要格式化分区

- 对于 EFI 分区 (如果选择和 Windows 共用同一个 EFI 分区, 跳过这一步)

  ```bash
  mkfs.fat -F 32 /dev/efi_system_partition
  ```

- Linux 文件系统分区

  ```bash
  # mkfs.<格式>, 可以选择其他的格式, 如 btrfs 等 (善用 tab 键和wiki)
  mkfs.ext4 /dev/root_partition
  ```

- swap 分区 (或者swapfile, 如果没有可以先跳过这一步, 详细看下方 Note)

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

- swap分区 (或者swapfile, 如果没有可以先跳过这一步, 详细看下方 Note)

  ```bash
  swapon /dev/swap_partition
  ```

> [!NOTE]
> 如果你要创建swapfile, 挂载完 `/mnt` 就可以创建了, 创建到 `/mnt/swapfile`, [创建swapfile](#创建swapfile)  
> 如果你提前创建了, `swapoff` 之后移动swapfile到 `/mnt` 下然后 `swapon` 即可

### 2. 安装

#### 镜像源

如果需要可以先配置镜像源, 调整 `/etc/pacman.d/mirrorlist` 中镜像的顺序即可 (此更改只在当前安装过程中生效)

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

`linux-zen` 是一种性能较好的内核, 可以替换为其他内核, 例如 `linux`、`linux-lts`

`linux-headers` 是内核的头文件, dkms 会用到, 也可以需要时再安装

根据 CPU 选择安装 `intel-ucode` (Intel CPU) 或 `amd-ucode` (Amd CPU)  
这个安装项是可选的，如果装不了可以不用管

`vi/vim/neovim` 是一种常用的终端文件编辑器, 不会用可以装 `nano`

```bash
pacstrap -K /mnt base base-devel linux-zen linux-zen-headers linux-firmware [intel-ucode/amd-ucode] [vi/vim/neovim/nano] networkmanager git
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
| [`systemd-boot`](#systemd-boot) | 不支持    | 支持      | 手动       | 支持       | 简单省事           |
| [`rEFInd`](#refind)             | 不支持    | 支持      | 支持       | 支持       | 双系统推荐         |
| syslinux                        | 支持      | 部分支持  | 支持       | 支持       |                    |

参考文档: <https://wiki.archlinuxcn.org/wiki/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F>

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
pacman -S refind
refind-install
```

> [!WARNING]
> 当 refind-install 运行在chroot环境下 (例如：安装Arch Linux时的live环境) /boot/refind_linux.conf 内将会添加live系统的内核选项，而不是安装它的系统。
> 编辑 /boot/refind_linux.conf 并确保其中的 内核参数 对于你的系统是正确的，否则下次启动可能会出现内核错误。

###### rEFInd 主题

- refind-theme-regular
  github: <https://github.com/kmyi/refind-theme-regular>

### 4. 重启

安装完引导之后, `ctrl+d` 退出 chroot 环境, 重启电脑 (也可以先把后续操作做完再重启)

### 5. 后续操作

#### 考虑启用pacman的multilib和AUR

- [multilib软件仓库](#multilib软件仓库)
- [archlinuxcn软件仓库](#archlinuxcn软件仓库)
- [安装AUR助手](#安装aur助手)

#### 安装桌面环境

强烈建议创建一个非root用户再来使用桌面

- KDE

  可以参考 [KDE软件生态](#kde软件生态), 选择你需要的软件  
  sddm 是 kde 官方的会话管理器, 如果不喜欢你也可以换成别的

  ```bash
  pacman -S sddm plasma dolphin konsole yakuake zen-browser spectacle ark filelight

  # 然后设置sddm开机自启, 重启电脑后自动显示登录界面
  systemctl enable sddm
  ```

#### 安装各种驱动

- [音频驱动](#音频驱动)
- [显卡驱动](#显卡驱动)

## 系统配置

### 音频驱动

```bash
pacman -S pipewire pipewire-pulse pipewire-alsa pipewire-jack
# for multilib
pacman -S lib32-pipewire lib32-pipewire-jack
```

#### OpenAL

跨平台3D音频库

```bash
pacman -S openal
# for multilib
pacman -S lib32-openal
```

### 显卡驱动

注: 独显核显都需要安装驱动

- 通用

  `mesa` 开源 OpenGL 驱动, 支持所有主流显卡

  ```bash
  pacman -S mesa mesa-utils
  # for multilib
  pacman -S lib32-mesa-utils
  ```

- AMD

  安装 Vulkan 驱动

  ```bash
  pacman -S vulkan-radeon
  # for multilib
  pacman -S lib32-vulkan-radeon

  # 另一种选择, 但是不推荐
  pacman -S amdvlk
  # for multilib
  pacman -S lib32-amdvlk
  ```

- Intel

  安装 Vulkan 驱动

  ```bash
  pacman -S vulkan-intel
  # for multilib
  pacman -S lib32-vulkan-intel
  ```

- NVIDIA

  首先安装主要驱动, 有NVIDIA官方驱动, 和社区开源驱动, 选择其一安装即可

  - 官方驱动  
    NVIDIA 官方提供了闭源和开源两种驱动, 分别是 `nvidia` 和 `nvidia-open`(仅2060及以上)  
    nvidia-utils 中包含了 vulkan 驱动

    **注意: 对于非标准内核 (比如linux-zen), 请安装 nvidia-dkms / nvidia-open-dkms, 而不是 nvidia / nvidia-open**

    ```bash
    pacman -S nvidia-open/nvidia/nvidia-open-dkms/nvidia-dkms nvidia-utils [opencl-nvidia] [nvidia-prime]
    # for multilib
    pacman -S lib32-nvidia-utils
    ```

  - 社区开源驱动

    - `vulkan-nouveau` 开源 NVIDIA Vulkan 驱动, nouveau 已在内核模块中

      ```bash
      pacman -S vulkan-nouveau
      # for multilib
      pacman -S lib32-vulkan-nouveau
      ```

#### VA-API 视频加速

详情看这里: <https://wiki.archlinuxcn.org/wiki/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F#%E5%AE%89%E8%A3%85>

- Intel

  对于新Intel显卡 - Intel Media Driver for VAAPI — Broadwell+ iGPUs

  ```bash
  pacman -S intel-media-driver
  ```

  对于旧Intel显卡 - VA-API implementation for Intel G45 and HD Graphics family

  ```bash
  pacman -S libva-intel-driver
  # for multilib
  pacman -S lib32-libva-intel-driver
  ```

  检验 VA-API: <https://wiki.archlinuxcn.org/wiki/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F#%E6%A3%80%E9%AA%8C_VA-API>

#### EGL and GLX

- EGL

  ```bash
  pacman -S egl-wayland
  ```

- GLX

  ```bash
  pacman -S libva
  # for multilib
  pacman -S lib32-libva
  ```

### 双显卡管理

- optimus-manager (仅X11)

- envycontrol

  支持 Wayland

  - cli

    `envycontrol -q` 查询当前模式

    `envycontrol -s <mode>` 切换模式, 可选项：`hybrid`、`integrated`、`nvidia`

    `envycontrol --reset` 重置

  - 桌面环境适配

    支持 KDE Widget  
    `Optimus GPU Switcher`: <https://store.kde.org/p/2138365>

- switcheroo-control

  记得启用服务 `sudo systemctl enable --now switcheroo-control`

  - cli

    `switcherooctl launch <command>` 用独显运行命令

  - 桌面环境适配

    然后你应该能在桌面环境编辑.desktop的属性时看到使用独立显卡的选项  
    或者在.desktop的\[Desktop Entry\]中添加以下内容

    ```
    PrefersNonDefaultGPU=true
    X-KDE-RunOnDiscreteGpu=true
    ```

### fstab

archwiki: <https://wiki.archlinuxcn.org/wiki/Fstab>

> fstab(5)文件可用于定义磁盘分区，各种其他块设备或远程文件系统应如何装入文件系统。  
> 每个文件系统在一个单独的行中描述。这些定义将在引导时动态地转换为系统挂载单元，并在系统管理器的配置重新加载时转换。在启动需要挂载的服务之前，默认设置会自动 fsck 和挂载文件系统。例如，Systemd 会自动确保远程文件系统挂载（如 NFS 或 Samba ）仅在网络设置完成后启动。因此，在 /etc/fstab 中指定的本地和远程文件系统挂载应该是开箱即用的。有关详细信息，请参阅 systemd.mount(5) 。  
> mount命令将使用fstab，如果仅给出其中一个目录或设备，则填充其他参数的值。 这样做时，也将使用 fstab 中列出的挂载选项。  
> 编辑 `/etc/fstab`, 按照这样的格式编写

`<file system> <dir> <type> <options> <dump> <pass>`  
分别代表:

- `<file system>` 文件系统, 填写 `UUID=xxx`, 或者 `/dev/xxx`
- `<dir>` 挂载点, 对于 swap 或没有挂载点的分区, 填 `none`
- `<type>` 分区类型
- `<options>` 挂载选项  
  可选值(可多选, 用 `,` 分隔):
  - `defaults`: 默认
- `<dump>` 备份  
  此选项广泛用于 ext2/3 文件系统和磁带备份, 如今, 由于更新的文件系统和实用程序, 它已经过时了, 填 `0` 即可  
  可选值:
  - `0`: 不备份
  - `1`: 备份
- `<pass>` 系统启动后通过`fsck`检查  
  通常给根分区设置`1`其余分区设置`2`或`0`  
  可选值:
  - `0`: 不检查
  - `1`: 检查
  - `2`: 在1之后检查，但不一定检查

示例 :

```fstab
UUID=xxx  /    ext4 rw,relatime 0 1
UUID=xxxx /xxx ext4 defaults    0 2
```

### Swap

#### Swap大小建议

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

如果不想通过分区使用 swap, 可以创建 swapfile 作为 swap

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

### mkinitcpio的systemd钩子

systemd钩子可异步加载内核模块, 速度相对udev快一些, 可能不支持老旧硬件  
mkinitcpio 默认的钩子组合是以udev为主的, 如果需要更换为systemd

编辑 `/etc/mkinitcpio.conf`, 找到 HOOKS 配置项, 并替换为以下内容  
HOOKS上面应该是有注释说明的, 注释中也有systemd配置的示例

```conf
HOOKS=(base systemd autodetect modconf kms keyboard sd-vconsole sd-encrypt block filesystems fsck)
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

使用 `blkid /dev/nvme0n1p1`, 查看 UUID

示例:

```bash
❯ sudo blkid /dev/nvme0n1p1
/dev/nvme0n1p1: LABEL="archlinux" UUID="4483df75-6a1d-42a1-9a3e-66406b7a9cac" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="1cf11453-a83c-4dd9-9f88-28a24754818f"
```

然后将 `resume=UUID=xxxxxx` 写入到内核参数  
对于 swapfile, 需要额外加上 `resume_offset=xxxxxx`, 表示偏移量, 偏移量可以通过此命令快速获取 `filefrag -v <swap_file> | awk '$1=="0:" {print substr($4, 1, length($4)-2)}'`

获取 swapfile 偏移量示例:

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

### 多线程下载

在 pacman 配置文件找到并取消注释 `ParallelDownloads`

```confini
[options]
...
#VerbosePkgLists
ParallelDownloads = 5
...
```

### 颜色

在 pacman 配置文件中取消 `Color` 的注释

```confini
[options]
...
#UseSyslog
Color
#NoProgressBar
...
```

### pacman的其他软件仓库

#### multilib软件仓库

安装Steam或其他32位软件包需要此软件源, 在 pacman 配置文件中取消注释 multilib 部分然后运行 `sudo pacman -Sy`

```conf
[multilib]
Include = /etc/pacman.d/mirrorlist
```

#### archlinuxcn软件仓库

> Arch Linux 中文社区仓库是由 Arch Linux 中文社区驱动的非官方软件仓库，包含许多官方仓库未提供的额外的软件包，以及已有软件的 git 版本等变种。一部分软件包的打包脚本来源于 AUR，但也有许多包与 AUR 不一样。

添加步骤: 将下面内容加入 pacman 配置文件末尾 `/etc/pacman.conf`

```conf
[archlinuxcn]
## 北京外国语大学 (北京) (ipv4, ipv6, http, https)
Server = https://mirrors.bfsu.edu.cn/archlinuxcn/$arch
```

> [!TIP]
> 更多archlinuxcn镜像服务器查看此处 <https://github.com/archlinuxcn/mirrorlist-repo>

然后安装archlinuxcn的密钥环

```bash
sudo pacman -Sy archlinuxcn-keyring
```

2023年10月之后, 新系统下安装cn密钥环如果遇到以下报错

```bash
error: archlinuxcn-keyring: Signature from "Jiachen YANG (Arch Linux Packager Signing Key) <farseerfc@archlinux.org>" is marginal trust
```

请在本地信任 farseerfc 的 GPG key, 并再次尝试安装

```bash
sudo pacman-key --lsign-key "farseerfc@archlinux.org"
```

#### Arch 用户软件仓库 (AUR)

> Arch 用户软件仓库（Arch User Repository，AUR）是为用户而建、由用户主导的 Arch Linux 软件仓库。AUR 中的软件包以软件包生成脚本（PKGBUILD）的形式提供，用户自己通过 makepkg 生成包，再由 pacman 安装。创建 AUR 的初衷是方便用户维护和分享新软件包，并由官方定期从中挑选软件包进入 extra 仓库。本文介绍用户访问和使用 AUR 的方法。  
> 许多官方仓库软件包都来自 AUR。通过 AUR，大家相互分享新的软件包生成脚本（PKGBUILD 和其他相关文件）。用户还可以为软件包投票。如果一个软件包投票足够多、没有许可证问题、打包质量好，那么它就很有希望被收录进官方 community 仓库（以后就可以直接通过 pacman 或 abs 安装了）。

> [!WARNING]
> 警告： AUR 中的软件包是由其他用户编写的，这些 PKGBUILD 完全是非官方的，未经彻底审查。使用这些文件的风险由您自行承担。

##### 安装AUR助手

AUR助手帮你省去了上网站搜索AUR包, 克隆仓库手动执行命令的过程, 还能自动更新  
可选的 aur 助手有: [yay](#yay)、[paru](#paru), 使用 aur 助手代替 pacman

##### 手动安装AUR软件包

如果你没有AUR助手, 又需要安装AUR软件包, 可以通过以下步骤安装

首先确认AUR包名, 然后执行以下命令

```bash
git clone https://aur.archlinux.org/<包名>.git
cd <包名>
makepkg -si
```

### Arch Linux Archive

> Arch Linux 存档库（Arch Linux Archive，简称 ala），以前称为 Arch Linux 回滚机（Arch Linux Rollback Machine，简称 ARM），保存了官方仓库快照、iso 镜像和引导程序包的历史版本。

编辑 `/etc/pacman.d/mirrorlist`, 注释或删除原有Server, 并加入以下内容, 或者给 `/etc/pacman.conf` 中的每个仓库单独设置 Server 也可以

```conf
Server=https://archive.archlinux.org/repos/<year>/<month>/<day>/$repo/os/$arch
```

文档: <https://wiki.archlinuxcn.org/wiki/Arch_Linux_Archive>

### 彩蛋

在 pacman 配置中加入 `ILoveCandy`, 进度条会被替换成吃豆人

```confini
[options]
ILoveCandy
```

### pacman以及AUR助手常用命令

以下为个人理解, 有些地方可能并不准确或非官方叫法

pacman 使用方式和 vim 很像, 格式为一个Operator加n个Motion

常用的 Operator 有 `-S` (同步/安装)、`-R` (卸载)、`-Q` (查询本地)

| 常用命令                       | 描述                                                                  |
| ------------------------------ | --------------------------------------------------------------------- |
| **通用**                       |                                                                       |
| `pacman -Syu`                  | 更新数据库(y)和软件包(u)                                              |
| `pacman -S <软件包>`           | 安装软件包                                                            |
| `pacman -Ss <regex>`           | 搜索软件包(s)                                                         |
| `pacman -Si <软件包>`          | 查看软件包信息(i)                                                     |
| `pacman -Syyuu`                | 强制更新数据库(yy)并升级/降级软件包(uu)                               |
| `pacman -S --rebuild <软件包>` | 重新构建和安装软件包(--rebuild)                                       |
| `pacman --fm nvim -S <软件包>` | 安装软件包, 并在安装之前编辑仓库, 例如修改 PKGBUILD (--fm)            |
| `pacman -Rsn <软件包>`         | 删除软件包以及相关依赖(s)和配置文件(n)                                |
| `pacman -Rsnc <软件包>`        | 删除软件包以及相关依赖(s)和配置文件(n), 并且删除依赖它的软件包(c)     |
| `pacman -Rsndd <软件包>`       | 强制删除软件包以及相关依赖(s)和配置文件(n), 忽略依赖问题(dd)          |
| `pacman -Rsnc $(pacman -Qtdq)` | 删除所有孤包                                                          |
| `pacman -Q`                    | 列出已安装的软件包                                                    |
| `pacman -Qs <regex>`           | 搜索软件包(s)                                                         |
| `pacman -Qi <软件包>`          | 查看软件包信息(i)                                                     |
| `pacman -Ql <软件包>`          | 查看软件包的文件路径(l), 不包含软件后续产生的文件, 如 `~/.config/xxx` |
| `pacman -Qo <file>`            | 查询已安装的文件或命令所属软件包(o)                                   |
| `pacman -Qdtq`                 | 列出孤包(dt), 即不被需要(t)的软件包依赖(d), 不显示版本信息(q)         |
| `pacman -Qeq`                  | 列出自己安装的软件包(e), 不显示版本信息(q)                            |
| `pacman -Qetq`                 | 列出自己安装(e)的不被其他软件包依赖(t)的软件包, 不显示版本信息(q)     |
| `pacman -Qk`                   | 校验软件包文件缺失(k)                                                 |
| `pacman -Qkk`                  | 校验软件包文件完整性(kk)                                              |
| `pacman -F <file>`             | 查询文件或命令所属软件包                                              |
| `pacman -Fy`                   | 更新文件数据库(y)                                                     |
| `pacman -U <file>`             | 从文件安装软件包(package.tar.gz)                                      |
| **paru**                       |                                                                       |
| `paru -c`                      | 删除不再需要的软件包 (不推荐, 不会删除软件包的依赖)                   |
| `paru -Gc <软件包>`            | 查看aur软件包评论                                                     |

### 软件包降级

- 所有软件包降级

  [Arch Linux Archive](#Arch Linux Archive)

- 降级单个软件包

  ```bash
  sudo downgrade <package_name>
  ```

- AUR降级

  AUR包通常是git仓库, 所以只需要使用 nvim 或其他方式 reset/checkout 到你想要的版本

  ```bash
  paru --fm nvim -S <package_name>
  ```

## 常用软件包/工具/命令

| 软件包/工具/命令          | 描述                             |
| ------------------------- | -------------------------------- |
| [`yay`](#yay)             | Aur 助手                         |
| [`paru`](#paru)           | Aur 助手                         |
| `debtap`                  | deb包转pacman包                  |
| **Shell**                 |                                  |
| `zsh`                     | shell                            |
| `fish`                    | shell                            |
| `fisher`                  | shell 扩展管理                   |
| **终端**                  |                                  |
| `konsole`                 | 终端                             |
| `yakuake`                 | 下拉终端                         |
| `wezterm`                 | 终端                             |
| `kitty`                   | 终端                             |
| **Shell 工具**            |                                  |
| `reflector`               | pacman镜像服务器地址生成         |
| `mirro-rs`                | 查找速度最快的pacman镜像服务器   |
| [`tmux`](./tmux.md)       | 终端复用                         |
| `bat`                     | better cat                       |
| `exa`                     | better ls                        |
| `fzf`                     | fuzzy finder                     |
| `yazi`                    | 终端下的 explorer                |
| `superfile`               | 终端下的文件管理器               |
| `hyperfine`               | 命令行性能测试                   |
| `btop`                    | 终端资源监视器                   |
| **基础设施**              |                                  |
| `lspci`                   |                                  |
| `lsusb`                   |                                  |
| `watch`                   | 定时执行                         |
| `at`                      | 定时执行                         |
| `crontab`                 | 定时任务                         |
| `bluetoothctl`            | Bluetooth 管理                   |
| `btmgmt`                  | Bluetooth 管理                   |
| `pw-top`                  | pipewire top                     |
| `tlp+tlp-rdw+tlpui`       | 电源管理                         |
| `power-profiles-deamon`   | 电源管理                         |
| `pamixer`                 |                                  |
| `brightnessctl`           |                                  |
| `authbind`                | 非root绑定特权端口               |
| **分区管理**              |                                  |
| `efibootmgr`              | EFI 启动管理                     |
| `lsblk`                   |                                  |
| `cfdisk`                  |                                  |
| `df`                      |                                  |
| `du`                      |                                  |
| **网络**                  |                                  |
| `ss/netstat`              | 网络状态                         |
| `nftables`                | 安装 iptables-nft 包即可         |
| `whois`                   | 域名查询                         |
| `dig`                     | 域名解析工具                     |
| `nslookup`                | 域名解析工具                     |
| `nali`                    | ip归属查询                       |
| `dnsmasq`                 | DNS 服务                         |
| `mtr`                     | traceroute 和 ping 功能的结合    |
| `nexttrace`               | 网络路径分析                     |
| `openresolv`              | resolv.conf 管理                 |
| `nethogs`                 | 网络流量监听                     |
| `wireshark`               | 网络分析工具                     |
| **CPU**                   |                                  |
| `lscpu`                   |                                  |
| `turbostat`               | CPU 温度频率监测                 |
| `cpupower`                |                                  |
| **GPU**                   |                                  |
| `nvtop`                   | 终端GPU监视器                    |
| `intel_gpu_top`           |                                  |
| `nvidia-smi`              |                                  |
| `prime-run`               |                                  |
| **hack**                  |                                  |
| [`fcrackzip`](#fcrackzip) | 压缩包破解                       |
| **GUI 工具**              |                                  |
| `pavu-control`            | pipewire GUI                     |
| `qpwgraph`                | 音频控制                         |
| `mission-center`          | 类 Windows 任务管理器            |
| `cpu-x`                   | CPU 信息监测                     |
| `qalculate`               | 计算器                           |
| **视频**                  |                                  |
| `vlc`                     | 视频播放器                       |
| `mpv`                     | 精简视频播放器                   |
| `kdenlive`                | 视频剪辑                         |
| `obs-studio`              | 视频录制/推流                    |
| **音频**                  |                                  |
| `elisa`                   | 音乐播放器, 自带电台             |
| `easyeffects`             | 音频效果                         |
| **图像**                  |                                  |
| `gwenview`                | kde 图像查看器                   |
| `gimp`                    | 修图                             |
| `inkscape`                | 矢量图编辑                       |
| `pureref`                 | 多图片查看, 钉图, 编辑           |
| **开发工具**              |                                  |
| `neovide`                 | nvim的GUI                        |
| `blender`                 | 建模                             |
| **通信**                  |                                  |
| `thunderbird`             | 邮件                             |
| **办公**                  |                                  |
| `okular`                  | PDF/MD 阅读                      |
| `onlyoffice`              | 仿微软办公套件                   |
| `calligra`                | KDE 推出的办公套件               |
| **浏览器**                |                                  |
| `firefox`                 | Linux 用户人手一个               |
| `zen-browser`             | 基于Firefox的浏览器              |
| `tor-browser`             | 很安全的基于Firefox的浏览器      |
| **磁盘管理**              |                                  |
| `partiionmanager`         | 分区工具                         |
| `gparted`                 | 分区工具                         |
| `etcher`                  | 刻录工具                         |
| **游戏**                  |                                  |
| [`mangohud`](#mangohud)   | 游戏性能监控                     |
| `goverlay`                | mangohud 的图形化控制台          |
| `gamemode`                | 使用游戏模式运行游戏             |
| `steam`                   | Steam 客户端                     |
| `heroic`                  | 第三方 Epic 客户端               |
| `lutris`                  | 游戏管理器                       |
| `faugus-launcher`         | wine/proton 启动器               |
| **远程**                  |                                  |
| `kdeconnect`              | 手机电脑局域网连接               |
| `scrcpy`                  | Android 屏幕远程控制             |
| `remmina`                 | 远程连接工具，支持VNC/RDP等      |
| `rustdesk`                | 屏幕分享                         |
| `frpc/frps`               | 内网穿透                         |
| `npc/nps`                 | 内网穿透/P2P                     |
| **代理/VPN**              |                                  |
| `proxychains`             | 终端强制代理工具, 可代理ping流量 |
| `v2raya`                  | v2ray web ui                     |
| `nekoray`                 | sing-box GUI                     |
| `clash-verge-rev`         | clash-meta GUI                   |
| **玩具**                  |                                  |
| `lolcat`                  | 渐变色输出                       |
| `sl`                      | 火车                             |
| `cmatrix`                 | 黑客字幕                         |
| `figlet`                  | 艺术字                           |
| `pyfiglet`                | figlet Python 实现               |
| `toilet`                  | 艺术字                           |
| `cowsay`                  | 奶牛说                           |
| `asciiquarium`            | 水族馆                           |
| `nyancat`                 | 彩虹猫                           |
| `carbonyl`                | 终端浏览器                       |
| `griddycode`              | 代码编辑器                       |
| **其他**                  |                                  |
| `teamspeak3`              | 语音服务器                       |
| `motrix`                  | 下载工具                         |
| `alist`                   | 整合各种网盘                     |
| `davfs`                   |                                  |
| `kanshi`                  | Wayland 动态显示屏切换           |
| **字体**                  |                                  |
| `noto-fonts-cjk`          | 中文                             |
| `noto-fonts-emoji`        | 表情                             |
| `noto-fonts-extra`        |                                  |
| `ttf-fira-code`           | Fira Code                        |
| `ttf-firacode-nerd`       | Fira Code Nerd Font              |
| `ttf-maple`               |                                  |

### yay

- 安装

  ```bash
  sudo pacman -S --needed base-devel
  git clone https://aur.archlinux.org/yay.git
  cd yay
  makepkg -si
  ```

### paru

GitHub: <https://github.com/Morganamilo/paru>

- 安装

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

### fcrackzip

示例:

```bash
# -b 暴力破解
# -c 指定暴力破解包含的字符, 具体看help
# -l 指定密码长度, n 或者 n1-n2
fcrackzip -b -c 'aA1!' -l 6 example.zip
```

### mangohud

性能监测工具, 如果游戏是32位的, 需要安装32位的mangohud

- 安装

  ```bash
  pacman -S mangohud
  # for multilib
  pacman -S lib32-mangohud
  ```

- 示例

  ```bash
  mangohud glxgears
  # Steam游戏参数
  mangohud %command%
  ```

  对于steam或其他支持MANGOHUD的游戏, 也可以这么写

  ```bash
  MANGOHUD=1 %command%

  ```

#### mangohud with opengl

对于 OpenGL, 可能需要 `--dlsym` 参数

```bash
mangohud --dlsym glxgears
```

#### mangohud 快捷键

- R_SHIFT + F12

  切换显示/隐藏HUD

- R_SHIFT + F11

  切换HUD的位置

- R_SHIFT + F10

  切换HUD的预设

- L_SHIFT + F2

  开始/结束Log

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

## KVM 显卡直通

以 intel + nvidia 举例

首先需要知道显卡的PCI ID, 可以通过 lspci 查看, 值在末尾方括号中

```bash
$ lspci -nn | grep "NVIDIA"
# 显卡
01:00.0 VGA compatible controller [0300]: NVIDIA Corporation GA107M [GeForce RTX 3050 Ti Mobile] [10de:25a0] (rev a1)
# 声卡
01:00.1 Audio device [0403]: NVIDIA Corporation GA107 High Definition Audio Controller [10de:2291] (rev a1)
```

添加内核参数, vfio-pci.ids 填写显卡PCI ID

```bash
... intel_iommu=on vfio-pci.ids=10de:25a0,10de:2291
```

也可以不通过内核参数, 在modprobe中配置, `/etc/modprobe.d/vfio.conf`

```modconf
options vfio-pci ids=10de:25a0,10de:2291
softdep nvidia pre: vfio-pci
```

通过 virt-manager 配置pci直通显卡即可, 具体自行搜索教程 (施工中)

## Wiki

Archwiki: <https://wiki.archlinux.org/title/Main_page>

### Linux 基础目录

以下只是简短描述, 详情见: <https://www.freedesktop.org/software/systemd/man/latest/file-hierarchy.html>

- `/boot`

  存放启动镜像各种启动配置的文件夹

- `/dev` - devtmpfs

  设备目录, 例如和主板连接的硬盘, u盘, 鼠标, 键盘等设备都在这里显示

- `/etc`

  配置文件目录

- `/home`

  用户目录, 例如用户 `hmeqo` 的用户目录是 `/home/hmeqo`, 这个位置并非绝对的, 可以修改

- `/mnt`

  用于挂载其他分区, 例如将 windows 盘挂载到 `/mnt/windows`

- `/opt`

  用于存放软件包的目录, 通常是一些因某些原因不能把软件拆分开的商业软件

- `/proc` - proc

  进程目录, 在这里可以看到当前正在运行的进程, 以及各种信息

- `/root`

  root 用户的家目录

- `/run` - tmpfs

  用于存放运行时数据, 套接字, 和其他类似文件, 通常仅对特权程序可写

- `/srv`

  srv - Service Data, 用于存放服务的目录

- `/sys` - sysfs

  一个虚拟内核文件系统, 主要提供与内核接口相关的 API

  例如临时关闭 Intel CPU 睿频: `echo 1 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo`

- `/tmp` - tmpfs

  临时文件目录

- `/usr`

  用于存放应用程序的目录

- `/var`

  用于存放数据的目录 (随时会变化的数据)

- `/bin` -> `/usr/bin`

- `/lib` -> `/usr/lib`

- `/lib64` -> `/usr/lib`

- `/sbin` -> `/usr/bin`

- `EFI`

  EFI 分区目录, 如果你把 EFI 分区挂载到了 `/boot`, 那么你可以在 `/boot/EFI` 中找到启动项  
  如果你的 EFI 挂载点是 `/`, 那么对应的 EFI 目录则是 `/EFI`

### 文件系统

- ext4

- xfs

- zfs

- btrfs

- tmpfs

  挂载在内存的文件系统

### WINE/PROTON 运行 Windows 应用/游戏

#### WINE 生态中的各种工具介绍

- Wine

  - 是什么: Wine 是一个开源兼容层, 允许在类 Unix 操作系统 (如 Linux、macOS) 上运行设计为在 Microsoft Windows 上运行的应用程序 (特别是那些使用 Win32 API 的应用程序)  
    其原理是重写了 Windows 的 dll

- DXVK

  DXVK 一个用于转换 DirectX9/10/11 API 为 Vulkan API 的兼容层, 能大幅度提升游戏性能, 甚至超越 Windows, DXVK 不止能用于 Linux, 也能在 Windows 上使用

- VKD3D

  VKD3D 一个用于转换 DirectX12 API 为 Vulkan API 的兼容层, 不过 VKD3D 不像 DXVK 那样已经发展了很久, VKD3D 的游戏性能在某些情况下可能只有 Windows 的 2/3

- Proton

  - 是什么: Proton 是 Valve 为其数字发行平台 Steam 开发的一个开源工具, 基于 Wine, 但专门为运行 Windows 游戏进行了优化  
    Proton 整合了 DXVK, VKD3D 等一系列工具, Valve 对 Proton 的更改都会回馈到上游 (Wine, DXVK, VKD3D 等), Proton 极大促进了 Linux 游戏/软件生态的发展
  - 与 Wine 的关系: Proton 构建于 Wine 之上, 使用 Wine 的代码库作为其核心, 并添加了 Valve 自己的补丁、优化和额外功能, 以提高游戏的兼容性和性能

- Proton-GE

  由 GloriousEggroll 创建的一个 Proton 定制版, 相比于 Proton, 整合了更多 Proton 没有或暂时没有的功能, 有更好的游戏兼容性

- Wine-GE

  由 GloriousEggroll 创建的一个 Wine 定制版, Wine-GE 是为非 Steam 游戏分发的版本, 因为 Proton 是专为 Steam 开发, 有很多非 Steam 游戏不需要的功能

- UMU-Launcher

  由于 Proton 是专门为 Steam 游戏开发的, 在 Wine9.0 之前, 一般建议用 Wine-GE 运行非 Steam 游戏/应用, Proton-GE 运行 Steam 游戏  
  但在 9.0 之后, GE 作者不再分发 Wine-GE 版本, 转而开发了 UMU-Launcher, 用 Proton-GE 运行非 Steam 游戏/应用

- GPTK (Game Porting Toolkit)

  Apple 为 macOS 开发的基于 Wine 的游戏兼容层

> [!NOTE]
> Proton 能够以高性能运行 Windows 游戏, 主要功劳在于 DXVK 和 VKD3D  
> 各种利用 Wine 运行 Windows 游戏的启动器都默认帮你配好了 DXVK, VKD3D 等工具, 其游戏性能和 Proton 无太大区别

#### WINE/PROTON GUI 启动器

- Steam

  伟大无需多言

- lutris

  流行且通用的游戏/应用启动/管理工具

- heroic-games-launcher

  非官方 Epic 游戏启动器

- bottles

  UI 不错

- faugus-launcher

  利用 UMU-Launcher 的游戏/应用启动器

- CrossOver

  付费版 Wine
