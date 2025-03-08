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
        """烧录picoW固件"""
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
        except:
            print("错误")
        return False

    def send_file(self, py_path: str, dest_path="") -> bool:
        """发送文件到micropython板子指定路径上"""
        if not os.path.exists(py_path):
            print(py_path, "不存在")
            return False
        print(self.tty_path, "发送文件", os.path.basename(py_path), "到", {dest_path})
        ret = os.system(f"ampy --port {self.tty_path} put {py_path} {dest_path}")
        if ret == 0:
            print("发送成功")
            return True
        else:
            print("发送失败")
            return False

    def files_clear(self) -> bool:
        """清除micropython板子上的文件"""
        ret = os.system(f"ampy --port {self.tty_path} rmdir /")
        if ret == 0:
            print("清除成功")
            return True
        else:
            print("清除失败")
            return False

    def mkdir_on_board(self, dir_name: str) -> bool:
        """创建文件夹"""
        ret = os.system(f"ampy --port {self.tty_path} mkdir {dir_name}")
        if ret == 0:
            print("创建成功")
            return True
        else:
            print("创建失败")
            return False

    def is_file_on_board(self, file_name: str) -> bool:
        """判断文件是否存在"""
        ret = os.system(f"ampy --port {self.tty_path} ls | grep {file_name}")
        if ret == 0:
            print(file_name, "文件存在")
            return True
        else:
            print(file_name, "文件不存在")
            return False

    def reset_mpy_board(self):
        """重启micropython板子"""
        ret = os.system(f"ampy --port {self.tty_path} reset")
        if ret == 0:
            print("重启成功")
            return True
        else:
            print("重启失败")
            return False

    def run_py_file(self, file_name: str):
        """运行电脑上的文件"""
        ret = os.system(f"ampy --port {self.tty_path} run {file_name}")
        if ret == 0:
            print("运行成功")
            return True
        else:
            print("运行失败")
            return False
