import os

from page_mode import *

from usb_port import USB_PORT
import transfer


class PAGE(PAGE_MODE):
    bin_file: str

    def run_in_connected(self, port: USB_PORT, label: QtWidgets.QLabel):
        acm_path = port.get_dev_path()
        print("uSB插入", port.description)
        if os.path.exists(acm_path):
            print(acm_path)
        else:
            print("未找到acm路径")
            return
        label_set_stylesheet(label, ui.label_color_burn_bin.styleSheet())
        if transfer.TRANSFER(acm_path).burner_picoW(self.bin_file):
            label_set_stylesheet(label, ui.label_color_burn_bin_end.styleSheet())
        else:
            label_set_stylesheet(label, ui.label_color_error.styleSheet())

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
