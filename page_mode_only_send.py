import os

from page_mode import *

from usb_port import USB_PORT
import transfer


class PAGE(PAGE_MODE):
    file_dir: str
    files = []
    files_size = 0

    def run_in_connected(self, port: USB_PORT, usb_progress: USB_PROGRESS):
        acm_path = port.get_dev_path()
        if os.path.exists(acm_path):
            print(acm_path)
        else:
            label_set_stylesheet(usb_progress.label, ui.label_color_error.styleSheet())
            print("未找到acm路径")
            return
        # for循环遍历files列表，挨个发送
        total = 0
        for i in self.files:
            f = i
            now_file_size = os.path.getsize(i)
            usb_progress.print(f.replace(self.file_dir, "") + " " + str(now_file_size))
            label_set_stylesheet(
                usb_progress.label, ui.label_color_send_py.styleSheet()
            )
            if transfer.TRANSFER(acm_path).send_py_file(i):
                # 计算目前发送完成的文件体积的占总文件体积的百分之多少
                total += now_file_size
                usb_progress.progress.set_value(int(total/self.files_size*100))

            else:
                label_set_stylesheet(
                    usb_progress.label, ui.label_color_error.styleSheet()
                )
                print("退出")
                break

    def __init__(
        self,
        py_file_dir: str,
        usb1: USB_PORT,
        usb2: USB_PORT,
        usb3: USB_PORT,
    ):
        super().__init__(usb1, usb2, usb3)
        self.file_dir = py_file_dir
        self.usb1.callback = self.run_in_connected
        self.usb2.callback = self.run_in_connected
        self.usb3.callback = self.run_in_connected
        ui.textEdit_notice.setText("当前为仅发送文件,文件列表如下")
        # 遍历py_file_dir路径下所有子文件夹，将搜索到的所有文件的完整路径都添加到列表
        for root, dirs, files in os.walk(py_file_dir):
            for file in files:
                self.files.append(os.path.join(root, file))

        # 计算总文件大小
        for i in self.files:
            self.files_size += os.path.getsize(i)

        ui.textEdit_notice.append(f"共{self.files_size}Byte")

        # 挨个输出文件名
        for i in self.files:
            ui.textEdit_notice.append(i.replace(py_file_dir, ""))
