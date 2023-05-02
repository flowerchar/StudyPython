## 无线网卡驱动安装

大部分软件安装与配置，都需要网络，如果网络都没处理好，下边的环境配置也就无从谈起了。

有线网卡的驱动一般都会自动装好，但是无线网卡的驱动经常因为版本或内核问题，或是网卡太新导致系统里的旧版无线网卡驱动不兼容。以下提供两种解决方案：

### 一、编译无线网卡驱动方案(推荐)

如果以上不能解决你的无线网卡问题，找不到无线网卡或是搜不到wifi信号，那请看终极解决方案：下载无线网卡驱动自行编译安装即可。

1. 下载源码（确保有git）：

```
sudo apt install git
git clone https://gitee.com/tangyang/backport-iwlwifi.git

#或直接从原始位置获取
# git clone https://git.kernel.org/pub/scm/linux/kernel/git/iwlwifi/backport-iwlwifi.git
```

1. 编译源码

```
cd backport-iwlwifi
sudo make defconfig-iwlwifi-public

# 这个sed修改.config操作是可选的，先不执行他，如果最后你sudo make install重启之后还不行，再试试加上这句话来一遍
# sudo sed -i 's/CPTCFG_IWLMVM_VENDOR_CMDS=y/# CPTCFG_IWLMVM_VENDOR_CMDS is not set/' .config

sudo make -j4
```

1. 安装刚刚编译好的驱动

```
sudo make install
```

最后重启电脑，顺利的话，应该就解决了你的问题啦。

参考的是kernel官方文档：https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi/core_release#core_release

### 二、升级内核并手动安装驱动方案

- **查看自己的网卡型号**

在Ubuntu下目前因为没有驱动，不好找无线网卡型号，可以尝试以下命令`lspci | grep -i net`或`iwconfig`，或直接到品牌电脑官网查看对应型号。

如果能进入Windows，可以到`控制面板-设备管理器-网络适配器`中查看包含`Wireless`的项目，比如`Intel Dual Band Wireless-AC 8265`

- **打开网卡驱动下载页面：**

[intel官网（推荐）](https://www.intel.com/content/www/us/en/support/articles/000005511/network-and-i-o/wireless-networking.html) 或 [kernel官网](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi)

找到自己网卡对应固件程序并下载，本例为8265，把文件`iwlwifi-8265-ucode-22.361476.0.tgz`保存好，一定要主要找自己的网卡设备对应的固件！并留意Kernels的版本，后边要用

| Device                            | Kernels | Firmware                                                     |
| :-------------------------------- | :------ | :----------------------------------------------------------- |
| Intel® Dual Band Wireless-AC 8265 | 4.6+    | [iwlwifi-8265-ucode-22.361476.0.tgz](https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-8265-ucode-22.361476.0.tgz) |

- **查看内核版本**

```
uname -r
```

**如果显示的数字开头>=4.6，则可直接进行下一步**！说明你的内核已经满足这个无线网卡驱动了！不用再更新内核啦！不用再更新内核啦！不用再更新内核啦！重要的事情说3遍！！！

否则说明你硬件太新，系统太老，需要更新系统内核，才能安装运行你的新网卡，按照如下步骤更新内核：

- 确认要下载的版本，>=4.6即可，我们更新为4.8的。（本例以64位OS为例）
- 打开内核下载网站，[链接在此](https://kernel.ubuntu.com/~kernel-ppa/mainline/)
- 在终端执行下载命令

```
wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.8/linux-headers-4.8.0-040800_4.8.0-040800.201610022031_all.deb

wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.8/linux-headers-4.8.0-040800-generic_4.8.0-040800.201610022031_amd64.deb

wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.8/linux-image-4.8.0-040800-generic_4.8.0-040800.201610022031_amd64.deb
```

- 安装这些deb包，完毕后重启电脑

```
sudo dpkg -i *.deb
```

- 再次检查确定内核已升级为4.8+

```
uname -r
```

重启电脑后，有可能此时无线网卡已经可以使用，如果还不行，再往下走：

- 解压刚刚下载的iwlwifi-8265-ucode-22.361476.0.tgz并复制驱动到`/lib/firmware`**

```
# 先解压压缩包
tar -zxvf iwlwifi-*.tgz
# 进入解压目录后，拷贝文件到/lib/firmware目录
sudo cp iwlwifi-*.ucode /lib/firmware
```

- **更新grub并重启**

```
sudo update-grub
sudo update-pciids
sudo reboot
```

# 系统全局镜像配置

配置镜像的目的是可以在更新系统组件，安装各种软件工具时，不需要访问默认国外的下载地址。而是访问国内同步过来的镜像。配置阿里云镜像源`Ubuntu18.04`版，其他版本可自行到阿里云镜像官网查找。

[阿里云镜像源官网](https://developer.aliyun.com/mirror/) 或 [国内高校开源镜像站友情链接](http://mirrors.hust.edu.cn/links.html)

当然，你也可以通过`设置->软件&更新->`来选择中国的服务器，这里不作展开介绍。

- 备份系统配置

```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
```

- 编辑配置

```
sudo gedit /etc/apt/sources.list
```

- 修改内容如下（适用于Ubuntu18.04）

```
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```

- 修改完保存，进行更新

```
sudo apt-get update
```

# 搜狗输入法安装

### 1. 确认fctix环境

Ctrl+Alt+T，打开终端Terminal；

首先确定有没有fcitx，在终端输入`fcitx`回车，如果提示未找到命令，则安装：

```
sudo apt-get install fcitx
```

### 2. 安装搜狗sogou拼音

#### 方式一：安装包安装(推荐)

1. 点击立即下载64bit，链接https://pinyin.sogou.com/linux/?r=pinyin
2. 到下载目录中执行安装命令：

```
sudo dpkg -i sogoupinyin_*.deb
```

1. 如果安装过程提示有依赖问题，使用以下命令解决：

```
sudo apt-get install -f
```

#### 方式二：在线安装

直接联网在线安装：

```
sudo add-apt-repository ppa:fcitx-team/nightly
sudo apt-get update
sudo apt-get install fcitx-sogoupinyin 
```

### 3. 开启fcitx环境，搜狗输入法

在命令行输入`im-config`，点“确定”->"yes"->选择fcitx->"确定"，随后**重启机器**即可。

> 注意
>
> 如果重启后仍旧无法通过`Ctrl+空格`切出搜狗输入法：
>
> 可输入`fcitx-config-gtk3`搜索并将sogou添加到列表中。注意把`Only Show Current Language(只显示当前语言)`前边的勾勾去掉。
>
> 如果没有`im-config`和`fcitx-config-gtk3`命令,可通过以下命令安装，仍旧注意确保fcitx已安装：
>
> ```
> sudo apt-get install im-config fcitx-config-gtk
> ```

# 用户目录中英文修改

用户目录里的**“下载”**，**“桌面”**如果是中文，使用命令打开他们就十分的费劲，可以使用以下方法快速的修改为英文。

**Ctrl+Alt+T** （默认终端快捷键）打开终端，输入以下命令：

```
# 首先更改系统语言环境为英文
export LANG=en_US
xdg-user-dirs-gtk-update
```

此时会弹出界面，选择带有**“update”**字样的选项或者是**“更新名称”**

```
# 接着更改回中文语言环境
export LANG=zh_CN.UTF-8
xdg-user-dirs-gtk-update
# 此时再次弹出界面，选择“保留旧的名称”
```

# python-pip镜像源

### 配置Python安装源

#### 临时指定安装源

如安装opencv-python的3.4.0.12版本，可直接使用`-i`参数指定源

```
pip3 install -i https://pypi.douban.com/simple opencv-python==3.4.0.12
```

#### 永久指定安装源

每次临时指定源地址比较麻烦，可以通过以下方式配置永久源

在主目录创建.pip文件夹

```
mkdir ~/.pip
```

编写~/.pip/pip.conf

```
sudo gedit ~/.pip/pip.conf
```

并添加以下内容

```
[global]
trusted-host=pypi.douban.com
index-url=https://pypi.douban.com/simple/
timeout=6000
```

此时，默认`pip install xxx`已经可以自动走镜像地址， 但是sudo模式下的pip和pip3并不能使用此镜像。所以要把这个pip.conf复制到`/root/.pip`目录下

```
sudo mkdir -p /root/.pip
sudo cp ~/.pip/pip.conf /root/.pip/
```

可用的源有:

```
清华大学：https://pypi.tuna.tsinghua.edu.cn/simple 
阿里云：http://mirrors.aliyun.com/pypi/simple/ 
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
华中理工大学：http://pypi.hustunique.com/ 
山东理工大学：http://pypi.sdutlinux.org/ 
豆瓣：https://pypi.douban.com/simple/
```

### pip依赖修复

如果安装过程中遇到pip环境工具问题，可以通过以下命令重装pip和pip3

```
sudo apt-get install --reinstall python3-pip
sudo apt-get install --reinstall python-pip
```

