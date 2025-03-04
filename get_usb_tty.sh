#!/bin/bash
# 传入一个usb编号（使用lsusb命令，里面的Bus参数）
# 如果该usb被插入且出现ttyACM设备，则返回dev的路径


USB_NUM=$1
if [ -z "$USB_NUM" ]; then
    echo "null"
    exit 1
fi
USB_DEVICE="/sys/bus/usb/devices/$USB_NUM-1"
if [ ! -e "$USB_DEVICE" ]; then
    echo "no"
    exit 1
fi

USB_TTY="$USB_DEVICE/$USB_NUM-1:1.0/tty"
DEV_TTY="/dev/$(ls $USB_TTY)"
if [ -e $DEV_TTY ]; then
    echo "$DEV_TTY"
    exit 0
fi

echo "no"
exit 1
