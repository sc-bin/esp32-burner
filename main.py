import os
import time
import usb_port

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

# import page_mode_burner
import page_choose


class RUN:
    def sloat_choose(self, num: int):
        print("收到选择", num)

    def __init__(self):
        self.page1 = page_choose.PAGE()
        self.page1.show()
        self.page1.signal_choose.connect(self.sloat_choose)


run = RUN()

sys.exit(app.exec_())
