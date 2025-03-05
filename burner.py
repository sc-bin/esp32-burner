import os
import esptool


class BURNER(object):
    tty_path: str

    def __init__(self, tty_path: str):
        self.tty_path = tty_path
        if not os.path.exists(self.tty_path):
            print(tty_path, "路径不存在")
            exit(1)

    def burner_picoW(self, firmware_path: str) -> bool:
        if not os.path.exists(firmware_path):
            print(firmware_path, "不存在")
            return False

        print("烧录文件", os.path.basename(firmware_path), "到", self.tty_path)
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
        except:
            print("烧录失败:")
        return False

    def send_main_py(self, py_path: str) -> bool:
        """
        发送文件到micropython板子上
        """
        if not os.path.exists(py_path):
            print(py_path, "不存在")
            return False
        print("发送文件", os.path.basename(py_path), "到", self.tty_path)
        os.system(f"ampy --port {self.tty_path} put {py_path}")
