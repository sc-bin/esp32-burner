import time
import usb_port

usb1 = usb_port.USB_PORT(5, "左单")
usb2 = usb_port.USB_PORT(6, "中上")
usb3 = usb_port.USB_PORT(8, "中下")

while True:
    time.sleep(0.1)

    if usb1.is_connected():
        print("USB1 插入",usb1.get_dev_path())
    else:
        print("USB1 未插入")

    if usb2.is_connected():
        print("USB2 插入",usb2.get_dev_path())
    else:
        print("USB2 未插入")

    if usb3.is_connected():
        print("USB3 插入",usb3.get_dev_path())
    else:
        print("USB3 未插入")
    
    print("\n\n")
