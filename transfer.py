import os
import esptool

banudrate = 1152000
# banudrate = 921600


class AMPY_OPS(object):
    tty_path: str

    def __init__(self, tty_path: str):
        self.tty_path = tty_path

    def is_tty_exists(self) -> bool:
        """判断tty路径是否存在"""
        if not os.path.exists(self.tty_path):
            print(self.tty_path, "路径不存在")
            return False
        else:
            return True

    def run(self, command: str) -> bool:
        """运行命令,并返回是否运行成功"""
        if not os.path.exists(self.tty_path):
            print(self.tty_path, "路径不存在")
            return False
        ret = os.system(f"ampy --baud {banudrate} --port {self.tty_path} {command}")
        if ret == 0:
            print("运行成功")
            return True
        else:
            print("运行失败")
            return False

    def run_with_return(self, command: str) -> str:
        """运行命令，并返回该命令的输出"""
        if not os.path.exists(self.tty_path):
            print(self.tty_path, "路径不存在")
            return False
        ret = os.popen(
            f"ampy --baud {banudrate} --port {self.tty_path} {command}"
        )
        return ret.read()

    def is_in_burn_mode(self) -> bool:
        """判断设备是否进入烧录模式"""
        ret = os.system(f"timeout 3 ampy --port {self.tty_path} ls")
        if ret != 0:
            print("设备已进入烧录模式")
            return True
        else:
            print("设备未进入烧录模式")
            return False

    def send_file(self, py_path: str, dest_path="") -> bool:
        """发送文件到micropython板子指定路径上"""
        return self.run(f"put {py_path} {dest_path}")

    def files_clear(self) -> bool:
        """清除micropython板子上的文件"""
        self.run(f"rmdir /")
        return True

    def mkdir_on_board(self, dir_name: str) -> bool:
        """创建文件夹"""
        # 判断mpy上是否已经有同名文件夹
        if self.is_file_on_board(dir_name):
            print("文件夹已存在")
            return True
        return self.run(f"mkdir {dir_name}")

    def is_file_on_board(self, file_name: str) -> bool:
        """判断文件是否存在"""
        return self.run(f"ls | grep {file_name}")

    def reset_mpy_board(self):
        """重启micropython板子"""
        return self.run(f"reset")

    def run_py_file(self, file_name: str):
        """运行电脑上的文件"""
        return self.run(f"run {file_name}")


class TRANSFER(AMPY_OPS):
    tty_path: str

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

    def __init__(self, tty_path: str):
        super().__init__(tty_path)
