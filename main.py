from usb_port import USB_PORT


# 【可选代码】允许远程运行
import os

os.environ["DISPLAY"] = ":0.0"

# 【建议代码】允许终端通过ctrl+c中断窗口，方便调试
import signal
from PyQt5 import QtCore

signal.signal(signal.SIGINT, signal.SIG_DFL)
timer = QtCore.QTimer()
timer.start(100)  # You may change this if you wish.
timer.timeout.connect(lambda: None)  # Let the interpreter run each 100 ms

# 初始化窗口
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

import page_mode_only_burn
import page_choose


FIRMWARE_PATH = os.path.dirname(__file__) + "/烧录文件存放文件夹"
# 查找FIRMWARE_PATH路径下第一个.bin文件
bin_file = None
for file in os.listdir(FIRMWARE_PATH):
    if file.endswith(".bin"):
        bin_file = os.path.join(FIRMWARE_PATH, file)
        break
if bin_file is None:
    print("未找到.bin文件")
    exit(1)
else:
    print("bin文件 : ", os.path.basename(bin_file))


page1 = page_choose.PAGE()
page_only_burn = page_mode_only_burn.PAGE(
    bin_file, USB_PORT(8, "左单"), USB_PORT(6, "中上"), USB_PORT(5, "中下")
)


def sloat_choose(num: int):
    if num == 1:
        page_only_burn.show()


def sloat_to_choose():
    page1.show()
    page1.signal_choose.connect(sloat_choose)


page_only_burn.signal_return.connect(sloat_to_choose)
sloat_to_choose()

sys.exit(app.exec_())
