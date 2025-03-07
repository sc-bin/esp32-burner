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
import page_mode_only_send
import page_choose

PY_PATH = os.path.dirname(__file__) + "/要传输的py文件存放到此/py"
FIRMWARE_PATH = os.path.dirname(__file__) + "/待烧录的bin文件存放到此"
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

page_mode1 = page_mode_only_burn.PAGE(
    bin_file, USB_PORT(8, "左单"), USB_PORT(6, "中上"), USB_PORT(5, "中下")
)

page_mode2 = page_mode_only_send.PAGE(
    PY_PATH, USB_PORT(8, "左单"), USB_PORT(6, "中上"), USB_PORT(5, "中下")
)


def to_other_page(num: int):
    if num == 1:
        page_mode1.show()
    elif num == 2:
        page_mode2.show()


def show_choose_page():
    page1.show()


page1.signal_choose.connect(to_other_page)
page_mode1.signal_return.connect(show_choose_page)
page_mode2.signal_return.connect(show_choose_page)

show_choose_page()

sys.exit(app.exec_())
