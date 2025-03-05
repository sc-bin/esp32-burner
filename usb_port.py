import os


class USB_PORT(object):
    port_number: int
    description: str
    USB_DEV_PATH: str

    def __init__(self, port_number: int, description: str):
        self.port_number = port_number
        self.description = description
        self.USB_DEV_PATH = "/sys/bus/usb/devices/" + str(port_number) + "-1"

    # 该usb口是否插入

    def is_connected(self) -> bool:
        """
        该usb口是否插入
        """
        if os.path.exists(self.USB_DEV_PATH):
            return True
        return False

    def get_dev_path(self) -> str:
        """
        获取该usb口对应的设备路径
        """
        usb_deb_tty_path = self.USB_DEV_PATH + "/" + str(self.port_number) + "-1:1.0/tty"
        if os.path.exists(usb_deb_tty_path):
            acm_name = os.listdir(usb_deb_tty_path)[0]
            if acm_name == "":
                return ""
            dev_path = "/dev/" + acm_name
            if os.path.exists(dev_path):
                return dev_path
        return ""
