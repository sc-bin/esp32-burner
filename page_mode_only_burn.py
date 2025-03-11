import os

from page_mode import *

from usb_port import USB_PORT
import transfer


class PAGE(PAGE_MODE):
    bin_file: str

    def set_color_run(self, usb_progress: USB_PROGRESS):
        usb_progress._label_ops.setStyleSheet(color.label_background.burn_running)

    def set_color_end(self, usb_progress: USB_PROGRESS):
        usb_progress._label_ops.setStyleSheet(color.label_background.burn_end)

    def set_color_error(self, usb_progress: USB_PROGRESS):
        usb_progress._label_ops.setStyleSheet(color.label_background.error)

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
            self.set_color_error(usb_progress)
            return
        usb_progress.print("开始烧BIN...")
        usb_progress.progress.set_value(0)
        self.set_color_run(usb_progress)
        usb_progress.label_setText("开始烧BIN...")

        def progress(value: int):
            usb_progress.progress.set_value(value)

        if transfer.TRANSFER(acm_path).burner_picoW(self.bin_file, progress):
            self.set_color_end(usb_progress)
            end_time = time.time()  # 记录结束时间
            usb_progress.print(
                f"烧BIN完成: {end_time - start_time:.2f} 秒"
            )  # 输出总共花费的时间
            usb_progress.progress.set_value(100)
            usb_progress.label_setText("烧BIN完成")

        else:
            self.set_color_error(usb_progress)
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
