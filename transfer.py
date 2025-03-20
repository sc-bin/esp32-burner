import os
import subprocess
import re  # 添加正则表达式模块

baudrate = 1152000
# baudrate = 921600
# baudrate = 115200


class RSHELL_OPS(object):
    tty_path: str

    def __init__(self, tty_path: str):
        self.tty_path = tty_path

    def replace_space(self, command: str) -> str:
        """替换空格为\ """
        return command.replace(" ", "\\ ")
    def is_tty_exists(self) -> bool:
        """判断tty路径是否存在"""
        if not os.path.exists(self.tty_path):
            print(self.tty_path, "路径不存在")
            return False
        else:
            return True

    def run_rshell(self, command: str) -> bool:
        """运行命令,并返回是否运行成功"""
        print("运行命令:", command)
        if not os.path.exists(self.tty_path):
            print(self.tty_path, "路径不存在")
            return False
        ret = os.system(f"rshell --baud {baudrate} --port {self.tty_path} {command}")
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
        ret = os.popen(f"rshell --baud {baudrate} --port {self.tty_path} {command}")
        return ret.read()

    def is_in_burn_mode(self) -> bool:
        """判断设备是否进入烧录模式"""
        ret = os.system(f"timeout 3 rshell --port {self.tty_path} ls")
        if ret != 0:
            print("设备已进入烧录模式")
            return True
        else:
            print("设备未进入烧录模式")
            return False

    def send_file(self, py_path: str, dest_path="") -> bool:
        """发送文件到micropython板子指定路径上"""
        return self.run_rshell(f"cp \"{self.replace_space(py_path)}\" \"/pyboard/{self.replace_space(dest_path)}\"")

    def files_clear(self) -> bool:
        """清除micropython板子上的文件"""
        self.run_rshell(f"rm -rf /pyboard/*")
        return True

    def mkdir_on_board(self, dir_name: str) -> bool:
        """创建文件夹"""
        # 判断mpy上是否已经有同名文件夹
        if self.is_file_on_board(dir_name):
            print("文件夹已存在")
            return True
        return self.run_rshell(f"mkdir /pyboard/{dir_name}")

    def is_file_on_board(self, file_name: str) -> bool:
        """判断文件是否存在"""
        output = self.run_with_return(f"ls /pyboard/")
        return file_name in output

    def reset_mpy_board(self):
        """重启micropython板子"""
        return self.run_rshell(f"repl ~ import machine; machine.reset()")


class AMPY_OPS(object):
    tty_path: str

    def __init__(self, tty_path: str):
        self.tty_path = tty_path

    def run_ampy(self, command: str) -> bool:
        """传入ampy命令运行"""
        if not os.path.exists(self.tty_path):
            print(self.tty_path, "路径不存在")
            return False
        ret = os.system(f"ampy --port {self.tty_path} {command}")
        if ret == 0:
            print("运行成功")
            return True
        else:
            print("运行失败")
            return False

    def run_py_file(self, file_name: str):
        """运行电脑上的文件"""
        return self.run_ampy(f"run {file_name}")


class TRANSFER(RSHELL_OPS, AMPY_OPS):
    tty_path: str

    def burner_picoW(self, firmware_path: str, progress_callback=None) -> bool:
        """烧录picoW固件"""
        if not os.path.exists(firmware_path):
            print(firmware_path, "不存在")
            return False
        try:
            command = [
                "esptool.py",
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
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
            )
            last_progress = -1
            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    print(output.strip())
                    # 解析进度信息
                    if "Writing at" in output:
                        # 使用正则表达式提取百分比
                        match = re.search(r"(\d+) %", output)
                        if match:
                            progress = int(match.group(1))
                            if progress != last_progress:
                                last_progress = progress
                                if progress_callback:
                                    progress_callback(progress)
            rc = process.poll()
            if rc == 0:
                print("烧录完成")
                return True
            else:
                print("烧录失败")
                return False
        except Exception as e:
            print("错误:", e)
        return False

    def __init__(self, tty_path: str):
        RSHELL_OPS.__init__(self, tty_path)
        AMPY_OPS.__init__(self, tty_path)
