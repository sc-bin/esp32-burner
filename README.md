# esp32-burner
在核桃派1b上运行的esp32烧录器,开发时使用的是2.5.1版本debian12 server镜像,使用3.5寸屏

## 1.首先需要在板上安装两个库
```shell
sudo pip3 install esptool
sudo pip3 install adafruit-ampy
```
## 2.把本文件夹存放到/boot/start路径下
## 3.运行本文件夹下的安装脚本
```shell
sudo ./install.sh
```
或者可以把 **boot-start** 这个文件夹下的两个脚本复制到 **/boot/start**文件夹下

esp32-burner-first.sh 脚本用于开启3.5寸屏和启用xorg带鼠标终端

esp32-burner-normal.sh 用于在开机时运行qt界面

