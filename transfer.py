import os
import esptool


class TRANSFER(object):
    tty_path: str
    def __init__(self, tty_path: str):
        self.tty_path = tty_path
        if not os.path.exists(self.tty_path):
            print(tty_path, "路径不存在")
            exit(1)

    def is_in_burn_mode(self) -> bool:
        """判断设备是否进入烧录模式"""
        ret = os.system(f"timeout 3 ampy --port {self.tty_path} ls")
        if ret != 0:
            print("设备已进入烧录模式")
            return True
        else:
            print("设备未进入烧录模式")
            return False          

    def burner_picoW(self, firmware_path: str) -> bool:
        '''烧录picoW固件'''
        if not os.path.exists(firmware_path):
            print(firmware_path, "不存在")
            return False
        try:
            esptool.main(
                [
                    "--chip",
                    "esp32s3",
                    "--port",
                    self.tty_path,
                    "--after",
                    "hard_reset",
                    "write_flash",
                    "-z",
                    "0",
                    firmware_path,
                ]
            )
            print("烧录完成")
            return True
        except esptool.FatalError as e:
            print("烧录失败:", e)
        return False

    def send_py_file(self, py_path: str) -> bool:
        """发送文件到micropython板子上"""
        if not os.path.exists(py_path):
            print(py_path, "不存在")
            return False
        print("发送文件", os.path.basename(py_path), "到", self.tty_path)
        ret = os.system(f"ampy --port {self.tty_path} put {py_path}")
        if ret == 0:
            print("发送成功")
            return True
        else:
            print("发送失败")
            return False