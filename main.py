import os
import time
import usb_port
import burner

FIRMWARE_PATH = os.path.dirname(__file__) + "/烧录文件存放文件夹"

# 查找FIRMWARE_PATH路径下第一个.bin文件
bin_file = None
for file in os.listdir(FIRMWARE_PATH):
    if file.endswith(".bin"):
        bin_file = os.path.join(FIRMWARE_PATH, file)
        break
if bin_file is None:
    print("未找到.bin文件")
    exit(1)
else:
    print("bin文件 : ", os.path.basename(bin_file))


class USB_BURNER(object):
    usb: usb_port.USB_PORT

    def callback_connected(self, port: usb_port.USB_PORT):
        acm_path=port.get_dev_path()
        print("uSB插入", port.description)
        if os.path.exists(acm_path):
            print(acm_path)
        else:
            print("未找到acm路径")
            return
        burner.BURNER(bin_file).burner(acm_path)

    def callback_disconnect(self, port: usb_port.USB_PORT):
        print("USB拔出", port.description)

    def __init__(self, port_number: int, description: str):
        self.usb = usb_port.USB_PORT(port_number, description)
        self.usb.regester_callback_connected(self.callback_connected)
        self.usb.regester_callback_disconnect(self.callback_disconnect)
        self.usb.start_detection()


usb1 = USB_BURNER(8, "左单")
usb1 = USB_BURNER(6, "中上")
usb1 = USB_BURNER(5, "中下")


while True:
    time.sleep(1)
