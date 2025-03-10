import os

from page_mode import *

from usb_port import USB_PORT
import transfer


class PAGE(PAGE_MODE):
    bin_file: str

    def run_in_connected(self, port: USB_PORT, usb_progress: USB_PROGRESS):

        start_time = time.time()  # 记录开始时间
        acm_path = port.get_dev_path()
        print("uSB插入", port.description)
        usb_progress.progress.set_value(0)
        # 获取当前小时分钟秒的字符串
        if os.path.exists(acm_path):
            print(acm_path)
        else:
            print("未找到acm路径")
            label_set_stylesheet(usb_progress.label, color.label_background.error)
            return
        usb_progress.print("开始烧BIN...")
        usb_progress.progress.set_value(0)
        label_set_stylesheet(usb_progress.label, color.label_background.burn_running)
        usb_progress.label_setText("开始烧BIN...")

        def progress(value: int):
            usb_progress.progress.set_value(value)

        if transfer.TRANSFER(acm_path).burner_picoW(self.bin_file, progress):
            label_set_stylesheet(usb_progress.label, color.label_background.burn_end)
            end_time = time.time()  # 记录结束时间
            usb_progress.print(
                f"烧BIN完成: {end_time - start_time:.2f} 秒"
            )  # 输出总共花费的时间
            usb_progress.progress.set_value(100)
            usb_progress.label_setText("烧BIN完成")

        else:
            label_set_stylesheet(usb_progress.label, color.label_background.error)
            usb_progress.print("错误")
            usb_progress.label_setText("错误")
            usb_progress.progress.set_value(0)

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
