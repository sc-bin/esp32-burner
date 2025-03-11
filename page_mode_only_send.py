import os
import time  # 导入time模块

from page_mode import *

from usb_port import USB_PORT
import transfer
import color


class PAGE(PAGE_MODE):
    file_dir: str
    files = []
    files_size = 0

    def set_color_run(self, usb_progress: USB_PROGRESS):
        usb_progress._label_ops.setStyleSheet(color.label_background.send_running)

    def set_color_end(self, usb_progress: USB_PROGRESS):
        usb_progress._label_ops.setStyleSheet(color.label_background.send_end)

    def set_color_error(self, usb_progress: USB_PROGRESS):
        usb_progress._label_ops.setStyleSheet(color.label_background.error)

    def run_in_connected(self, port: USB_PORT, usb_progress: USB_PROGRESS):
        start_time = time.time()  # 记录开始时间
        acm_path = port.get_dev_path()
        if os.path.exists(acm_path):
            print(acm_path)
        else:
            print("未找到acm路径")
            self.set_color_error(usb_progress)
            return
        usb_progress.print("正在清除板上py文件")
        transfer.TRANSFER(acm_path).files_clear()
        usb_progress.label_setText("发送文件...")
        self.set_color_run(usb_progress)
        total = 0
        # 挨个发送
        for i in self.files:
            now_file_size = os.path.getsize(i)
            relative_path = os.path.relpath(i, self.file_dir)  # 计算相对路径
            usb_progress.print(relative_path + " " + str(now_file_size))

            # 判断是否创建子文件夹
            if os.path.dirname(relative_path):  # 如果相对路径有父目录
                sub_dir = os.path.dirname(relative_path)
                transfer.TRANSFER(acm_path).mkdir_on_board(sub_dir)  # 创建子目录
            if transfer.TRANSFER(acm_path).send_file(
                i, relative_path
            ):  # 发送文件到相对路径
                total += now_file_size
                usb_progress.progress.set_value(int(total / self.files_size * 100))
            else:
                self.set_color_error(usb_progress)
                usb_progress.print("错误")
                usb_progress.label_setText("错误")

                return
            self.set_color_end(usb_progress)
        transfer.TRANSFER(acm_path).run_py_file(self.file_dir + "/main.py")
        end_time = time.time()  # 记录结束时间
        usb_progress.print(
            f"文件传输完成: {end_time - start_time:.2f} 秒"
        )  # 输出总共花费的时间
        usb_progress.label_setText("文件传输完成")

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
