import os

from page_mode import *

from usb_port import USB_PORT
import transfer


class PAGE(PAGE_MODE):
    bin_file: str

    def run_in_connected(self, port: USB_PORT, usb_progress: USB_PROGRESS):
        acm_path = port.get_dev_path()
        print("uSB插入", port.description)
        # 获取当前小时分钟秒的字符串
        if os.path.exists(acm_path):
            print(acm_path)
        else:
            print("未找到acm路径")
            label_set_stylesheet(usb_progress.label, ui.label_color_error.styleSheet())
            return
        usb_progress.print("开始烧BIN")
        label_set_stylesheet(usb_progress.label, ui.label_color_burn_bin.styleSheet())
        if transfer.TRANSFER(acm_path).burner_picoW(self.bin_file):
            label_set_stylesheet(
                usb_progress.label, ui.label_color_burn_bin_end.styleSheet()
            )
            usb_progress.print("烧BIN完成")
        else:
            label_set_stylesheet(usb_progress.label, ui.label_color_error.styleSheet())
            usb_progress.print("错误")

    def __init__(
        self,
        bin_file_path: str,
        usb1: USB_PORT,
        usb2: USB_PORT,
        usb3: USB_PORT,
    ):
        super().__init__(usb1, usb2, usb3)
        self.bin_file = bin_file_path
        self.usb1.callback = self.run_in_connected
        self.usb2.callback = self.run_in_connected
        self.usb3.callback = self.run_in_connected
        ui.textEdit_notice.setText("当前为仅烧录bin固件模式\n")
        ui.textEdit_notice.append(f"{os.path.basename(bin_file_path)}\n")
        # 获取当前事件得到一个小时分钟秒的字符串
